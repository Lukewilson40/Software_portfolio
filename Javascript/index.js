document.addEventListener('DOMContentLoaded', () => {
	const taskForm = document.getElementById('task-form');
	const taskList = document.getElementById('task-list');

	// Load tasks from localStorage
	loadTasks();

	// Add Task
	taskForm.addEventListener('submit', (event) => {
		event.preventDefault();
		const title = document.getElementById('task-title').value;
		const deadline = document.getElementById('task-deadline').value;
		const task = { id: Date.now(), title, deadline, completed: false };
		saveTask(task);
		addTaskToDOM(task);
		taskForm.reset();
	});

	// Mark as Completed or Delete
	taskList.addEventListener('click', (event) => {
		const taskId = event.target.closest('.task-item').dataset.id;
		if (event.target.classList.contains('complete-btn')) {
			toggleTaskStatus(taskId);
		} else if (event.target.classList.contains('delete-btn')) {
			deleteTask(taskId);
		}
	});
});

function loadTasks() {
	const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
	tasks.forEach(addTaskToDOM);
}

function saveTask(task) {
	const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
	tasks.push(task);
	localStorage.setItem('tasks', JSON.stringify(tasks));
}

function addTaskToDOM(task) {
	const taskItem = document.createElement('li');
	taskItem.classList.add('task-item');
	taskItem.dataset.id = task.id;
	taskItem.innerHTML = `
       <span>${task.title} - ${task.deadline}</span>
       <button class="complete-btn">${
			task.completed ? 'Undo' : 'Complete'
		}</button>
       <button class="delete-btn">Delete</button>
    `;
	document.getElementById('task-list').appendChild(taskItem);
}

function toggleTaskStatus(id) {
	const tasks = JSON.parse(localStorage.getItem('tasks'));
	const task = tasks.find((t) => t.id == id);
	task.completed = !task.completed;
	localStorage.setItem('tasks', JSON.stringify(tasks));
	document.getElementById('task-list').innerHTML = '';
	loadTasks();
}

function deleteTask(id) {
	let tasks = JSON.parse(localStorage.getItem('tasks'));
	tasks = tasks.filter((task) => task.id != id);
	localStorage.setItem('tasks', JSON.stringify(tasks));
	document.getElementById('task-list').innerHTML = '';
	loadTasks();
}

function filterTasks(status) {
	const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
	const filteredTasks = tasks.filter((task) =>
		status === 'all'
			? true
			: status === 'completed'
			? task.completed
			: !task.completed
	);
	document.getElementById('task-list').innerHTML = '';
	filteredTasks.forEach(addTaskToDOM);
}
