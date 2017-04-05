function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.strokeStyle = "yellow";
	canvas.fillStyle = "purple";
	canvas.beginPath();
	canvas.moveTo(50, 50);
	canvas.lineTo(70, 250);
	canvas.lineTo(300,200);
	canvas.closePath();
	canvas.stroke();
	canvas.fill();
}

window.addEventListener("load", shapes, false);