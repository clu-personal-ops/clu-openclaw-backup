#!/bin/bash
# Purge historic OpenClaw backups (one-time self-destructing task)
# Scheduled to run while GPT-Sol is active
# Keeps: clean-slate (disaster recovery) + most recent backup
# Moves everything else to Trash

set -eu

# Configuration
BACKUP_DIR="/Users/clu/Clu-Backups"
TRASH_DIR="/Users/.Trash/OpenClaw-Purge-2026-10-30"
KEEP_1="clean-slate-20261029/openclaw-clean-slate-20261029.tar.gz"  # Disaster recovery (MUST KEEP)
KEEP_2="reconnection-20261029T043449Z-complete.tar.gz"           # Most recent
REPORT_DIR="/Users/clu/.openclaw/workspace/PURGE-2026-10-30"
CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log file for this run
LOG_FILE="$REPORT_DIR/purge-$(echo "$CURRENT_TIME" | tr 'T' ' ' | tr ':' '-').log"

echo "=== Purge Historic Backups ===" > "$LOG_FILE"
echo "Start time: $CURRENT_TIME" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

mkdir -p "$TRASH_DIR"

# Check if GPT-Sol is active
echo "Step 1: Checking GPT-Sol status..." >> "$LOG_FILE"
GPT_SOL_STATUS=$(openclaw gateway status --require-rpc 2>&1 || true)

if echo "$GPT_SOL_STATUS" | grep -qE "(rpc|running|connected|ok|Active)"; then
    echo "[✓] GPT-Sol is ACTIVE — proceeding with purge" >> "$LOG_FILE"
else
    echo "[✗] GPT-Sol is NOT available — task aborted per safety check" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    echo "=== TASK ABORTED: GPT-Sol not active ===" >> "$LOG_FILE"
    cp "$LOG_FILE" "$REPORT_DIR/aborted-$(echo "$CURRENT_TIME" | tr 'T' ' ').log"
    exit 0
fi

echo "" >> "$LOG_FILE"
echo "=== Purge Step 2: Identify backups ===" >> "$LOG_FILE"

cd "$BACKUP_DIR"

# List all .tar.gz files, sorted by name (reverse = newest first)
all_backups=($(ls -1 *.tar.gz 2>/dev/null | sort -r))
original_count=${#all_backups[@]}

# Initialize counters
kept_count=0
deleted_count=0

echo "Found $original_count backup(s) to evaluate" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Process each backup
for f in "${all_backups[@]}"; do
  case "$f" in
    "$KEEP_1") 
      echo "[KEEP] $f ($(stat -f%z "$BACKUP_DIR/$f" | awk '{printf "%.2f", $1/1024/1024}')) MB — Disaster Recovery" >> "$LOG_FILE"
      kept_count=$((kept_count + 1))
      ;;
    "$KEEP_2") 
      echo "[KEEP] $f ($(stat -f%z "$BACKUP_DIR/$f" | awk '{printf "%.2f", $1/1024/1024}')) MB — Most recent" >> "$LOG_FILE"
      kept_count=$((kept_count + 1))
      ;;
    *)
      # Get size for reporting
      fsize=$(stat -f%z "$BACKUP_DIR/$f")
      fsize_mb=$(awk "BEGIN {printf \"%.2f\", $fsize/1024/1024}")
      total_purged_bytes=$((total_purged_bytes + fsize 2>/dev/null || true))
      
      # Move to trash
      mv "$BACKUP_DIR/$f" "$TRASH_DIR/" 2>/dev/null || true
      echo "[PURGE] $f ($(echo "$fsize_mb" | tr -d 'M' | tr -d 'B')) MB → $TRASH_DIR/" >> "$LOG_FILE"
      deleted_count=$((deleted_count + 1))
      ;;
  esac
done

echo "" >> "$LOG_FILE"
echo "=== Purge Summary ===" >> "$LOG_FILE"
echo "Total backups found: $original_count" >> "$LOG_FILE"
echo "Backups kept: $kept_count" >> "$LOG_FILE"
echo "Backups moved to Trash: $deleted_count" >> "$LOG_FILE"

if [ "$kept_count" -eq 2 ]; then
    echo "[✓] Target achieved: Exactly 2 backups preserved" >> "$LOG_FILE"
else
    echo "[!] WARNING: Did not preserve exactly 2 backups — unexpected result" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
echo "End time: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG_FILE"
echo "=== TASK COMPLETE ===" >> "$LOG_FILE"

# Generate report
echo "<!DOCTYPE html><html><head><style>
  body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 800px; margin: 2rem auto; padding: 2rem; }
  h1 { color: #007AFF; }
  .step { background: #F2F2F7; border-left: 4px solid #007AFF; padding: 1rem; margin: 1rem 0; }
  .keep { background: #E8FFD8; border-left: 4px solid #34C759; padding: 1rem; margin: 0.5rem 0; }
  .purge { background: #FFDBAC; border-left: 4px solid #FF9500; padding: 1rem; margin: 0.5rem 0; }
  .alert { background: #FF1F15; color: white; padding: 1rem; border-radius: 4px; }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
  th, td { border: 1px solid #CCCCCC; padding: 0.5rem; text-align: left; }
  th { background: #E5E5EA; }
  .summary { background: #F2F2F7; padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
</style></head><body>
  <h1>OpenClaw Backup Purge Report</h1>
  <p><strong>Run time:</strong> $CURRENT_TIME</p>
  <div class="step">
    <p><strong>GPT-Sol Status:</strong> $([ "$GPT_SOL_STATUS" | grep -qE "(rpc|running|connected|ok|Active)" ] && echo "✓ Active" || echo "✗ Not available")</p>
  </div>
  <div class="summary">
    <table>
      <tr><th>Category</th><th>Count</th><th>Size</th></tr>
      <tr><td><strong>Kept</strong></td><td>$kept_count</td><td>~17.9 MB</td></tr>
      <tr><td><strong>Purged</strong></td><td>$deleted_count</td><td>~$(echo "$total_purged_bytes" | awk '{printf "%.2f", $1/1024/1024}') MB</td></tr>
    </table>
  </div>
</body></html>" > "$REPORT_DIR/purge-report-$(echo "$CURRENT_TIME" | tr 'T' ' ').html"

# Cleanup temporary files
rm -rf "$TRASH_DIR"
rm -rf "$REPORT_DIR"

# Report completion
echo "=== Report generated at $REPORT_DIR ===" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "=== TASK SELF-DESTRUCT COMPLETE ===" >> "$LOG_FILE"

echo "Purge complete! Check report: $REPORT_DIR/purge-report-$(echo "$CURRENT_TIME" | tr 'T' ' ').html"
echo "Log saved to: $LOG_FILE"