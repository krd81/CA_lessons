function loopOverArray(directions) {
    let result = {}
  
    for (let direction of directions) {

      if (result[direction]) {
        result[direction]++
      } else {
        result[direction] = 1

      }
    }
    console.log(result)
    return result;
  }

  function test(directions){
    let result = []

    for (let direction of directions) {
        if (!result.includes(direction)){
            result.push(direction)
        }        
    }
    console.log(result)

  }

  loopOverArray(["e", "n", "s", "e"])
  loopOverArray(["north", "south", "east", "north", "east", "west", "south", "south"])
  loopOverArray([])