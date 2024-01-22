import express from 'express'

const categories = ['Food', 'Gaming', 'Coding', 'Other']
const entries = [
    {category: 'Food', content: 'Pizza is yummy!'},
    {category: 'Coding', content: 'Coding is fun!'},
    {category: 'Gaming', content: 'Skyrim is for the Nords'}
]

const app = express()

// This is middleware that performs the action of checking each incoming object
// If the header type is application/json and there is content in the body(??)
// It will parse the body into JSON format
app.use(express.json())

app.get('/', (request, response) => response.send({info: "Journal API - info"}))
app.get('/categories', (req, res) => res.send(categories))
app.get('/entries', (req, res) => res.send(entries))

app.get('/entries/:id', (req, res) => {
    const entry = entries[req.params.id - 1]
    if (entry) {
        res.send(entry)
    } else {
        res.status(404).send({error: "Entry not found"})
    }


})

app.post('/entries', (req, res) => {
    // Get entry data from the request
    console.log(req.body)
    // Validate
    // Create a new entry object
    // Push the new entry to the array
    entries.push(req.body)
    // Respond with 201 and the created entry
    res.status(201).send(entries[entries.length-1])
})

app.listen(4001)

