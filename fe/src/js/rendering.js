import { onEvent, websocketUrl } from './utils.js';

let connection;

onEvent('waitingLoaded', ({ uid, size }) => {
    connection = new WebSocket(websocketUrl("fullgenerate"));
    connection.onopen = () => {
        connection.send(JSON.stringify({ uid, size }));
    };
    connection.onmessage = (event) => {
        const eventData = JSON.parse(event.data);
        console.log(eventData);
    }
});