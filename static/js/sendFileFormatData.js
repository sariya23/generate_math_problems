document.addEventListener('DOMContentLoaded', function() {
    var dataForm = document.getElementById('file_format_form');

    dataForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = {
            fileFormat: document.getElementById('fileFormatSelect').value,
        };

        fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(function(response) {
            console.log(response)
        })
        .catch(function(error) {
            console.log(`error: ${error}`)
        });
    });
});