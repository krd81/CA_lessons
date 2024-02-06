import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./Home"
import NavBar from "./NavBar"
import Article from "./Article"
import ShowArticles from "./ShowArticles"
import { useEffect, useState } from "react"



function App() {
  const [articles, setArticles] = useState([])

  // Get articles from the API
  useEffect(() => {
    fetch('https://api.slingacademy.com/v1/sample-data/blog-posts')
    .then(res => res.json())
    .then(data => setArticles(data))
  }, [])


  function allArticles (id, title, content_text, user_id, photo_url, category) {
    const newArticle = {
      id: id,
      title: title,
      content_text: content_text,
      user_id: user_id,
      photo_url: photo_url,
      category: category
    }
    setArticles([...articles, newArticle])
  }

  return (
    <>
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/articles' element={<ShowArticles articles={articles} />} />
      {/* <Route path='/' element={''} />
      <Route path='/' element={''} /> */}
      <Route path='*' element={<h3>Page not found</h3>}/>
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
