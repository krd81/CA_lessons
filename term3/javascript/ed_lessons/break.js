function breakWhenPrivate(array) {
    for (let item of array){
        if(item === "PRIVATE"){
            break
        } else {
            console.log(item)
        }
    }
  }


  breakWhenPrivate(["cat", "dog", "PRIVATE", "fish", "elephant"])