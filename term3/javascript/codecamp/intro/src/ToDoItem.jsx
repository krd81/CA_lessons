import React from 'react'
import './App.css'

const ToDoItem = (props) => {
  return (
    <div className="todo-item">
        <input type="checkbox" checked={props.item.completed} onChange={() => console.log("Checkbox ticked!")}/>
        <p>{props.item.text}</p>

    </div>
  )
}

export default ToDoItem