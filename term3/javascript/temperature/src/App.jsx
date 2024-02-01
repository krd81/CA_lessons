import { useState } from 'react'
import colourCalc from './colourCalc'
import './App.css'

function App() {
  let [temp, setTemp] = useState(0)
  let [colPage, setColPage] = useState('rgb(0,0,0)')
  let [colFont, setColFont] = useState('rgb(255,255,0)')
  
  // let rgb = colourCalc(temp)
  // `rgb(${rgb.r},${rgb.g},${rgb.b})`

  function changeColour() {
    // Sets the temp to be a number 0-100
    temp = Math.floor(Math.random() * 100)
    setTemp(temp)
    // Calls the colourCalc method which generates r,g,b values for background & font
    let col = colourCalc(temp)
    setColPage(`rgb(${col.r1},${col.g1},${col.b1})`)
    setColFont(`rgb(${col.r2},${col.g2},${col.b2})`)

  }

  
  return (
    // Returns the page render with the styling options
    <body style={{"backgroundColor" : colPage, "color": colFont}}> 
    <h1>Temperature Colours...</h1>
    <h3>{temp}<a style={{"fontVariantPosition": "super"}}>o</a>C</h3>
    {/* Button onClick method calls the changeColour function which obtains the new colours
    and updates the state
    */}
    <button onClick={changeColour}>Click here!</button>
    </body>
    
  )
}


export default App
