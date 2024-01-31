import React, { useState } from 'react'
import './App.css'
import ToDoItem from './ToDoItem'
import todosData from './todosData'


function App() {
  let [todos, setToDos] = useState(todosData)
  const todoItems = todos.map(item => <ToDoItem key={item.id} item={item}/>)
  return (    
    <div className="todo-list">
      {todoItems}
    </div>
 
  )
}




export default App
