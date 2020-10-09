$(document).ready(function(){
	commentUrl = $(".comment-form").attr("data-api");
	//commentReplyUrl = $(".comment-reply-form").attr("data-api")
	
	$(".comment-form").ajaxForm({
		url: commentUrl, 
		type: "post",
		success: function(data){
			console.log(commentUrl)
			$( ".comment-container" ).load(window.location.href + " .comment-container" );
			$(".comment-form").clearForm();
		}
	});

	//NEED TO REFERENCE REPLY FORMS WITH IDS!!!!
	$("[id^=form-reply-]").ajaxForm({
		url: $("[id^=form-reply-]").attr("data-api"), 
		type: "post",
		success: function(data){
			console.log($(this).closest("form").attr("data-api"))
			$( ".comment-container" ).load(window.location.href + " .comment-container" );
			$("[id^=form-reply-]").clearForm();
		}
	});
})




