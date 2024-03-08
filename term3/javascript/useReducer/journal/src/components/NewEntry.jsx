import React, {useState, useContext}  from 'react'
import { useNavigate, useParams } from "react-router-dom"
import { journalContext } from '../reducer'

const NewEntry = ({ addEntry }) => {
    const params = useParams()
    const [entry, setEntry] = useState('')
    const nav = useNavigate()
    const state = useContext(journalContext)


    console.log(params)

    async function createEntry(e){
        e.preventDefault()
        // 1. Create an entry object from user input
        // App creates the new entry and adds it to the entries array

        const id = await addEntry(params.cat_id, entry)
        // Clear input textarea
        setEntry('')
        // Redirect the browser to the new entry
        nav(`/entry/${id}`)
    }

  return (
   <>
   <h3>New journal entry in category {state.categories[params.cat_id]?.name}</h3>
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