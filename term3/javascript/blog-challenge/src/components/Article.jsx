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

const Article = ({ title, content_text, photo_url, user_id, category, created_at }) => {
    const logos = []
    const date = new Date(created_at)


    function addLogo () {
        // for (let i=1; i<13; i++){
            // let file = `"../assets/${i}.png"`
            let file = "../assets/1.png"

            logos.push(file)
        // }
    }


    function randomNumber (max) {
        const rand = Math.floor(Math.random() * max)
        return rand
    }

    function textPreview () {
        const newString = content_text
        const contentArray = newString.split(" ")
        const previewArray = []

        let i = 0
        let max = Math.min(50, contentArray.length)

        for (let word of contentArray) {
            if (i < max) {
                previewArray.push(word)
            }
            i++
        }
        const tempString_1 = previewArray.toString()
        // @ts-ignore
        const tempString_2 = tempString_1.replaceAll(",", " ")
        return tempString_2
    }

  return (
    <>
    {addLogo()}
    <div className="card">
        <div className="card-image">
            <figure className="image is-4by3">
                <img src={photo_url} alt="Placeholder image" />
            </figure>
        </div>
        <div className="card-content">
            <div className="media">
                {/* <div className="media-left"> */}
                    {/* <figure className="image is-48x48"> */}
                        {/* <img src={logos[randomNumber(12)]} alt="Placeholder image" /> */}
                        {/* <img src="blog-challenge/src/components/12.png" alt="...Placeholder image" /> */}
                    {/* </figure> */}
                {/* </div> */}
                <div className="media-content">
                    <p className="title is-4">{title}</p>
                    <p className="subtitle is-6">User: {user_id}</p>
                    <p className="subtitle is-7">{category}</p>
                </div>
            </div>

            <div className="content">
                <p>{textPreview()}</p>
                 {/* <a>@bulmaio</a>. */}
                <a href="#">#css</a> <a href="#">#responsive</a>
                <br />
                <time dateTime="2016-1-1">{`${date.getDate()}-${date.getMonth()+1}-${date.getFullYear()}`}</time>
            </div>
        </div>
    </div>
    </>
  )
}

export default Article