import { components, postFormData, sendEvent, onEvent, disableElement, enableElement, hide, show, store, addClass } from './utils.js';
import { waitingDim } from './waiting.js';


onEvent("init", () => {
    components.sizeElement.onchange = (e) => {
        e.preventDefault();
        if (components.sizeElement.value > 0) {
            /*       components.waitingImgElement.attributeStyleMap.clear();
            addClass(components.waitingImgElement, "waiting-img");
            show(components.waitingImgElement);
 */
            enableElement(components.filePickerElement);
        }
    }

    components.filePickerElement.onchange = async(e) => {
        const pieces = document.getElementsByClassName("piece")
        for (let i = pieces.length - 1; i >= 0; i--) {
            pieces[i].remove();
        }
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", components.filePickerElement.files[0]);
        const res = await postFormData(`upload/${waitingDim()}`, {
            formData
        });
        const json = await res.json();
        store()["uid"] = json.uid;
        store()["size"] = components.sizeElement.value;
        sendEvent('uploaded');
        disableElement(components.filePickerElement);
    }
});

onEvent("constructionDone", () => {
    //components.filePickerElement.value = "";
    //components.sizeElement.value = "";
});