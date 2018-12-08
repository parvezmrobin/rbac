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