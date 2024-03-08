import React from 'react'

const ShowEntry = ({ entry }) => {
  return entry ? (
<>
    <h5>{entry.content}</h5>
    {/* <p>Posted in {categories[entry.category].name}</p> */}
    <p>Posted in {entry.category?.name}</p>
    {console.log(entry)}
    {/* {console.log(categories)} */}
</>
  ) : (
    <h3>Entry not found!</h3>
  )
}

export default ShowEntry
