import { hide, onEvent, removeClass, show, apiThumbnailImage, sendEvent, store } from './utils.js';

const waitingImg = document.getElementById("waiting-img");
const thumbnailContainer = document.getElementById("thumbnail-container");
const thumbnailImg = document.getElementById("thumbnail-img");
const app = document.getElementById("app");

onEvent("renderingDone", () => {
    const uid = store()["uid"];
    removeClass(waitingImg, 'waiting-img');
    const startingR = waitingImg.getBoundingClientRect();
    //app.appendChild(waitingImg);
    waitingImg.style.position = "fixed";
    waitingImg.style.top = `${startingR.top}px`;
    waitingImg.style.left = `${startingR.left}px`;
    waitingImg.style.width = `${startingR.width}px`;
    waitingImg.style.height = `${startingR.height}px`;

    const wR = waitingImg.getBoundingClientRect();
    const tR = thumbnailContainer.getBoundingClientRect();
    const wX = wR.left + (wR.width / 2) - (tR.width / 2);
    const wY = wR.top + (wR.height / 2) - (tR.height / 2);

    const tX = tR.left - wX;
    const tY = tR.top - wY;
    const sX = tR.width / wR.width;
    const sY = tR.height / wR.height;
    waitingImg.style.transition = "all 1s";
    waitingImg.style.transform = `translateX(${tX}px) translateY(${tY}px) scale(${sX}, ${sY})`;
    let end = false;
    waitingImg.ontransitionend = () => {
        if (!end) {
            end = true;
            thumbnailImg.src = apiThumbnailImage(uid);
            show(thumbnailContainer);
            hide(waitingImg);
            sendEvent("animWaitingDone");
        }
    };



});