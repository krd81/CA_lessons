import express from 'express'
import { EntryModel, CategoryModel } from './db.js'


const app = express()

// This is middleware that performs the action of checking each incoming object
// If the header type is application/json and there is content in the body(??)
// It will parse the body into JSON format
app.use(express.json())

app.get('/', (request, response) => response.send({info: "Journal API - info"}))
app.get('/categories', async (req, res) => res.send(await CategoryModel.find()))
app.get('/entries', async (req, res) => res.send(await EntryModel.find()))

app.get('/entries/:id', async (req, res) => {
    // const entry = await EntryModel.findOne({_id: req.params.id})
    const entry = await EntryModel.findById(req.params.id)
    if (entry) {
        res.send(entry)
    } else {
        res.status(404).send({error: "Entry not found"})
    }
})

app.post('/entries', async (req, res) => {
    try{
        // Get entry data from the request
        // console.log(req.body)
        // Validate
        // Create a new entry object
        // Push the new entry to the array
        // entries.push(req.body)
        const insertedEntry = await EntryModel.create(req.body)
        // Respond with 201 and the created entry
        res.status(201).send(insertedEntry)
    }
    catch (err) {
        res.status(500).send({error: err.message})
    }
})

// UPDATE route
app.put('/entries/:id', async (req, res) => {
    try{
        const updatedEntry = await EntryModel.findByIdAndUpdate(req.params.id, req.body, {new : true})
        if(updatedEntry) {
            res.send(updatedEntry)
         } else {
            res.status(404).send({error: 'Entry not found'})
         }
    }
    catch (err) {
        res.status(500).send({error: err.message})
    }
})


// DELETE route
app.delete('/entries/:id', async (req, res) => {
    try{
        const deletedEntry = await EntryModel.findByIdAndDelete(req.params.id)
        if(deletedEntry) {
            res.sendStatus(204)
         } else {
            res.status(404).send({error: 'Entry not found'})
         }
    }
    catch (err) {
        res.status(500).send({error: err.message})
    }
})



app.listen(4001)

