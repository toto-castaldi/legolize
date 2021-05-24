import { postFormData, sendEvent, onEvent, disableElement, enableElement } from './utils.js';
import { waitingDim } from './waiting.js';

const filePickerElement = document.getElementById('file-picker')
const sizeElement = document.getElementById('size')

onEvent('init', () => {
    sizeElement.onchange = (e) => {
        e.preventDefault();
        if (sizeElement.value > 0) {
            disableElement(sizeElement);
            enableElement(filePickerElement);
        }
    }

    filePickerElement.onchange = async(e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", filePickerElement.files[0]);
        const res = await postFormData(`upload/${waitingDim()}`, {
            formData
        });
        const json = await res.json();
        sendEvent('uploaded', { uid: json.uid, size: sizeElement.value });
        disableElement(filePickerElement);
    }
});