$("#request").submit(function() {
	    var oData = {
	        'name': $('#request').find('[name="name"]').val(),
	        'phone': $('#request').find('[name="phone"]').val(),
	        'email': $('#request').find('[name="email"]').val(),
	        'date': $('#request').find('[name="date"]').val(),
	        'time': $('#request').find('[name="time"]').val(),
	        'message': $('#request').find('[name="message"]').val()

	    };

	    oData = $('#request').serialize();

	    $.ajax({
            type: 'POST',
            url: '/',
            dataType: 'html',
            data: oData,

	    })


		return false;
	});

