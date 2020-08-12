$(document).ready(function(){
	commentUrl = $(".route-comment-form").attr("data-api");
	
	$(".route-comment-form").ajaxForm({
		url: commentUrl, 
		type: "post",
		success: function(data){
			$( ".comment-container" ).load(window.location.href + " .comment-container" );
			$(".route-comment-form").clearForm();
		}
	});

})

$(document).ready(function(){
	commentUrl = $(".crag-comment-form").attr("data-api");
	
	$(".crag-comment-form").ajaxForm({
		url: commentUrl, 
		type: "post",
		success: function(data){
			$( ".comment-container" ).load(window.location.href + " .comment-container" );
			$(".crag-comment-form").clearForm();
		}
	});

})



