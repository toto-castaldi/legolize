import { onEvent, addClass, store } from './utils.js';

const fileBrowseElement = document.getElementById("file-browse");
const app = document.getElementById("app");


onEvent("animWaitingDone", () => {
    const pictureW = store()["size"]["w"];
    const pictureH = store()["size"]["h"];
    const pieces = store()["pieces"];

    let scale = 1;

    let startDrag = undefined;
    let delta = {
        x: 0,
        y: 0
    }
    let transitionDelay = 3000;
    const fR = fileBrowseElement.getBoundingClientRect();

    const render = document.getElementById("render");
    const renderW = render.clientWidth;
    const renderH = render.clientHeight;
    const minRenderLen = (renderW > renderH ? renderH : renderW) * 0.9 * scale;
    const maxRenderElement = pictureW > pictureH ? pictureW : pictureH;
    const elementLen = minRenderLen / maxRenderElement;
    const centerX = renderW / 2 + delta.x;
    const centerY = renderH / 2 + delta.y;
    const startX = centerX - (pictureW / 2) * elementLen;
    const startY = centerY - (pictureW / 2) * elementLen;

    let index = 0;

    const putPiece = () => {
        const piece = pieces[index];
        const w = piece.size[0];
        const h = piece.size[1];
        const pieceDiv = document.createElement("div");
        addClass(pieceDiv, "piece");
        const top = fR.top + 100;
        pieceDiv.style.top = `${top}px`;
        pieceDiv.style.width = `${w * elementLen}px`;
        pieceDiv.style.height = `${h * elementLen}px`;
        app.appendChild(pieceDiv);
        for (let x = 0; x < w; x++) {
            for (let y = 0; y < h; y++) {
                const piecePoint = document.createElement("div");
                addClass(piecePoint, "piece-point");
                piecePoint.style.top = `${y * elementLen}px`;
                piecePoint.style.left = `${x * elementLen}px`;
                piecePoint.style.width = `${elementLen}px`;
                piecePoint.style.height = `${elementLen}px`;
                addClass(piecePoint, `palette-${piece.color}`);
                pieceDiv.appendChild(piecePoint);
            }
        }
        const pR = pieceDiv.getBoundingClientRect();
        const tX = startX + piece.position[0] * elementLen - pR.left;
        const tY = startY + piece.position[1] * elementLen - pR.top;
        if (transitionDelay > 100) {
            transitionDelay -= 100;
        }
        pieceDiv.style.transition = `all ${transitionDelay}ms`;
        pieceDiv.style.transform = `translateX(${tX}px) translateY(${tY}px)`;
        let end = false;
        pieceDiv.ontransitionend = () => {
            if (!end) {
                end = true;
                index++;
                if (index < pieces.length) {
                    putPiece()
                }
            }
        };
    }

    putPiece();

});