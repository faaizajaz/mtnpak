$(document).ready(function(){
	$("#star5").click(function(e){
		var this_ = $(this);
		var rateUrl = this_.attr("data-api");
		console.log(rateUrl)
		$.ajax({
			type: 'GET',
			url: rateUrl,
			data: {},
			success: function(data){
				//refresh the route rting div only. spaces here are necessary
				$( "#route-rating" ).load(window.location.href + " #route-rating" );
			}, error: function(error){
				console.log(error);
				console.log("error");
			}
		});

	});
	$("#star4").click(function(e){
	//$("input[name='rating']").click(function(e){
		//e.preventDefault();
		var this_ = $(this);
		var rateUrl = this_.attr("data-api");
		console.log(rateUrl)
		$.ajax({
			type: 'GET',
			url: rateUrl,
			data: {},
			success: function(data){
				//$("#avg_score").html(data);
				//$(".rating").hide();
				//$(".user-rating").show();
				$( "#route-rating" ).load(window.location.href + " #route-rating" );
			}, error: function(error){
				console.log(error);
				console.log("error");
			}
		});

	});
	$("#star3").click(function(e){
	//$("input[name='rating']").click(function(e){
		//e.preventDefault();
		var this_ = $(this);
		var rateUrl = this_.attr("data-api");
		console.log(rateUrl)
		$.ajax({
			type: 'GET',
			url: rateUrl,
			data: {},
			success: function(data){
				//$("#avg_score").html(data);
				//$(".rating").hide();
				//$(".user-rating").show();
				$( "#route-rating" ).load(window.location.href + " #route-rating" );
			}, error: function(error){
				console.log(error);
				console.log("error");
			}
		});

	});
	$("#star2").click(function(e){
	//$("input[name='rating']").click(function(e){
		//e.preventDefault();
		var this_ = $(this);
		var rateUrl = this_.attr("data-api");
		console.log(rateUrl)
		$.ajax({
			type: 'GET',
			url: rateUrl,
			data: {},
			success: function(data){
				//$("#avg_score").html(data);
				//$(".rating").hide();
				//$(".user-rating").show();
				$( "#route-rating" ).load(window.location.href + " #route-rating" );
			}, error: function(error){
				console.log(error);
				console.log("error");
			}
		});

	});
	$("#star1").click(function(e){
	//$("input[name='rating']").click(function(e){
		//e.preventDefault();
		var this_ = $(this);
		var rateUrl = this_.attr("data-api");
		console.log(rateUrl)
		$.ajax({
			type: 'GET',
			url: rateUrl,
			data: {},
			success: function(data){
				//$("#avg_score").html(data);
				//$(".rating").hide();
				//$(".user-rating").show();
				$( "#route-rating" ).load(window.location.href + " #route-rating" );
			}, error: function(error){
				console.log(error);
				console.log("error");
			}
		});

	});


	//$("#user-rating").click(function(){
	//	$("#re-rate").show();
	//});

	//$("#re-rate-link").click(function(){
		//alert("want to re-rate")
		
	//});
});
//data.liked