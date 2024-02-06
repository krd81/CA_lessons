import React, {useState}  from 'react'
import { useParams } from "react-router-dom"

const NewEntry = ({ categories, addEntry }) => {
    const params = useParams()
    const [entry, setEntry] = useState('')
    console.log(params)

    function createEntry(e){
        e.preventDefault()
        // 1. Create an entry object from user input
        // App creates the new entry and adds it to the entries array

        addEntry(params.cat_id, entry)
        setEntry('')
    }

  return (
   <>
   <h3>New journal entry in category {categories[params.cat_id]}</h3>
        <form className='section' onSubmit={createEntry}>
            <label className="label">Content</label>
            <div className='control'>
                <textarea className="textarea" value={entry} onChange={e => setEntry(e.target.value)}placeholder="Type your journal entry here"></textarea>
            </div>
            <div className='field is-grouped'>
                <div className='control'>
                    <button className='button is-link'>Create Entry</button>
                </div>
            </div>
        </form>
   </>
  )
}

export default NewEntry