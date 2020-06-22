$(document).ready(function(){
	
  $(window).scroll(function() {   
    var height = $(window).scrollTop();
    if(height  > 50) {
        $("body").addClass('sticky')
    } else{
        $("body").removeClass('sticky');
    }
  });

  //--nav-toggle
  $('.navbar-toggler').on('click', function(){
    $('body').toggleClass('nav-open');
  });
  //---nav-active
	// $(".navbar-nav > li > a").on('click', function(){
	// 	$(this).parent('li').addClass('active').siblings().removeClass('active');
	// });

  //top-slider

  $('.top_slider.owl-carousel').owlCarousel({
      loop:true,
      nav:true,
      dots:false,
      items:1,
      // animateOut: 'fadeOut',
      autoplay:true,
      mouseDrag:false,
      smartSpeed:1000
  });
   var owl = $('.top_slider.owl-carousel');
  function setAnimation ( _elem, _InOut ) {
    var animationEndEvent = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';

    _elem.each ( function () {
      var $elem = $(this);
      var $animationType = 'animated ' + $elem.data( 'animation-' + _InOut );

      $elem.addClass($animationType).one(animationEndEvent, function () {
        $elem.removeClass($animationType); // remove animate.css Class at the end of the animations
      });
    });
  }
  // Fired before current slide change
  owl.on('change.owl.carousel', function(event) {
      var $currentItem = $('.owl-item', owl).eq(event.item.index);
      var $elemsToanim = $currentItem.find("[data-animation-out]");
      setAnimation ($elemsToanim, 'out');
  });
  // Fired after current slide has been changed
  owl.on('changed.owl.carousel', function(event) {
      var $currentItem = $('.owl-item', owl).eq(event.item.index);
      var $elemsToanim = $currentItem.find("[data-animation-in]");
      setAnimation ($elemsToanim, 'in');
  });
  
  //----aos------
  AOS.init({
    duration:1000,
  });

});