$(document).ready(function(){
	$("#star5").click(function(e){
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
				//$(".rating").hide();
				//$(".user-rating").show();

				//$("#avg_score").html(data);

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
			}, error: function(error){
				console.log(error);
				console.log("error");
			}
		});

	});
});
//data.liked