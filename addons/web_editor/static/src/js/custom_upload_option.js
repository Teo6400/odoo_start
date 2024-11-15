odoo.define('web_editor.custom_upload_option', function (require) {
    'use strict';
    
    var options = require('web_editor.snippets.options');

    options.Class.include({
        onBuilt: function () {
            this._super.apply(this, arguments);
            var $btn = this.$target.find('.o_upload_image_button');
            if ($btn.length) {
                $btn.on('click', this._onUploadImage.bind(this));
            }
        },

        _onUploadImage: function () {
            var self = this;
            var fileInput = $('<input/>', {
                type: 'file',
                accept: 'image/*'
            });
            
            fileInput.click();
            fileInput.on('change', function (e) {
                var file = e.target.files[0];
                if (file) {
                    self._uploadImage(file);
                }
            });
        },

        _uploadImage: function (file) {
            // Funzione di caricamento dell'immagine
            console.log('Caricamento immagine:', file);
            // Puoi aggiungere il codice per il caricamento dell'immagine su un server qui.
        }
    });
});