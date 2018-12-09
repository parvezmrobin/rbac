String.prototype.capitalize = function () {
    return this.charAt(0).toUpperCase() + this.slice(1);
};

function openUrl(url) {
    const a = document.createElement('a');
    a.href = url;
    a.hidden = true;
    document.body.appendChild(a);
    a.click();
}

$(document).ready(function () {
    if (typeof nav !== 'undefined') $('#' + nav).addClass('active');
});

function getCookie(cname) {
    const name = cname + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return null;
}

(function () {
    if (window.location.pathname.indexOf("auth") !== -1) {
        return;
    }
    if (typeof Storage === 'undefined') {
        window.access_token = getCookie('token')
    } else {
        let token = localStorage.getItem('token');
        if (token === null) {
           token = sessionStorage.getItem('token');
        }
        if (token === null) {
            openUrl('/auth/login')
        } else {
            window.access_token = token;
        }
    }
})();
