function drag() {
	mantis = document.getElementById("fish");
	leftbox = document.getElementById("leftBox")
	
	mantis.addEventListener("dragstart", startDrag, false);
	
	leftBox.addEventListener("dragenter", function(e){e.preventDefault()}, false);
	leftBox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftBox.addEventListener("drop", drop, false);
	
}

function startDrag(e) {
	var pic = '<img id = "fish" src = "https://s-media-cache-ak0.pinimg.com/736x/25/7e/da/257edab7e8e88e0cfc56c78207b44054.jpg">';
	e.dataTransfer.setData('Picture', pic);
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

window.addEventListener("load", drag, false);