import { useState } from 'react'
import CategorySelection from './CategorySelection'
import Home from './Home'
import NewEntry from './NewEntry'
import NavBar from './Navbar'
import { BrowserRouter, Routes, Route } from "react-router-dom"
// import '../index.css'

const App = () => {
  return(
    <>
    <BrowserRouter>
    <NavBar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/category' element={<CategorySelection />}/>
        <Route path='/entry'>
          <Route path='new/:cat_id' element={<NewEntry />}/>
        </Route>
        <Route path='*' element={<h3>Page not found</h3>}/>
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
