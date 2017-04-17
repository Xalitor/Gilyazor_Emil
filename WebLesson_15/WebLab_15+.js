function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	var g = canvas.createLinearGradient(10, 10, 2000, 2000);
	g.addColorStop(0, "purple");
	g.addColorStop(.5, "gray");
	g.addColorStop(1, "yellow");
	canvas.strokeStyle = "purple";
	canvas.fillStyle = g;
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
	canvas.fill();
	
	


}

window.addEventListener("load", shapes, false);