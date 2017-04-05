function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.strokeStyle = "";
	canvas.fillStyle = "";
	canvas.beginPath();
	canvas.moveTo(150, 100);
	canvas.lineTo(60, 100);
	canvas.lineTo(140, 150);
	canvas.lineTo(60, 220);
	canvas.lineTo(150, 190);
	canvas.lineTo(170, 300);
	canvas.lineTo(190, 190);
	canvas.lineTo(280, 220);
	canvas.lineTo(200, 150);
	canvas.lineTo(280, 100);
	canvas.lineTo(190, 100);
	canvas.lineTo(170, -10);
	canvas.closePath();
	canvas.stroke();
	var g = canvas.createLinearGradient(10, 10, 100, 200);
	g.addColorStop(0, "purple");
	g.addColorStop(1, "yellow");
	canvas.fillStyle = g;
}

window.addEventListener("load", shapes, false);