function skipWhenSmall(obj, end) {
    for (let i in obj){
        if(obj[i].length < 3){
            continue
        } else {
            for (let j in obj[i]){
                if(obj[i][j] > end){
                    break
                } else {
                    console.log(obj[i][j])
                }
            }
        }
    }
}


let obj = {
    a: ["1", "2", "3", "4"],
    b: ["5", "6"],
    c: ["7", "8", "9"],
    d: ["10", "11", "9"]
}

skipWhenSmall(obj, 9)