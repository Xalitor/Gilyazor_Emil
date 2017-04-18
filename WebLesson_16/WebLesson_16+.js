function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	var pic = new Image();
	pic.src = "http://thedesigninspiration.com/wp-content/uploads/2010/05/animals/006.jpg";
	
	pic.addEventListener("load", function() {canvas.drawImage(pic, 0, 0, 200, 200);}, false);

}

window.addEventListener("load", text, false);