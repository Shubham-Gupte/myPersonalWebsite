$(document).ready(function() {
  $("#redabout").slideUp(1);
  $("#redabout").delay(100).slideDown(1000);

  $("#blueabout").slideUp(1);
  $("#blueabout").delay(100).slideDown(1000);

  $("#greenabout").slideUp(1);
  $("#greenabout").delay(100).slideDown(1000);
  $('#jsWrapper').hide(0).delay(100).fadeIn(1000);
  $('#resume').click(function(e) {
    e.preventDefault();
    newLocation = this.href;
    $('body').fadeOut('slow', newpage);

  });
  $('a').click(function(e) {
    e.preventDefault();
    newLocation = this.href;
    $('body').fadeOut('slow', newpage);

  });
  $("#mailer").click(function(e){
    location.reload();
      window.location.href = "mailto:shubham@gupte.me";
  });

  function newpage() {
    window.location = newLocation;
  }

  function Reload() {
    try {
      var headElement = document.getElementsByTagName("head")[0];
      if (headElement && headElement.innerHTML)
        headElement.innerHTML += "<meta http-equiv=\"refresh\" content=\"1\">";
    } catch (e) {}
  }

  /*! Reloads on every visit in mobile safari */
  if ((/iphone|ipod|ipad.*os 5/gi).test(navigator.appVersion)) {
    window.onpageshow = function(evt) {
      if (evt.persisted) {
        document.body.style.display = "none";
        location.reload();
      }
    };
  }
});
