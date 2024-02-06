import React from 'react'

/*
Posts contain the following:
"content_text"
"user_id"
"title"
"photo_url"
"created_at"
"id"
"description"
"content_html"
"category"
"updated_at"
*/

const Article = ({ title, content_text, photo_url, user_id, category }) => {
    console.log(title, content_text, photo_url, user_id, category)
  return (
    <>
    <div className="card">
        <div className="card-image">
            <figure className="image is-4by3">
                <img src={photo_url} alt="Placeholder image" />
            </figure>
        </div>
        <div className="card-content">
            <div className="media">
                <div className="media-left">
                    <figure className="image is-48x48">
                        <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image" />
                    </figure>
                </div>
                <div className="media-content">
                    <p className="title is-4">{title}</p>
                    <p className="subtitle is-6">User: {user_id}</p>
                    <p className="subtitle is-7">{category}</p>
                </div>
            </div>

            <div className="content">
                <p>{content_text}</p>
                 {/* <a>@bulmaio</a>. */}
                <a href="#">#css</a> <a href="#">#responsive</a>
                <br />
                <time dateTime="2016-1-1">11:09 PM - 1 Jan 2016</time>
            </div>
        </div>
    </div>
    </>
  )
}

export default Article