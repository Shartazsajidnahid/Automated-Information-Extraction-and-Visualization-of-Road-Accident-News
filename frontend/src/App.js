import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/tasks/").then((response) => {
      setTasks(response.data);
    });
  }, []);

  const handleAddTask = () => {
    axios.post("/tasks/", { task: newTask }).then((response) => {
      setTasks([...tasks, newTask]);
      setNewTask("");
    });
  };

  return (
    <div>
      <h1>To-Do List</h1>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>{task}</li>
        ))}
      </ul>
      <div>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
        />
        <button onClick={handleAddTask}>Add Task</button>
      </div>
    </div>
  );
}

export default App;
