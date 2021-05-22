import { setUrl, sendEvent } from './utils.js';
import './waiting.js';
import './inputImage.js';
import './rendering.js';


const configRes = await fetch("config.json");
const configJson = await configRes.json();
setUrl(configJson);
sendEvent('init');