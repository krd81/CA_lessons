function fetchJoke(){
    // Default method is "GET"
    fetch("https://icanhazdadjoke.com/", {
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => console.log(data))
}

fetchJoke()
