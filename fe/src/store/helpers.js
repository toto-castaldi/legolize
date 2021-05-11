let serverUrl = "";

export const setUrl = (url) => {
    serverUrl = url + (url.endsWith('/') ? '' : '/');
}

export const apiInputImage = (uid) => `${serverUrl}input/${uid}`;

export const apiOutpuImage = (uid) => `${serverUrl}output/${uid}`;

export const get = async(url) => {
    const res = await fetch(`${serverUrl}${url}`, {
        method: 'GET'
    })
    return res;
};

export const post = async(url, { body }) => {
    const res = await fetch(`${serverUrl}${url}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
    });

    return res;
}

export const postFormData = async(url, { formData }) => {
    return await fetch(`${serverUrl}${url}`, {
        method: 'POST',
        body: formData
    });
}

export const put = async(url, { body }) => {
    const res = await fetch(`${serverUrl}${url}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
    });

    return res;
}

export const del = async(url) => {
    const res = await fetch(`${serverUrl}${url}`, {
        method: 'DELETE'
    });

    return res;
}