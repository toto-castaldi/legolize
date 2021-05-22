import { sendEvent, show, setWidth, setHeight, center, onWindowResize, minAppDimension, getWidth, onEvent, apiWaitingImage, post } from './utils.js';

const waitingElement = document.getElementById('waiting');
const waitingImgElement = document.getElementById('waiting-img');

const dim = () => {
    const dim = minAppDimension() * 0.9;
    setWidth(waitingElement, dim);
    setHeight(waitingElement, dim);
    center(waitingElement, dim, dim);
};

const showWaitingArea = () => {
    dim();
    show(waitingElement);
}

const waitingDim = () => getWidth(waitingElement)

window.addEventListener('init', () => {
    onWindowResize(dim);
    showWaitingArea();
});

onEvent('uploaded', ({ uid, size }) => {
    waitingImgElement.src = apiWaitingImage(uid);
    sendEvent('waitingLoaded', { uid, size });
});


export { waitingDim }