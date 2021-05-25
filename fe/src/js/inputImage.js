import { postFormData, sendEvent, onEvent, disableElement, enableElement, hide, show, store, addClass } from './utils.js';
import { waitingDim } from './waiting.js';

const filePickerElement = document.getElementById("file-picker");
const sizeElement = document.getElementById("size");
const choosenSizeElement = document.getElementById("choosen-size");
const waitingImg = document.getElementById("waiting-img");
const waitingElement = document.getElementById("waiting");
const app = document.getElementById("app");




onEvent("init", () => {
    sizeElement.onchange = (e) => {
        e.preventDefault();
        if (sizeElement.value > 0) {
            choosenSizeElement.value = sizeElement.value;
            disableElement(sizeElement);
            show(choosenSizeElement);
            enableElement(filePickerElement);
        }
    }

    filePickerElement.onchange = async(e) => {
        const pieces = document.getElementsByClassName("piece")
        for (let i = pieces.length - 1; i >= 0; i--) {
            pieces[i].remove();
        }
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", filePickerElement.files[0]);
        const res = await postFormData(`upload/${waitingDim()}`, {
            formData
        });
        const json = await res.json();
        store()["uid"] = json.uid;
        store()["size"] = sizeElement.value;
        sendEvent('uploaded');
        disableElement(filePickerElement);
    }
});

onEvent("constructionDone", () => {
    waitingImg.attributeStyleMap.clear();
    waitingElement.appendChild(waitingImg);
    addClass(waitingImg, "waiting-img");

    hide(choosenSizeElement);
    enableElement(sizeElement);
    filePickerElement.value = "";
    sizeElement.value = "";
});