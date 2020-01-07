// show랑 hide이용해서 해보기.
$(document).ready(function(){

	$("#textbox1").click(function(){
		var display =  $("#musicli").css("display");
		if(display!="none"){
			$("#musicli").css({"display": "none"});
		}
		else{
			$("#musicli").css({"display":"block"});
		}
	});

	$("#textbox2").click(function(){
		var display =  $("#movieli").css("display");
		if(display!="none"){
			$("#movieli").css({"display": "none"});
		}
		else{
			$("#movieli").css({"display":"block"});
		}
	});

	$("#textbox3").click(function(){
		var display =  $("#sportsli").css("display");
		if(display!="none"){
			$("#sportsli").css({"display": "none"});
		}
		else{
			$("#sportsli").css({"display":"block"});
		}
	});

	$("#input").keyup(function(event) {
		if (event.keyCode === 13) {
			alert("hey");

		}
	});
})