import { useState } from 'react'
import tempCalc from './tempCalc'
import colourCalc from './colourCalc'


import './App.css'

function App() {
  let [temp, setTemp] = useState(0)
  temp = 42.2
  let rgb = colourCalc(temp)
  // `rgb(${rgb.r},${rgb.g},${rgb.b})`
   let backgroundColour = {
      backgroundColor: `rgb(${rgb.r},${rgb.g},${rgb.b})`
  }

  return (
  
    <body style={backgroundColour}> 
    <h1>Temperature Colours...</h1>
    <h3>{temp}<a style={{"fontVariantPosition": "super"}}>o</a>C</h3>
    <button onClick={''}>Click here!</button>
    </body>
    
  )
}
App()

export default App
