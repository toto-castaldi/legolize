const elementId = (pos) => `${pos.x}-${pos.y}`;

const start = (data) => {
    let scale = 1;

    //load thumbnail
    document.getElementById("thmbnail-img").src = data.thmbnailSrc;

    //elements
    for (palettePoint of data.renderedInfo.points) {
        const element = document.createElement("div");
        element.id = elementId(palettePoint.pos);
        render.appendChild(element);

        element.classList.add(`element`, `palette-${palettePoint.colorId}`);
    }

    //update elements size and position
    const draw = () => {
        const render = document.getElementById("render");
        const renderW = render.clientWidth;
        const renderH = render.clientHeight;
        const minRenderLen = (renderW > renderH ? renderH : renderW) * 0.9 * scale;
        const maxRenderElement = data.renderedInfo.w > data.renderedInfo.h ? data.renderedInfo.w : data.renderedInfo.h;
        const elementLen = minRenderLen / maxRenderElement;
        const centerX = renderW / 2;
        const centerY = renderH / 2;
        const startX = centerX - (data.renderedInfo.w / 2) * elementLen;
        const startY = centerY - (data.renderedInfo.h / 2) * elementLen;
        for (palettePoint of data.renderedInfo.points) {
            const element = document.getElementById(elementId(palettePoint.pos));
            const palettePointX = palettePoint.pos.x;
            const palettePointY = palettePoint.pos.y;

            element.style.width = Math.ceil(elementLen) + "px";
            element.style.height = Math.ceil(elementLen) + "px";
            element.style.left = Math.ceil(startX + palettePointX * elementLen) + "px";
            element.style.top = Math.ceil(startY + palettePointY * elementLen) + "px";
        }
    }

    //zoom
    const zoom = (event) => {
        event.preventDefault();



        if (event.deltaY > 0) {
            scale += 0.1;
        } else {
            scale -= 0.1;
        }

        //scale += event.deltaY * -0.01;

        scale = Math.min(Math.max(.125, scale), 4);

        draw();
    }

    const el = document.getElementById("app");
    el.onwheel = zoom;


    window.onresize = () => {
        scale = 1;
        draw();
    }

    draw();
}

fetch('data/demo-palette-points.json')
    .then(response => response.json())
    .then(data => start({
        thmbnailSrc: "images/demo-thumbnail.png",
        renderedInfo: data
    }));