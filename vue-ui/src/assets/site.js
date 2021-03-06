import axios from "axios";


const origin = 'http://localhost:5000';

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

    let token;
    if (typeof Storage === 'undefined') {
        token = getCookie('token')
    } else {
        token = localStorage.getItem('token');
        if (token === null) {
            token = sessionStorage.getItem('token');
        }

    }

    if (token === null) {
        openUrl('/auth/login');
        return;
    } else {
        window.access_token = token;
    }

    window.request = axios.create({
        baseURL: origin + '/api/v1/',
        headers: {
            Authorization: 'JWT ' + token
        }
    })
})();

const mixin = {
    data: function () {
        return {
            user: null,
        }
    },
    methods: {
        logout: function () {
            document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            localStorage.removeItem('token');
            sessionStorage.removeItem('token');

            openUrl('/auth/login')
        }
    },
    mounted() {
        if (typeof window.request !== "undefined") {
            window.request.get('auth/user').then(r => {
                this.user = r.data;
            })
        }
    }
};

export {mixin, openUrl, getCookie};
