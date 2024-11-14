document.getElementById('newsForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir que el formulario se envíe de la forma tradicional
    
    // Recoger los datos del formulario
    const title = document.getElementById('title').value;
    const date = document.getElementById('date').value;
    const author = document.getElementById('author').value;
    const category = document.getElementById('category').value;
    const content = document.getElementById('content').value;
    const tags = document.getElementById('tags').value.split(',');

    // Crear un objeto con la información
    const newsData = {
        title: title,
        date: date,
        author: author || 'No especificado',
        category: category || 'No especificado',
        content: content,
        tags: tags
    };

    // Convertir el objeto a JSON
    const jsonData = JSON.stringify(newsData, null, 4);

    // Crear un archivo Blob con el JSON
    const blob = new Blob([jsonData], { type: 'application/json' });
    const url = URL.createObjectURL(blob);

    // Mostrar la sección de descarga y proporcionar el enlace al archivo
    const downloadSection = document.getElementById('downloadSection');
    downloadSection.classList.remove('hidden');

    const downloadButton = document.getElementById('downloadButton');
    downloadButton.addEventListener('click', function() {
        const a = document.createElement('a');
        a.href = url;
        a.download = `${title} + ${date}.json`;
        a.click();
    });
});
