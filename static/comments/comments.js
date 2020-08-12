$(document).ready(function(){
	commentUrl = $(".comment-form").attr("data-api");
	
	$(".comment-form").ajaxForm({
		url: commentUrl, 
		type: "post",
		success: function(data){
			$( ".comment-container" ).load(window.location.href + " .comment-container" );
			$(".comment-form").clearForm();
		}
	});

})




