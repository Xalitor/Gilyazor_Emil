function drag() 
{
	mantis = document.getElementById("shark");
	leftbox = document.getElementById("leftBox")
	
	mantis.addEventListener("dragstart", startDrag, false);
	mantis.addEventListener("dragend", endDrag, false);
	
	leftBox.addEventListener("dragenter", dragEnter, false);
	leftBox.addEventListener("dragleave", dragLeave, false);
	leftBox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftBox.addEventListener("drop", drop, false);
	
}

function startDrag(e) {
	var pic = '<img id = "shark" src = "https://s-media-cache-ak0.pinimg.com/736x/0d/e8/25/0de82521eed9d665827126e50f6a3949.jpg">';
	e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "orange";
	leftbox.style.border = "3px solid yellow";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "brown";
	leftbox.style.border = "3px solid black";
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