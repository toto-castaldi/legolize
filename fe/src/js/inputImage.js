import { postFormData, sendEvent, onEvent, disableElement } from './utils.js';
import { waitingDim } from './waiting.js';

const filePickerElement = document.getElementById('file-picker')
const sizeElement = document.getElementById('size')

onEvent('init', () => {
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
        disableElement(sizeElement);
    }
});