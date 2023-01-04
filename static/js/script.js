$(function($) {
  let url = window.location.href;
  $('.navbar-nav .nav-link').each(function() {
    if (this.href === url) {
      $(this).closest('.nav-item').addClass('active');
    }
  });
});