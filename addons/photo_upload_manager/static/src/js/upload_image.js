document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('photo_upload').addEventListener('change', function (event) {
        let file = event.target.files[0];
        let reader = new FileReader();

        reader.onloadend = function () {
            fetch('/upload/photo', {
                method: 'POST',
                body: JSON.stringify({ image: reader.result, order_id: document.querySelector('input[name="order_id"]').value }),
                headers: { 'Content-Type': 'application/json' }
            });
        };
        reader.readAsDataURL(file);
    });
});
