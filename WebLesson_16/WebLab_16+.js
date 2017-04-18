function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	

	
	window.addEventListener("mousemove", icon, false);
	pic.addEventListener("load", function() {canvas.drawImage(pic, 0, 0, 200, 200);}, false)
	
}

function icon(e) {
	canvas.clearRect(0, 0, 600, 600);
	var xPos = e.clientX;
	var yPos = e.clientY;
	var pic = new Image();
	pic.src = "http://thedesigninspiration.com/wp-content/uploads/2010/05/animals/006.jpg";
	canvas.fillRect(xPos-50, yPos-50, 100, 100);
	
	
	
}

window.addEventListener("load", mouse, false);