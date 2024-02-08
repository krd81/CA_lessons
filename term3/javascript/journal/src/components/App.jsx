import { useEffect, useState } from 'react'
import CategorySelection from './CategorySelection'
import Home from './Home'
import NewEntry from './NewEntry'
import NavBar from './Navbar'
import { BrowserRouter, Routes, Route, useParams } from "react-router-dom"
import ShowEntry from './ShowEntry'
// import '../index.css'

const App = () => {
  const [categories, setCategories] = useState([])
  const [entries, setEntries] = useState([])

  useEffect (() => {
    fetch('http://localhost:4001/categories')
    .then(res => res.json())
    // .then(data => console.log(data))
    .then(data => setCategories(data))

    fetch('http://localhost:4001/entries')
    .then(res => res.json())
    // .then(data => console.log(data))
    .then(data => setEntries(data))

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
    setEntries([...entries, data])


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
    <>
    <BrowserRouter>
    <NavBar />
      <Routes >
        <Route path='/' element={<Home entries={entries}/>} />
        <Route path='/category' element={<CategorySelection categories={categories}/>}/>
        <Route path='/entry'>
        <Route path=':id' element={<ShowEntryWrapper />} />
          <Route path='new/:cat_id' element={<NewEntry categories={categories} addEntry={addEntry}/>}/>
        </Route>
        <Route path='*' element={<h3>Page not found</h3>}/>
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
