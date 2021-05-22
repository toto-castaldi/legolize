const resizingCallbacks = [];
const appElement = document.getElementById("app");
let appW = appElement.clientWidth;
let appH = appElement.clientHeight;

const removeClass = (element, clazzName) => {
    element.classList.remove(clazzName);
}

const setWidth = (element, w) => {
    element.style.width = Math.ceil(w) + "px";
}

const setHeight = (element, h) => {
    element.style.height = Math.ceil(h) + "px";
}

const center = (element, currentW, currentH) => {
    element.style.left = Math.ceil(appW / 2 - currentW / 2) + "px";
    element.style.top = Math.ceil(appH / 2 - currentH / 2) + "px";
}

const show = (element) => {
    removeClass(element, "hidden");
}

const onWindowResize = (f) => resizingCallbacks.push(f);

const minAppDimension = () => Math.min(appW, appH);

onWindowResize(() => {
    appW = appElement.clientWidth;
    appH = appElement.clientHeight;
});

window.onresize = () => {
    for (const f of resizingCallbacks) {
        f();
    }
}

export { show, setHeight, setWidth, center, onWindowResize, minAppDimension }