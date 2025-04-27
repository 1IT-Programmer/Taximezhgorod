// Пример JavaScript-кода для минимальных взаимодействий на стороне клиента
document.addEventListener('DOMContentLoaded', function () {
    console.log("Frontend JavaScript loaded.");
});

// Пример обработки нажатия кнопки выхода ("Logout")
const logoutLink = document.getElementById('logout-link');
if (logoutLink) {
    logoutLink.addEventListener('click', function(event) {
        event.preventDefault(); // Предотвращаем переход по ссылке
        fetch('/logout', {
            method: 'GET',
            credentials: 'include'
        }).then(response => {
            window.location.href = '/'; // Переходим на главную страницу после выхода
        });
    });
}

// Пример обработки результата AJAX-запроса
fetch('/some-api-endpoint', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({key: 'value'})
}).then(response => {
    if (!response.ok) throw Error(response.statusText); // Обрабатываем ошибку
    return response.json();
}).then(data => {
    console.log('Success:', data);
}).catch(error => {
    console.error('Error:', error);
    alert('Ошибка при выполнении запроса.');
});
