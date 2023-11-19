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
        .then(function(response) {
            if (response.ok) {
                console.log(response)
                return response.json();
            } else {
                throw new Error('Failed to fetch file information');
            }
        })
        .then(function(jsonData) {
            // Создаем ссылку для скачивания файла
            document.getElementById('get_answers').removeAttribute('disabled')
            var a = document.createElement('a');
            a.href = jsonData.path;
            console.log(jsonData.path)
            a.download = 'integrals.' + jsonData.extension;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        })
        .catch(function(error) {
            console.log('Error:', error);
        });
    });
});
