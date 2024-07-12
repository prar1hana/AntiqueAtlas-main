$(document).ready(function() {
    $(window).scroll(function() {
        $('.revealUp').each(function() {
            var position = $(this).offset().top;
            var windowHeight = $(window).height();
            if (position < $(window).scrollTop() + windowHeight - 200) {
                $(this).addClass('visible'); 
            }
        });
    });
});
