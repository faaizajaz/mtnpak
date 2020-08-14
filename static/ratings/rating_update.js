$(document).ready(function(){
	//If click on any of the individual stars
	$(".indiv-star").click(function(e){
		//set current star
		var this_ = $(this);
		//set rate api url to that of clicked star
		var rateUrl = this_.attr("data-api");
		//do an ajax get request to the apropriate url
		$.ajax({
			type: 'GET',
			url: rateUrl,
			data: {},
			success: function(data){
				//refresh the route rting div only. spaces here are necessary
				$( "#route-rating" ).load(window.location.href + " #route-rating" );
			}, error: function(error){
				console.log(error);
				
			}
		});
	});
});
