// function Greeting ({ name='None', age=21}) << Destructure in situ and pass to constructor
function Greeting(props) {
  // Destructure JS object
  const { name="None", age=25, abc=18 } = props
    return (
      <>
        <p>FR: Bonjour, {name}!</p>
        <p>ES: Hola {abc}!</p>
      </>
    )
  }

  export default Greeting