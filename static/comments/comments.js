$(document).ready(function(){
	commentUrl = $(".comment-form").attr("data-api");
	commentReplyUrl = $(".comment-reply-form").attr("data-reply-api")
	
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
	/*$(".comment-reply-form").ajaxForm({
		url: commentReplyUrl, 
		type: "post",
		success: function(data){
			console.log($(this).attr("data-reply-api"))
			$( ".comment-container" ).load(window.location.href + " .comment-container" );
			$(".comment-reply-form").clearForm();
		}
	});*/
	//This is necessary to do the form reply.
	$(function () {
		$('form').on('submit', function (e) {
			$.ajax ({
				type: 'post',
				url: $(this).attr("data-reply-api"),
				data: $(this).serialize(),
				success: function () {
					$( ".comment-container" ).load(window.location.href + " .comment-container" );
					$(".comment-form").clearForm();
				}
			});
			e.preventDefault();
		});
	});
})




