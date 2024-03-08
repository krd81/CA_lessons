// @ts-ignore
import { useEffect, useReducer } from 'react'
import CategorySelection from './CategorySelection'
import Home from './Home'
import NewEntry from './NewEntry'
import NavBar from './Navbar'
import { BrowserRouter, Routes, Route, useParams } from "react-router-dom"
import ShowEntry from './ShowEntry'
import reducer, { journalContext } from '../reducer'

const App = () => {
  // const [categories, setCategories] = useState([])
  // const [entries, setEntries] = useState([])

  // dispatch is a function that takes an action and sends it to the reducer
  // it essentially calls the reducer
  const [state, dispatch] = useReducer(reducer, { categories: [], entries: [] })
  const { categories, entries } = state // Desctructure categories from state, so code can refer to categories

  useEffect (() => {
    fetch('http://localhost:4001/categories')
    .then(res => res.json())
    // .then(data => console.log(data))
    // .then(data => setCategories(data))
    .then((data) => 
    // @ts-ignore
    dispatch({
      type: "set categories",
      data: data,
    })
    )

    fetch('http://localhost:4001/entries')
    .then(res => res.json())
    // .then(data => console.log(data))
    // .then(data => setEntries(data))
    // @ts-ignore
    .then(data => dispatch({
      type: 'set entries',
      data: data
    }))

    // dispatch({
    //   type: 'set categories',
    //   data: ['Food', 'Other']
    // })

    }, [])

  // Params relates to the URL
  // const params = useParams()

  async function addEntry(cat_id, content) {
    const newId = entries.length
    // 1. Create entry object from user input
    const newEntry = {
      category: categories[cat_id],
      content: content
    }
    // POST new entry to API
    const res = await fetch('http://localhost:4001/entries', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newEntry)
    })
    const data = await res.json()
    // .then(res => res.json())
    // .then(data => setEntries([...entries, data]))
    // setEntries([...entries, data])
    // @ts-ignore
    dispatch({
      type: 'add entry',
      data: [data]
    })


    // 2. Add new entry to the entries list
    // Now being done in useEffect above
    // setEntries([...entries, newEntry])
    // 3. Return id of newly created element
    return newId

  }


  // Higher Order Component (HOC)
  function ShowEntryWrapper() {
    const {id} = useParams()
    return <ShowEntry entry={entries[id]} />
  }


  return(
    <journalContext.Provider value={state}>
    <BrowserRouter>
    <NavBar />
      <Routes >
        <Route path='/' element={<Home entries={entries}/>} />
        {/* <Route path='/category' element={<CategorySelection categories={categories}/>}/> */}
        <Route path='/category' element={<CategorySelection />}/>
        <Route path='/entry'>
        <Route path=':id' element={<ShowEntryWrapper />} />
          <Route path='new/:cat_id' element={<NewEntry addEntry={addEntry}/>}/>
        </Route>
        <Route path='*' element={<h3>Page not found</h3>}/>
      </Routes>
    </BrowserRouter>
    </journalContext.Provider>
  )
}

export default App
