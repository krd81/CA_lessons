const fs = require('fs'); 
//  /Users/Kelly/projects/term3/javascript/async/names.txt
//  async/names.txt
function checkList(name, callback) {
    fs.readFile('names.txt', 'utf8', (error, data) => callback(error, data, name))
}

function findName(error, data, name) {
    let found = false
    if (error){
        return console.log("Error reading file")
    } else {        
        if (data.includes(name)) {
            found = true
        }
        if (found === true) {
            return console.log(`${name} is in the list`)
        } else {
                return console.log(`${name} is not in the list`)
        }
    }
}

/* The tests for this challenge pass in names to test.
 You can get arguments passed in to node using the process.argv object.
 The line below removes the first two elements of the process.argv array.
 The first two elements are the full path to node and the full path to the JS file.
 Anything we pass as an argument will be additional elements in process.argv.
 Try console logging process.argv to get a better understanding of how this works.
*/
const names = process.argv.slice(2)
// loop through each name passed as an argument and call checkList
names.forEach((name) => {
    checkList(name, findName)
})



// Once you implement findName, you can test this yourself from terminal:
// node findName.js alex
// or pass multiple names (this is what clicking 'Run' will do):
// node findName.js alex micheal pikachu
