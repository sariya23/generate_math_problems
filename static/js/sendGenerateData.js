document.addEventListener('DOMContentLoaded', function() {
    var dataForm = document.getElementById('generate_data_integral_form');

    dataForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = {
            pattern: document.getElementById('dataInput').value,
            constants: document.getElementById('constantsInput').value,
            bounds: document.getElementById('boundsInput').value,
            numExpressions: document.getElementById('numExpressions').value,
            fileFormat: document.getElementById('fileFormatSelect').value,
        };

        fetch('/generate_integrals', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(function(response) {
            document.getElementById('status').textContent = 'Генерация выполнена успешно!';
            console.log(response)
        })
        .catch(function(error) {
            document.getElementById('status').textContent = 'Что-то пошло не так! Проверьте формат данных в форме';
            console.log(`error: ${error}`)
        });
    });
});