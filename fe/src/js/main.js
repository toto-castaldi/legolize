import { showWaitingArea } from './waiting.js';

let appState = 'WAITING';

switch (appState) {
    case 'WAITING':
        showWaitingArea();
        break;
    default:
        break;
}