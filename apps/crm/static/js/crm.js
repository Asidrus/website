$(document).ready(function() {
    $('#crm').submit(function() { // On form submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                $('#success_div').html(response.message); // update the DIV
            },
            error: function(e, x, r) { // on error..
                $('#error_div').html(e); // update the DIV
            }
        });
        return false;
    });
});