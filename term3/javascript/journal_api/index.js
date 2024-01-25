import express from 'express'
import { CategoryModel } from './db.js'
import entryRoutes from "./routes/entry_routes.js"


const app = express()

// This is middleware that performs the action of checking each incoming object
// If the header type is application/json and there is content in the body(??)
// It will parse the body into JSON format
// Use allows us to use middelware
app.use(express.json())

app.get('/', (request, response) => response.send({info: "Journal API - info"}))
app.get('/categories', async (req, res) => res.send(await CategoryModel.find()))


app.use('/entries', entryRoutes)

app.listen(4001)

