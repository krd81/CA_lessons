import { Router } from "express"
import { EntryModel } from '../db.js'

const router = Router()

// GET all entries
router.get('/', async (req, res) => res.send(await EntryModel.find().populate('category')))

// GET one entry
router.get('/:id', async (req, res) => {
    // const entry = await EntryModel.findOne({_id: req.params.id})
    const entry = await EntryModel.findById(req.params.id).populate('category')
    if (entry) {
        res.send(entry)
    } else {
        res.status(404).send({error: "Entry not found"})
    }
})


// POST ROUTE
router.post('/', async (req, res) => {
    try {
        const insertedEntry = await (await EntryModel.create(req.body)).populate('category')
        res.status(201).send(insertedEntry)
    }
    catch (err) {
        res.status(500).send({ error: err.message })
    }
})



// UPDATE route
router.put('/:id', async (req, res) => {
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
router.delete('/:id', async (req, res) => {
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

export default router