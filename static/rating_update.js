$(document).ready(function(){
	$(".rate-btn").click(function(e){
	//$("input[name='rating']").click(function(e){
		e.preventDefault();
		var this_ = $(this);
		var rateUrl = this_.attr("data-href");
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
