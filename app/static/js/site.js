String.prototype.capitalize = function () {
    return this.charAt(0).toUpperCase() + this.slice(1);
};

$(document).ready(function () {
    if (typeof nav !== 'undefined') $('#' + nav).addClass('active');
});