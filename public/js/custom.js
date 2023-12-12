(function ($) {

  "use strict";

    // PRE LOADER
    $(window).load(function(){
      $('.preloader').fadeOut(1000); // set duration in brackets    
    });


    // MENU
    $('.menu-burger').on('click', function() {
      $('.menu-bg, .menu-items, .menu-burger').toggleClass('fs');
      $('.menu-burger').text() == "☰" ? $('.menu-burger').text('✕') : $('.menu-burger').text('☰');
    });


    // ABOUT SLIDER
    $('body').vegas({
        slides: [
            { src: 'images/pexels-ethan-brooke-3142005.jpg' },
            { src: 'images/pexels-naufal-shidqi-12061667.jpg' },
            { src: 'images/korea-1095361_1920.jpg' },
            // { src: 'images/pexels-pixabay-52547.jpg' },
            // { src: 'images/kgb.jpg' },
            // { src: 'images/nhss.jpg' },
            // { src: 'images/롯데타워.png' },
        ],
        timer: false,
        transition: [ 'zoomOut', ]
    });

})(jQuery);
