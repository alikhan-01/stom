$(".js-sent-index-form").click(function() {

	    var oData = {
	        'selectww': $('.js-index-form').find('[name="selectww"]').val(),
	        'name': $('.js-index-form').find('[name="name"]').val(),
	        'phone': $('.js-index-form').find('[name="phone"]').val(),
	        'email': $('.js-index-form').find('[name="email"]').val(),
	        'date': $('.js-index-form').find('[name="date"]').val(),
	        'time': $('.js-index-form').find('[name="time"]').val(),
	        'message': $('.js-index-form').find('[name="message"]').val(),
	        "csrfmiddlewaretoken": $('.js-index-form').find('[name="csrfmiddlewaretoken"]').val()

	    };



	    $.ajax({
            type: 'POST',
            url: '/',
            dataType: 'json',
            data: oData,
            function(){
                alert("Успешно отправлено")ж
            }

	    })


		return false;
	});

