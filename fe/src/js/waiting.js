import { show, setWidth, setHeight, center, onWindowResize, minAppDimension, getWidth, onEvent, apiWaitingImage } from './utils.js';

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

onWindowResize(dim);

window.addEventListener('init', () => {
    onWindowResize(dim);
});

window.addEventListener('start', showWaitingArea);

onEvent('uploaded', ({ uid }) => {
    waitingImgElement.src = apiWaitingImage(uid);
});


export { waitingDim }