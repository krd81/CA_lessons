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
console.log(array)

function add(x, y) {
    return x + y
}

console.log(add(10, 34))