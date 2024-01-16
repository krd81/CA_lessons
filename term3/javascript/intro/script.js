let str = "Hello, World!"

console.log(str.length)
console.log(str.indexOf("lo"))
console.log(str.slice(8 ,-1))
console.log(str.replace("Hello", "Goodbye"))
console.log(str.replaceAll("o", "---"))

console.log(`Hello, ${str}!`)
console.log(`Answer: ${5 * 10}`)

let x = 5
console.log(x++)
console.log(++x)

console.log(x)
console.log(typeof x)

let person = {'name' : 'matt'}
let key = "name"
console.log(person.name)

array = [1, 2, 3, 3.14159, true, "Hello"]
console.log(array);

/*
function add(x, y) {
    return x + y
}
*/

const add = (x, y) => x + y
const square = x => x ** 2

console.log(add(10, 34))
console.log(square(10))

const numbers = [12, 50, 44, 32, 2]

const result = numbers.map(square)
console.log(result)

const double = numbers.map(x => x * 2)
console.log(double)

const utils = {
    add: (x, y) => x + y,
    double: x => x * 2,
    square: x => x ** 2
}

const people = ["Matt", "John", "Mary", "Kate"]
const [first, second, ...others] = people

console.log(first, second, others)

const bobBirds = ["Robin", "Crow"]
const sallyBirds = ["Bluejay", "Cadinal"]

const allBirds1 = bobBirds.concat(sallyBirds)
const allBirds2 = [...bobBirds, ...sallyBirds]


console.log(allBirds1)
console.log(allBirds2)
console.log(bobBirds)
console.log(sallyBirds)
