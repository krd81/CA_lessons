function Person(name, age, location) {
    this.name = name
    this.age = age
    this.location = location
}

Person.prototype.sayHello = function() {
    console.log(`Hi, my name is ${this.name}`)
}

function Student(name, age, location, studentId) {
    Person.call(this, name, age, location)
    this.studentId = studentId
}
Student.prototype = Object.create(Person.prototype);

Student.prototype.study = function() {
    console.log("I'm learning more every day!")
}

function Educator(name, age, location, wage) {
    Person.call(this, name, age, location)
    this.wage = wage
}

Educator.prototype = Object.create(Person.prototype);

Educator.prototype.work = function() {
    console.log("I have the best job in the world!")
}
