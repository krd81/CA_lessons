function enoughWater(cups) {
    if (cups > 7 && cups < 11){
        console.log(cups, `cups is 'true'`)
      return true
    }
    else{
        console.log(cups, `cups is 'false'`)
      return false
    }
  }


  
//   module.exports = enoughWater;
  
  enoughWater(0)
  enoughWater(10)
  enoughWater(12)