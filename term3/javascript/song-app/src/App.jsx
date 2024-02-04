import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  let [songList, setSongList] = useState('')

  songList = ["Despacito", "Summer Of 69", "Hotel California", "Single Ladies", "If I were a boy", "Run the World", "Waka Waka" ]
  let searchText = ''
  let newSongList = []

  function handleClick() {

  }

  function filterSongs(event) {
    searchText = event.target.value
    // displaySongs()
  }

  function displaySongs() {
    for (let song of songList){
      if (song.toLowerCase().includes(searchText.toLowerCase())) { 
          newSongList.push(song)
      }
    }
    console.log(searchText)
    console.log(newSongList)
    setSongList(newSongList)
    // return newSongList
  }




  return (
    <>
      {/* {displaySongs()} */}
     <h1>Search song:</h1>
     <form onSubmit={handleClick}>
        <input type="text" onChange={filterSongs} />
        <input type="submit" value="Filter" />
      </form>
      <ul>
        {newSongList.map(song => (
          <li key={song.id}>{song}</li>
        ))}
      </ul>
    </>
  )
}

export default App


/* 
      {{for (let song of SongList) {
          `<li>hello</li>`
        }
      }}

        <li>{songList[0]}</li>
        {songList[1]}
*/