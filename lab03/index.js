// show랑 hide이용해서 해보기.
$(document).ready(function(){

	$("#textbox1").click(function(){
		if($("#musicli").css("display")!="none"){
			$("#musicli").hide();
		}
		else{
			$("#musicli").show();
		}
	});

	$("#textbox2").click(function(){
		if($("#movieli").css("display")!="none"){
			$("#movieli").hide();
		}
		else{
			$("#movieli").show();
		}
	});

	$("#textbox3").click(function(){
		if($("#sportsli").css("display")!="none"){
			$("#sportsli").hide();
		}
		else{
			$("#sportsli").show();
		}
	});

	$("#input").keyup(function(event) {
		if (event.keyCode === 13) {
			alert("hey");

		}
	});
})