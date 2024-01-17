class Dog {
    constructor(name, breed){
        this.name = name
        this.breed = breed
        this.allWalks = []
        this.distanceWalked = 0
    }
    speak() {
        console.log(`Woof! My name is ${this.name}`)
    }

    walk(location, distance){
        let walk = {
            location : location,
            distance : distance
        }
        this.allWalks.push(walk)
        this.distanceWalked += distance
    }

    displayWalks(){
        for (let walk of this.allWalks){
            console.log(`${walk.location}, ${walk.distance}km`)
        }
    }


    totalDistance(){
        // let distance = 0
        // for (let walk in this.allWalks){
        //     distance += walk.distance
        // }
        console.log(`${this.name} has walked ${this.distanceWalked}km`)
    }
}

let dog1 = new Dog("Riley", "Cavalier King Charles Spaniel")
let dog2 = new Dog("Archie", "Cavoodle")

dog1.walk("Centennial Park", 7)
dog2.walk("Sydney Park", 5)
dog2.walk("Barangaroo", 8)

dog1.speak()
dog2.speak()

dog1.displayWalks()
dog2.displayWalks()

dog1.totalDistance()
dog2.totalDistance()
