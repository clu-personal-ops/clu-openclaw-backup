#!/usr/bin/env python3
"""Restore only this repair's settings, refusing to overwrite later edits."""
import json, pathlib, subprocess, os, sys
root = pathlib.Path(__file__).resolve().parent
manifest = json.loads((root / 'rollback-manifest.json').read_text())
current = json.loads(pathlib.Path('/Users/clu/.openclaw/openclaw.json').read_text())
provider = current['models']['providers'][manifest['provider']]
for path, expected in manifest['expected'].items():
    actual = current['agents']['defaults']['models'][manifest['modelRef']].get('params') if path.startswith('agents.') else provider.get(path.rsplit('.', 1)[1])
    if actual != expected:
        sys.exit('Refusing rollback: a repaired setting changed after verification. Review rollback-manifest.json.')
settings_path = pathlib.Path('/Users/clu/.lmstudio/settings.json')
settings = json.loads(settings_path.read_text())
if settings['developer']['unloadPreviousJITModelOnLoad'] is not False:
    sys.exit('Refusing rollback: LM Studio auto-eviction setting changed after verification.')
batch = root / 'rollback-batch.json'
batch.write_text(json.dumps(manifest['restore'], indent=2))
subprocess.run(['openclaw','config','set','--batch-file',str(batch),'--replace','--dry-run'], check=True)
subprocess.run(['openclaw','config','set','--batch-file',str(batch),'--replace'], check=True)
for path in manifest['unset']:
    subprocess.run(['openclaw','config','unset',path], check=True)
settings = json.loads(settings_path.read_text())
settings['developer']['unloadPreviousJITModelOnLoad'] = manifest['lmstudioAutoEvictOriginal']
tmp = settings_path.with_name('settings.rollback.tmp')
tmp.write_text(json.dumps(settings, indent=2) + '\n')
os.chmod(tmp, settings_path.stat().st_mode)
os.replace(tmp, settings_path)
subprocess.run(['openclaw','config','validate'], check=True)
print('Scoped rollback completed. Sol routes and unrelated settings were not restored or replaced.')
