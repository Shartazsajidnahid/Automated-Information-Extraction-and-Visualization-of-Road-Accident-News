import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL; // Access the environment variable
  
  useEffect(() => {
    axios.get(`${apiBaseUrl}/tasks/`).then((response) => {
      setTasks(response.data);
    });
  }, [apiBaseUrl]); // Include apiBaseUrl as a dependency

  const handleAddTask = () => {
    axios.post(`${apiBaseUrl}/tasks/`, { task: newTask }).then((response) => {
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
