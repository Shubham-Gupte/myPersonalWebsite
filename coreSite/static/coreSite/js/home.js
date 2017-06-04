$(window).load(function(){

    setTimeout(
  function()
  {
    $('#cover').fadeOut(800);
  }, 800);
});
$(document).ready(function(){
  $('#abovePic').hide();
  //Insert changing text
  var text = ["Web-Developer", "Student", "Tech-Enthusiast"];
   var counter = 0;
   var elem = document.getElementById("abovePic");
   setInterval(change, 3000);
   function change() {
    elem.innerHTML = text[counter];
    $('#abovePic').fadeIn(1000).delay(1000);
    $('#abovePic').fadeOut(1000);
       counter++;
       if(counter >= text.length) { counter = 0; }
   }
   var counterTwo=0;
   $('mobileButton').click(function(){
     counterTwo++;
     if (counterTwo==1) {
       //change background
       $('#homeNav').css('background-color',gray);
     } else {
       //change to transparent
       $('#homeNav').css('background-color',transparent);
       counterTwo=0;
     }
   });
});
