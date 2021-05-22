import { show, setWidth, setHeight, center, onWindowResize, minAppDimension } from './utils.js';

const waitingElement = document.getElementById('waiting')

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

onWindowResize(dim);

export { showWaitingArea }