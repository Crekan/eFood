import React, { useState, useEffect } from 'react';
import axios from 'axios';

function BookList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000')
      .then(response => {
        setTasks(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Books:</h1>
      <ul>
        {tasks.map(book => (
          <li key={book.id}>
            <h2>{book.name}</h2>
            <p>{book.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;