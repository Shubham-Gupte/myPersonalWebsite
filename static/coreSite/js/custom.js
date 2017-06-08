$(document).ready(function() {
  $('#jsWrapper').hide(0).delay(100).fadeIn(1000);
  $('a').click(function(e) {
    e.preventDefault();
    newLocation = this.href;
    $('body').fadeOut('slow', newpage);
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
