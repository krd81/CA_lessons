function Person(name, age, location){
    this.name = name
    this.age = age
    this.location = location
}

function Student(name, age, location, id){
    Person.call(this, name, age, location)
    this.studentID = id
}

function Educator(name, age, location, wage){
    Person.call(this, name, age, location)
    this.wage = wage
}

Person.prototype.sayHello = function(){
    console.log(`Hi, my name is ${this.name}`)
}

Student.prototype = Object.create(Person.prototype)
Educator.prototype = Object.create(Person.prototype)

Student.prototype.study = function(){
    console.log("I'm learning more every day!")
}

Educator.prototype.work = function(){
    console.log("I have the best job in the world!")
}


let student = new Student("Mick", 28, "Sydney", 654)
let educator = new Educator("Larry", 40, "Sydney", 1000000000)

student.sayHello()
educator.sayHello()
student.study()
educator.work()