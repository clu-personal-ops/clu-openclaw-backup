import fs from 'node:fs';
import assert from 'node:assert/strict';
import {fetchUsage,run,ROOT} from '../../scripts/usage-monitor.mjs';
const path=ROOT+'/state/usage-monitor.json';const before=fs.readFileSync(path);const previous=JSON.parse(before);const sample=await fetchUsage(0);assert(!sample.error,'Reliable live signal required; no success on missing usage');
let saved;const output=await run({load:()=>previous,save:s=>saved=s,fetch:async()=>sample,sync:s=>s});
assert(fs.readFileSync(path).equals(before));
console.log(JSON.stringify({phase:sample.phase,weeklyRemaining:sample.weeklyRemaining,snapshotAgeMs:Date.now()-sample.updatedAt,output:output==='NO_REPLY'?'NO_REPLY':'transition detected but not delivered',stateWrites:0,schedulerMutations:0,notifications:0,inferenceCalls:0}));
