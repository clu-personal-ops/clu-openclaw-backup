// Restores the original hourly definition; does not restart the Gateway or change credentials.
import fs from 'node:fs';
import {cli} from '../../scripts/usage-monitor.mjs';
const original=JSON.parse(fs.readFileSync(new URL('./job.json',import.meta.url),'utf8'));
const jobs=cli(['automations','list','--all','--json']).jobs;
for(const j of jobs) if(j.declarationKey?.startsWith('openai-usage-expiration:'+original.id)) cli(['automations','rm',j.id]);
const fields=['displayName','description','sessionTarget','payload','trigger','delivery','failureAlert','schedule','enabled'];
const patch=Object.fromEntries(fields.map(k=>[k,original[k]]));
console.log(JSON.stringify(cli(['gateway','call','cron.update','--json','--params',JSON.stringify({id:original.id,patch})]),null,2));
