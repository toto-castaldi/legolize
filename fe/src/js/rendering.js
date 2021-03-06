import { onEvent, websocketUrl, show, sendEvent, hide, store } from './utils.js';

let connection;


const renderProgressElement = document.getElementById('render-progress');
const progressElement = document.getElementById('progress');
const labelRenderProgressElement = document.getElementById('label-progress');
const labels = {
    'point': 'Clustering (1/3) :',
    'palette': 'Apply palette (2/3) :',
    'piece': 'Compute pieces (3/3) :'
}



onEvent('waitingLoaded', () => {
    const uid = store()["uid"];
    const size = store()["size"];
    const pieces = [];
    connection = new WebSocket(websocketUrl("fullgenerate"));
    connection.onopen = () => {
        connection.send(JSON.stringify({ uid, size }));
        show(renderProgressElement);
        renderProgressElement.value = 0;
        labelRenderProgressElement.innerHTML = "";
    };
    connection.onmessage = (event) => {
        const eventData = JSON.parse(event.data);
        if (eventData.action == "size") {
            store()["size"] = { "w": eventData.w, "h": eventData.h };
        }
        if (eventData.action == "piece") {
            pieces.push(eventData.piece);
        }
        if (eventData.progress) {
            labelRenderProgressElement.innerHTML = `${labels[eventData.action]}`;
            progressElement.value = eventData.progress;
        }
        if (eventData.action == "endPieces") {
            hide(renderProgressElement);
            connection.close();
            store()["pieces"] = pieces;
            sendEvent('renderingDone');
        }
    }
});