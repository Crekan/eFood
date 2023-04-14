import React, { useState, useEffect } from 'react';
import axios from 'axios';

function BookList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/books/')
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



// function PostList() {
//   const [tasks, setTasks] = useState([]);
//
//   useEffect(() => {
//     axios.get('http://127.0.0.1:8000/api/v1/books/')
//       .then(response => {
//         setTasks(response.data);
//       })
//       .catch(error => {
//         console.error(error);
//       });
//   }, []);
//
//   return (
//     <div>
//       <h1>Posts</h1>
//       <ul>
//         {tasks.map(task => (
//           <li key={task.id}>{task.title}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }
//
// export default PostList;
