window.addEventListener('load', function () {
	
	     alert("bonjour");
 
        /* initialize the slider based on the Slider's ID attribute */
        $('#rev_slider_1').show().revolution({
 
            /* options are 'auto', 'fullwidth' or 'fullscreen' */
            sliderLayout: 'auto',
 
            /* basic navigation arrows and bullets */
            navigation: {
 
                arrows: {
                    enable: true,
                    style: 'hesperiden',
                    hide_onleave: false
                },
 
                bullets: {
                    enable: true,
                    style: 'hesperiden',
                    hide_onleave: false,
                    h_align: 'center',
                    v_align: 'bottom',
                    h_offset: 0,
                    v_offset: 20,
                    space: 5
                }
            }
        });
    });