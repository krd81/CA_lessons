class Person{
    constructor(name, age, location){
        this.name = name
        this.age = age
        this.location = location     
    }

    sayHello(){
        console.log(`Hi, my name is ${this.name}`)
    }
}

class Student extends Person{
    constructor(name, age, location, studentID){
        super(name, age, location)
        this.studentID = studentID
    }
    study(){
        console.log("I'm learning more every day!")
    }
}


class Educator extends Person{
    constructor(name, age, location, wage){
        super(name, age, location)
        this.wage = wage
    }
    work(){
        console.log("I have the best job in the world!")
    }
}

let student = new Student("Mick", 28, "Sydney", 654)
let educator = new Educator("Larry", 40, "Sydney", 1000000000)

student.sayHello()
educator.sayHello()
student.study()
educator.work()