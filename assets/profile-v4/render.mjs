// Render the checked-in source in an isolated browser; set CDP_MODULE to the local CDP helper.
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
const here=dirname(fileURLToPath(import.meta.url));
if(!process.env.CDP_MODULE) throw Error('Set CDP_MODULE to an existing CDP browser helper');
const {Browser}=await import(pathToFileURL(resolve(process.env.CDP_MODULE)).href);
const browser=await Browser.launch();
try {for(const [name,width,height,hash] of [['wide',1200,550,''],['mobile',720,850,'#mobile']]) {const page=await browser.newPage({width,height,dsf:1}); await page.goto(pathToFileURL(resolve(here,'cover.html')).href+hash,{settleMs:500});const state=await page.eval(async()=>{await document.fonts.ready; const i=document.querySelector('img');await i.decode();return {width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,font:document.fonts.check('24px Instrument'),image:i.naturalWidth}}); if(state.width!==width||state.height!==height||!state.font||!state.image)throw Error(JSON.stringify(state)); await page.screenshot({path:resolve(here,`cover-${name}.png`),format:'png'});console.log(name,state);await page.close()}} finally {await browser.close()}
