let count = 3

while (count > 0){
    console.log(count--)
}

for (let i = 0; i < 10; i++) {
    console.log(i)
}

const favFoods = ["pizza", "pasta", "tacos"]


// If you don't need the index, for of is best
for (let item of favFoods) {
    console.log(item)
}

// For each is the better option
for (let index in favFoods) {
    console.log(`${parseInt(index)+1}. ${favFoods[index]}`)
}

// If you need index and element, use a 
favFoods.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})

favFoods.forEach(food => console.log(food))
