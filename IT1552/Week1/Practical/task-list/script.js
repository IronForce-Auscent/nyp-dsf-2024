// constants declared for input button and task list areas
const taskInput = document.querySelector(".newtask input");
const taskSection = document.querySelector(".tasks");

// listener for the Enter key. Used to add a new task
taskInput.addEventListener("keyup", (e) => {
    if (e.key == "Enter") {
        createTask();
    }
});

// the onclick event for the "Add" button
document.querySelector("#push").onclick = function () {
    createTask();
}

function createTask() {
    if (taskInput.value.trim() === "") {
        alert("The task field is blank. Enter a task name and try again");
    }
    else {
        // create new task elements
        const taskDiv = document.createElement("div");
        taskDiv.classList.add("task");

        const taskLabel = document.createElement("label");
        const taskCheckbox = document.createElement("input");
        taskCheckbox.type = "checkbox";
        taskCheckbox.onclick = function () {
            updateTask(taskCheckbox);
        }
        const taskName = document.createElement("p");
        taskName.textContent = taskInput.value;

        const deleteIcon = document.createElement("div");
        deleteIcon.classList.add("delete");
        deleteIcon.innerHTML = '<i class="uil uil-trash"></i>';
        deleteIcon.onclick = function () {
            taskDiv.remove();
        }

        taskLabel.appendChild(taskCheckbox);
        taskLabel.appendChild(taskName);
        taskDiv.appendChild(taskLabel);
        taskDiv.appendChild(deleteIcon);

        taskSection.appendChild(taskDiv);

        taskSection.offsetHeight >= 300 ? taskSection.classList.add("overflow") : taskSection.classList.remove("overflow");

        taskInput.value = ""; // clear the input field after adding the task
    }
}

function updateTask(task) {
    let taskItem = task.parentElement.lastElementChild;
    if (task.checked) {
        taskItem.classList.add("checked");
    }
    else {
        taskItem.classList.remove("checked");
    }
}
