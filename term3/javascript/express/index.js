import express from 'express'

// Create an instance of Express
const app = express();

// Configure settings to allow data to be sent into the server
app.use(express.json());
// app.use(express.urlencoded({extended: true}));

// Set up any data needed to give to the server later
const port = 3000;

// Tell the server:
// - configure the server instance to respond to an additional route
// - the route will be a HTTP GET request on the homepage of the server (eg. localhost:3000/ ) 
app.get('/', (request, response) => {
    // The response object manages all things regarding what gets returned to the client.
    // In this case, we tell the response to send a message in HTML to the client.
    response.send('Welcome to this empty website! Feel free to take a look around...');
});


app.put('/repeater', (request, response) => {
    let word = request.body.string
    let n = Number(request.body.repeat)
    let repeatedWord = word.repeat(n)

    console.log(repeatedWord)
    response.status(200).send({"response": repeatedWord})
})


// MESSAGE CONTROLLER
app.get('/message', (request, response) => {
    response.status(200).send({"response": "List of messages"})
})

app.post('/message', (request, response) => {
    response.status(201).send({"response": "Message created"})
})

app.put('/message', (request, response) => {
    response.status(200).send({"response": "Message updated"})
})

app.delete('/message', (request, response) => {
    response.status(200).send({"response": "Message deleted"})
})




// Once the server has been configured, tell it to start listening to web traffic.
app.listen(port, () => {
    // This logged message will appear in the terminal, not the browser.
    console.log(`ExpressJS Challenge app listening on port ${port}`);
});