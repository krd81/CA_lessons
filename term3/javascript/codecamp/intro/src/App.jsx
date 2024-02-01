import React, { useState } from 'react'
import './App.css'
import ToDoItem from './ToDoItem'
import todosData from './todosData'


function App() {
  let [todos, setToDos] = useState(todosData)
  let todoItems = todos.map(item => <ToDoItem key={item.id} item={item}/>)
  
  // let [checked, setChecked] = useState(false)

  // function changeItemStatus(id) {
  //   for (let item of todoItems){
  //     if (item.id === id) {
  //       item.completed = !item.completed
  //       return item
  //     }
  //   }
  // }
  
  
  return (    
    <div className="todo-list">
      {todoItems}
    </div>
 
  )
}




export default App

