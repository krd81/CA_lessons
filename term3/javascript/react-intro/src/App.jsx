import Greeting from './Greeting.jsx'
import './App.css'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
    <h1>Welcome</h1>
    <Greeting foo="bar" name="Matt" age="51"/>
    <Greeting abc={10*5}/>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi aspernatur aperiam at rerum maiores velit officiis inventore vel numquam amet distinctio, hic, quas dolores recusandae repellendus ducimus commodi aliquam sint!</p>
    </>
  
  )
}

export default App
