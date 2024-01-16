/*
function Person(name, age) {
    this.name = name
    this.age = age

    this.greet = () => {
        console.log(`${this.name} is ${this.age} years old`)
    }
}
*/

class Person {
    constructor(name, age) {
        this.name = name
        this.age = age

    }
    greet() {
        console.log(`${this.name} is ${this.age} years old`)
    }
}


var person = new Object ()
// person.name = 'matt'
// person.age = 51

person = new Person("matt", 51)
person.age = 52

console.log(person)
console.log(typeof person)
person.greet()