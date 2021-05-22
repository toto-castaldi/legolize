const resizingCallbacks = [];
const appElement = document.getElementById("app");
let appW = appElement.clientWidth;
let appH = appElement.clientHeight;
let serverUrl = "";
let wsUrl = "";

const removeClass = (element, clazzName) => {
    element.classList.remove(clazzName);
}

const setWidth = (element, w) => {
    element.style.width = Math.ceil(w) + "px";
}

const setHeight = (element, h) => {
    element.style.height = Math.ceil(h) + "px";
}

const getWidth = element => element.style.width.substr(0, element.style.width.length - 2);

const getHeight = element => element.style.height.substr(0, element.style.height.length - 2);

const center = (element, currentW, currentH) => {
    element.style.left = Math.ceil(appW / 2 - currentW / 2) + "px";
    element.style.top = Math.ceil(appH / 2 - currentH / 2) + "px";
}

const show = (element) => {
    removeClass(element, "hidden");
}

const onWindowResize = (f) => resizingCallbacks.push(f);

const minAppDimension = () => Math.min(appW, appH);

const setUrl = (config) => {
    serverUrl = config.api_url + (config.api_url.endsWith('/') ? '' : '/');
    wsUrl = config.ws_url + (config.ws_url.endsWith('/') ? '' : '/');
}

const postFormData = async(url, { formData }) => {
    return await fetch(`${serverUrl}${url}`, {
        method: 'POST',
        body: formData
    });
}

const sendEvent = (name, data) => window.dispatchEvent(new CustomEvent(name, { detail: data }))

const onEvent = (name, f) => window.addEventListener(name, event => f(event.detail))

const apiWaitingImage = (uid) => `${serverUrl}waiting/${uid}`;

onWindowResize(() => {
    appW = appElement.clientWidth;
    appH = appElement.clientHeight;
});

window.onresize = () => {
    for (const f of resizingCallbacks) {
        f();
    }
}

export { apiWaitingImage, show, setHeight, setWidth, center, onWindowResize, minAppDimension, setUrl, postFormData, getWidth, getHeight, sendEvent, onEvent }