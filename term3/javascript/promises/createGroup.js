
const fs = require('fs');

// For testing in terminal
const testFile = "students.txt"
const emptyFile = "empty.txt"

// We're giving you this one - but make sure you understand what is happening in this function
function getData(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (error, data) => {
            if (error) {
              // reject(error.message)
              reject(new Error("Error reading file"))
            }
            resolve(data);
        })
    })
}

getData("students.txt")
.then(console.log("File opened"))
.catch(error => console.log(error))

// Given the string `data`, return an array of names
function createList(data) {
    return data.split("\n").filter((val) => val.length > 0)
}

function createGroup(list,size) {
    /*
      If the list is empty and size > 0, throw an Error with the message:
      "List is empty. Cannot great a group of size " + size

      If size is more than array.length, throw an Error with the message:
      "Group too large. Size limited to " + list.length

      If size and list are valid, return a array of size with random values from list
    */

    return new Promise ((resolve, reject) => {
      let newArray = []
      if (list.length === 0 && size > 0){
        reject(new Error(`List is empty. Cannot great a group of size ${size}`))
      } else if (size > list.length){
        reject(new Error(`Group too large. Size limited to ${list.length}`))
      } else {
        for (let i=0; i<size; i++){          
          let addElement = false
          
          while (addElement == false) {
            let listElement = Math.floor(Math.random() * list.length)
            if (!newArray.includes(list[listElement])){
              newArray.push(list[listElement])
              addElement = true
            }
          }
        }
        resolve(newArray)
      }        
  })
}

list = ['Laura', 'Michelle', 'Hannah', 'Gemma', 'Louise', 'Katherine', 'Sarah']
list2 = []

// createGroup(list, 5)
//   .then(result => console.log(result))
//   .catch(error => console.log(error))



function getStudentList(file, size) {
    /*
      Use calls to getData, createList, and createGroup to return a Promise from this function that either resolves
      to the list of students, or rejects with the correct error message.

      Hint: Using promise chaining to make the implementation simpler
    */
      return getData(file)
        .then((data) => createList(data))
        .then((newArray) => createGroup(newArray, size))
        .then((newArray) => console.log(newArray))
        .catch((error) => console.log(error))
}

getStudentList(testFile, 2)
getStudentList(emptyFile, 2)
getStudentList(testFile, 50)

// For testing in terminal
// getStudentList(testFile, 2).then((list) => console.log(list))  // should print an array with 2 names
// getStudentList(emptyFile, 2).then((data) => console.log(data)).catch((error) => console.log(error)) // should print List is empty error
// getStudentList(testFile, 50).then((data) => console.log(data)).catch((error) => console.log(error)) // should print Group too large error


module.exports = {getData, getStudentList}
