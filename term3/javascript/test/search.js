let songList = ["Despacito", "Summer Of 69", "Hotel California", "Single Ladies", "If I were a boy", "Run the World", "Waka Waka" ]
let searchText = "hotel"
let newSongList = []

for (let song of songList){
  if (song.toLocaleLowerCase().includes(searchText.toLocaleLowerCase())) { 
      newSongList.push(song)
  }
}
console.log(searchText)
console.log(newSongList)


