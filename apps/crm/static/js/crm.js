$(document).ready(function() {
    $('#crm').submit(function() {
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function(response) {
                $('#orders').remove()
                $('#error').remove()
                $('#results').append(response.data)
            },
            error: function(e, x, r) {
                $('#orders').remove()
                $('#error').remove()
                $('#results').append('<div id="error">Ошибка обработчика</div>')
            }
        });
        return false;
    });
});

