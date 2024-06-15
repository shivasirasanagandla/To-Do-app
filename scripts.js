document.addEventListener('DOMContentLoaded', () => {
    const addButton = document.getElementById('add-todo-button');
    const modal = document.getElementById('todo-modal');
    const closeButton = document.querySelector('.close-button');

    addButton.addEventListener('click', () => {
        modal.style.display = 'block';
    });

    closeButton.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });

    const form = document.getElementById('todo-form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        const todo = {
            title: formData.get('title'),
            description: formData.get('description'),
            time: formData.get('time')
        };
        
        // Add image if pro user
        const imageInput = document.getElementById('image');
        if (imageInput.files.length > 0) {
            todo.image = imageInput.files[0];
        }

        try {
            const response = await fetch('/graphql', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    query: `
                        mutation {
                            createTodo(title: "${todo.title}", description: "${todo.description}", time: "${todo.time}", user_id: "${sessionStorage.getItem('user_id')}") {
                                id
                                title
                                description
                                time
                            }
                        }
                    `
                })
            });
            const result = await response.json();
            if (result.errors) {
                console.error(result.errors);
            } else {
                modal.style.display = 'none';
                window.location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
