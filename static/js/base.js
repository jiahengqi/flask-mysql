$(function(){
	$('#btn_login').click(function(){
		
		$.ajax({
			url: '/login_request',
			data: $('form').serialize(),
			type: 'GET',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
	$('#btn_signup').click(function(){
		
		$.ajax({
			url: '/signup_request',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
	$('#btn_newpwd').click(function(){
		
		$.ajax({
			url: '/newpwd_request',
			data: $('form').serialize(),
			type: 'PUT',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
	$('#btn_delete').click(function(){
		
		$.ajax({
			url: '/delete_request',
			data: $('form').serialize(),
			type: 'DELETE',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
