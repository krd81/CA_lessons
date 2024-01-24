import { EntryModel, CategoryModel, closeConnection } from "./db.js"

const entries = [
    {category: 'Food', content: 'Pizza is yummy!'},
    {category: 'Coding', content: 'Coding is fun!'},
    {category: 'Gaming', content: 'Skyrim is for the Nords'}
]

const categories = [
    {name: 'Food'}, 
    {name: 'Gaming'}, 
    {name: 'Coding'}, 
    {name: 'Other'}
]

await EntryModel.deleteMany()
await CategoryModel.deleteMany()
console.log("Deleted categories & entries")
await EntryModel.insertMany(entries)
await CategoryModel.insertMany(categories)
console.log("Added categories & entries")

closeConnection()

// process.send('SIGTERM')
// process.kill(process.pid, 'SIGINT')