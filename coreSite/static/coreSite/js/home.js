$(window).load(function () {

	setTimeout(
		function () {
			$('#cover').fadeOut(800);
		}, 800);
});
$(document).ready(function () {
	$('#abovePic').hide();
	$('#abovePic2').hide();
	//Insert changing text
	var text = ["Web-Developer", "Student", "Tech-Enthusiast"];
	var counter = 0;
	var count = 0;
	var elem = document.getElementById("abovePic");
	var elem2 = document.getElementById("abovePic2");
	setInterval(change, 3000);
	setInterval(changeOne, 3000);

	function change() {
		elem.innerHTML = text[counter];
		$('#abovePic').fadeIn(1000).delay(1000);
		$('#abovePic').fadeOut(1000);
		counter++;
		if (counter >= text.length) {
			counter = 0;
		}
	}

	function changeOne() {
		elem2.innerHTML = text[counter];
		$('#abovePic2').fadeIn(1000).delay(1000);
		$('#abovePic2').fadeOut(1000);
		count++;
		if (count >= text.length) {
			count = 0;
		}
	}
	var counterTwo = 0;
	$("#mobileButton").on("click", function () {
		counterTwo++;
		if (counterTwo == 1) {
			//change background
			$('#homeNav').css('background-color', '#00BFFF');
		} else {
			//change to transparent
			$('#homeNav').css('background-color', 'transparent');
			counterTwo = 0;
		}
	});
});
