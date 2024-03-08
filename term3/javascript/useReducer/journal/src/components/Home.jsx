import { useContext } from 'react'
import { Link } from 'react-router-dom'
import { journalContext } from '../reducer'




const Home = ({ entries=[] }) => {
  const state = useContext(journalContext)
  console.log(state)

  return (
    <>
      <h3>Journal Entries</h3>
        <ul>
            {state.entries.map((entry, index) => (
              <li key={index}>
                <Link to={`/entry/${index}`}>{entry.content}</Link>
              </li>
              ))}
        </ul>
    </>
  )
}

export default Home