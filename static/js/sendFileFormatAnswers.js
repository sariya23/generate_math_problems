document.addEventListener('DOMContentLoaded', function() {
    var dataForm = document.getElementById('get_answers_form');

    dataForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = {
            fileFormat: document.getElementById('file_format_answer_select').value,
        };
        fetch('/get_answers', {
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
            var a = document.createElement('a');
            a.href = jsonData.path;
            console.log(jsonData.path)
            a.download = 'answers.tex'
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        })
        .catch(function(error) {
            console.log('Error:', error);
        });
    });
});
