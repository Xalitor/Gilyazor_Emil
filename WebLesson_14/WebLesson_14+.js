function validate() {
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	var y = document.forms.input.password.value;
	//we need... username@webaddress.extension
	//if, the following...
		//@ is not in the string
		//@ is in the wrong place
		//there is no .com, .gov, or any other extension
		//final dot is in the wrong place
	
	
	if(atPos < 1 || dotPos < atPos+2 || dotPos+2 > x.length)
		alert("This is not a valid email address!");
	else if(6 > y.length)
		alert("Your password is so short!")
	else if(6 > y.length || atPos < 1 || dotPos < atPos+2 || dotPos+2 > x.length)
		alert("Both username and password are incorrect!")
	else
		alert("Success!")
}