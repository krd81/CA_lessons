import mongoose  from 'mongoose'
import dotenv from 'dotenv'

dotenv.config()

try{
    const mConn = await mongoose.connect(process.env.DB_URI)
    console.log(mConn.connection.readyState === 1 ? 'MongoDB connect!' : 'MongoDB failed to connect')
}
catch (err) {
    console.error(err)
}

/*
process.on('SIGTERM', () => mongoose.disconnect())


process.on('SIGINT', () => {
    mongoose.disconnect()
    console.log('Mongoose disconnected')

})*/

const closeConnection = () => {
    console.log('Mongoose disconnecting...')
    mongoose.disconnect()
}

const categoriesSchema = new mongoose.Schema({
    name : {type: String, required: true}
})

const CategoryModel = mongoose.model('Category', categoriesSchema)

const entriesSchema = new mongoose.Schema({
    // category : {type: String, required: true},
    category : {type: mongoose.ObjectId, ref: 'Category'},
    content: {type: String, required: true}
})

const EntryModel = mongoose.model('Entry', entriesSchema)

export {closeConnection, EntryModel, CategoryModel}

/* 
adding process.exit after mongoose.disconnect works for me for disconnecting with ctrl C using SIGINT

process.on('SIGINT', async () => {
    try {
        console.log('Disconnecting...');
        mongoose.disconnect();
        console.log('Disconnected. Exiting process.');
        process.exit(0);
    } catch (err) {
        console.error(err);
        process.exit(1);
    }
});
*/