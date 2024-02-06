import { useState } from 'react'
import CategorySelection from './CategorySelection'
import Home from './Home'
import NewEntry from './NewEntry'
import NavBar from './Navbar'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import ShowEntry from './ShowEntry'
import { useParams } from "react-router-dom"
// import '../index.css'

const App = () => {
  const [categories] = useState(['Food', 'Gaming', 'Coding', 'Social', 'School', 'Other'])
  const [entries, setEntries] = useState([{category: 0, content: 'I like pizza!'}])
  // Params relates to the URL
  // const params = useParams()



  function addEntry(cat_id, content) {
    const newEntry = {
      category: cat_id,
      content: content
    }
    // 2. Add new entry to the entries list
    setEntries([...entries, newEntry])
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
      <Routes>
        <Route path='/' element={<Home />} />
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
