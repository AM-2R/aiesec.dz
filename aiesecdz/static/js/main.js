$(window).on('scroll', navScroll);
$(document.body).on('touchmove', navScroll);

function navScroll() {
    if ($(document).scrollTop() !== 0) {
        $('#topnav').removeClass('faded');
        $('#topnav').addClass('unfaded');
    } else {
        $('#topnav').removeClass('unfaded');
        $('#topnav').addClass('faded');
    }
}