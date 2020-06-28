
$(function () {
    function after_form_submitted(data) {
        if (data.status == 201) {
            $('form#feedback_form').hide();
            $('#success_message').show();
            $('#error_message').hide();
        }
        else {
            $('#success_message').hide();
            $('#error_message').show();

            $('button[type="button"]', $form).each(function () {
                $btn = $(this);
                label = $btn.prop('orig_label');
                if (label) {
                    $btn.prop('type', 'submit');
                    $btn.text(label);
                    $btn.prop('orig_label', '');
                }
            });

        }
    }

    $('#feedback_form').submit(function (e) {
        e.preventDefault();

        $form = $(this);
        unindexed_array = $form.serializeArray();
        indexed_array = {};

        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });

        indexed_array.reference = 'h2o';

        //show some response on the button
        $('button[type="submit"]', $form).each(function () {
            $btn = $(this);
            $btn.prop('type', 'button');
            $btn.prop('orig_label', $btn.text());
            $btn.text('Sending ...');
        });

        $.ajax({
            type: "POST",
            url: '/feedback',
            data: JSON.stringify(indexed_array),
            processData: false,
            success: after_form_submitted,
            error: after_form_submitted,
            contentType: 'application/json',
            dataType: 'json'
        });

    });

    $('#close_button').click(function (e) {
        $('#success_message').hide();
        $('#error_message').hide();
        document.getElementById("feedback_form").reset();
        document.getElementById("feedback_form").style.display = null;
        $('button[type="button"]', $form).each(function () {
            $btn = $(this);
            label = $btn.prop('orig_label');
            if (label) {
                $btn.prop('type', 'submit');
                $btn.text(label);
                $btn.prop('orig_label', '');
            }
        });
    });
});
