import { postFormData, sendEvent } from './utils.js';
import { waitingDim } from './waiting.js';

const inputImageElement = document.getElementById('file-picker')

window.addEventListener('init', () => {
    inputImageElement.onchange = async(e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", inputImageElement.files[0]);
        const res = await postFormData(`upload/${waitingDim()}`, {
            formData
        });
        const json = await res.json();
        sendEvent('uploaded', json);
    }
});