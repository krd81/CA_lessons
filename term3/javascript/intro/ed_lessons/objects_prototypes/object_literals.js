function createObject(){
    let object = {}

    object = {
        name: "David",
        age: "25",
        city: "Los Angeles"
    }

    console.log(object)
}

createObject()

let person = {
    name: "Pauline",
    age: "54",
    country: "France",
    profession: "nurse",
    city: "Toulouse"
}


function badData(obj){
    for (let item in obj){
        if(item !== "name" && item !== "age" && item !== "city"){
            delete obj[item]
            // delete obj.item   << Doesn't work!
        }
    }
    console.log(obj)
}

console.log(person)
badData(person)