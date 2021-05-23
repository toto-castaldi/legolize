import { onEvent, websocketUrl, show } from './utils.js';

let connection;


const renderProgressElement = document.getElementById('render-progress');
const progressElement = document.getElementById('progress');
const labelRenderProgressElement = document.getElementById('label-progress');
const labels = {
    'point': 'Clustering (1/3) :',
    'palette': 'Apply palette (2/3) :',
    'piece': 'Compute pieces (3/3) :'
}



onEvent('waitingLoaded', ({ uid, size }) => {
    connection = new WebSocket(websocketUrl("fullgenerate"));
    connection.onopen = () => {
        connection.send(JSON.stringify({ uid, size }));
        show(renderProgressElement);
        renderProgressElement.value = 0;
        labelRenderProgressElement.innerHTML = "";
    };
    connection.onmessage = (event) => {
        const eventData = JSON.parse(event.data);
        if (eventData.action.startsWith("end")) {
            console.log(eventData);
        }
        if (eventData.progress) {
            labelRenderProgressElement.innerHTML = `${labels[eventData.action]}`;
            progressElement.value = eventData.progress;
        }
    }
});