import { onEvent, removeClass } from './utils.js';

const waitingImg = document.getElementById("waiting-img");
const thumbnailContainer = document.getElementById("thumbnail-container");
const app = document.getElementById("app");

onEvent('renderingDone', ({ pieces }) => {

    console.log(pieces.length);
    removeClass(waitingImg, 'waiting-img');
    const startingR = waitingImg.getBoundingClientRect();
    app.appendChild(waitingImg);
    waitingImg.style.position = "fixed";
    waitingImg.style.top = `${startingR.top}px`;
    waitingImg.style.left = `${startingR.left}px`;
    waitingImg.style.width = `${startingR.width}px`;
    waitingImg.style.height = `${startingR.height}px`;

    const wR = waitingImg.getBoundingClientRect();
    const tR = thumbnailContainer.getBoundingClientRect();
    const tX = tR.left - wR.left;
    const tY = tR.top - wR.top;
    const sX = 10 * tR.width / wR.width;
    const sY = 10 * tR.height / wR.height;
    waitingImg.style.transition = "all 5s";
    waitingImg.style.transform = `translateX(${tX}px) translateY(${tY}px) scale(${sX}, ${sY})`;
    //console.log(`translateX(${tX}px) translateY(${tY}px) scale(${sX}, ${sY})`);
    //waitingImg.style.transform = `translateY(${tY}px)`;
    //waitingImg.style.transform = `scale(${sX}, ${sY})`;

});