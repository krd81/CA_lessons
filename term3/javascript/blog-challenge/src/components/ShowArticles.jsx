import React from 'react'
import Article from './Article'
import { Link } from 'react-router-dom'

const ShowArticles = ({ articles }) => {
    // console.log(articles)
    const blogs = articles.blogs
  return (
    <>
        <div className="article-post">
        <Link to="/articles">
            <h1 className='article-heading'>ARTICLES</h1>
            {blogs.map(blog => <Article key={blog.id} title={blog.title} content_text={blog.content_text} photo_url={blog.photo_url} user_id={blog.user_id} category={blog.category} created_at={blog.created_at} />)}
            {/* <Article  article={articles.blogs[0].title}/> */}
        </Link>
        </div>
    </>
  )
}

export default ShowArticles