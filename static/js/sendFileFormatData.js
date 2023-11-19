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
            // Проверяем, что ответ имеет успешный статус
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Получаем объект Blob из ответа
            return response.blob();
        })
        .then(function(blob) {
            // Создаем URL для Blob
            var blobUrl = URL.createObjectURL(blob);

            // Создаем ссылку
            var downloadLink = document.createElement('a');
            downloadLink.href = blobUrl;
            downloadLink.download = 'integrals.tex';  // замените на реальное имя и расширение файла
            document.body.appendChild(downloadLink);

            // Программно вызываем клик по ссылке
            downloadLink.click();

            // Удаляем ссылку из документа
            document.body.removeChild(downloadLink);

            // Освобождаем ресурсы URL
            URL.revokeObjectURL(blobUrl);
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
    });
});
