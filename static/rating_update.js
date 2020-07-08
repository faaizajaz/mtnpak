$(document).ready(function(){
	$(".rating").click(function(e){
	//$("input[name='rating']").click(function(e){
		e.preventDefault();
		var this_ = $(this);
		var rateUrl = this_.attr("data-api");
		console.log(rateUrl)
			$.ajax({
				type: 'GET',
				url: rateUrl,
				data: {},
				success: function(data){
					$("#avg_score").html(data);

				}, error: function(error){
					console.log(error);
					console.log("error");
				}
			});

	});
});
