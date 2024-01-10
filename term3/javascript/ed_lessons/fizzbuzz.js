function fizzBuzz(start, end) {
    for (let i = start; i <= end; i++){
        if(i % 15 === 0){
            console.log(`"fizzbuzz" - number: ${i}`)
            return true            
        } else if (i % 3 === 0){
            console.log(`"fizz" - number: ${i}`)
            continue
        } else if (i % 5 === 0) {
            console.log(`"buzz" - number: ${i}`)
            continue
        } else {
            console.log(i)
            continue
        }
    }
    console.log("None")
    return false
    
}

fizzBuzz(1,10)