import { EntryModel, CategoryModel, closeConnection } from "./db.js"



const categories = [
    {name: 'Food'}, 
    {name: 'Gaming'}, 
    {name: 'Coding'}, 
    {name: 'Other'}
]



await EntryModel.deleteMany()
await CategoryModel.deleteMany()
console.log("Deleted categories & entries")
// await EntryModel.insertMany(entries)
const cats = await CategoryModel.insertMany(categories)
console.log("Added categories & entries")

console.log(categories)
console.log(cats)

const entries = [
    {category: cats[0], content: 'Pizza is yummy!'},
    {category: cats[2], content: 'Coding is fun!'},
    {category: cats[1], content: 'Skyrim is for the Nords'}
]

await EntryModel.insertMany(entries)


closeConnection()

// process.send('SIGTERM')
// process.kill(process.pid, 'SIGINT')