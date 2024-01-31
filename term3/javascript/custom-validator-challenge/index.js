const express = require('express');
// Create the server instance.
const app = express();
// Configure the server instance to receive JSON data.
app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use((error, request, response, next) => {
    response.json({
        errors: request.body.errors
    })
})

app.use((request, response, next) => {
    request.body.errors = null

    
})

const baseURL = "https://pokeapi.co/api/v2/pokemon/";

// localhost:3000
app.post('/', async (request, response) => {

    // If this fetch request returns JSON, then we want to store it as an object that we can work with.
    let result = await fetch(baseURL + request.body.pokemonName).then((data) => {return data.json()});

    if (result){
        response.json({
            pokedexNumber: result.id,
            name: result.name
        });
    } else {

    }
});


// Activate the server at port 3000.
app.listen(3000, () => {
    console.log("Server running!");
});