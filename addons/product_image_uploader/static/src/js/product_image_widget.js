odoo.define('product_image_uploader.imageWidget', function (require) {
    'use strict';

    const ajax = require('web.ajax');

    $(document).ready(function () {
        $('#upload_button').on('click', function () {
            const fileInput = $('#custom_image')[0];
            if (fileInput.files.length === 0) {
                alert('Per favore, seleziona un file.');
                return;
            }

            const file = fileInput.files[0];
            const formData = new FormData();
            formData.append('custom_image', file);

            ajax.post('/upload_image', formData, {
                processData: false,
                contentType: false,
            }).then(function (response) {
                alert('Immagine caricata con successo!');
            }).catch(function () {
                alert('Errore nel caricamento dell\'immagine.');
            });
        });
    });
});
