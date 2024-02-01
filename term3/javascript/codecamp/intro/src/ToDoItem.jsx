import React, { useState } from 'react'
// import App from '.App.jsx'
import './App.css'

const ToDoItem = (props) => {
    let [checked, setChecked] = useState(props.item.completed)

    function handleChange(event) {
        setChecked(event.target.checked)
        props.item.completed = !props.item.completed
    }

    const completedStyle = {
        backgroundColor : "#cdcdcd",
        // textDecoration: "line-through",
        color: "red",
        // fontFamily: "Ariel",
        // fontStyle: "italic"
    }

  return (
    <div className="todo-item">
        <input 
            type="checkbox" 
            checked={checked} 
            // onChange={() => props.handleChange(props.item.id)}
            onChange={handleChange}/>
        <p style={props.item.completed ? completedStyle: null}>{props.item.text}</p>

    </div>
  )
}

export default ToDoItem