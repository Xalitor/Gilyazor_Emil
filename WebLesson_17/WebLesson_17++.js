function drag() 
{
	mantis = document.getElementById("fish");
	leftbox = document.getElementById("leftBox")
	
	mantis.addEventListener("dragstart", startDrag, false);
	mantis.addEventListener("dragend", endDrag, false);
	
	leftBox.addEventListener("dragenter", dragEnter, false);
	leftBox.addEventListener("dragleave", dragLeave, false);
	leftBox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftBox.addEventListener("drop", drop, false);
	
}

function startDrag(e) {
	var pic = '<img id = "fish" src = "https://s-media-cache-ak0.pinimg.com/736x/25/7e/da/257edab7e8e88e0cfc56c78207b44054.jpg">';
	e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "#80657A";
	leftbox.style.border = "3px solid green";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "white";
	leftbox.style.border = "3px solid purple";
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
	pic = e.target ;
	pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);