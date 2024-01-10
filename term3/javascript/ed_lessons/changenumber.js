function changeNumber(number) {
    if (number % 2 === 0) {
      return number;
    } else {
      return number + 1;
    }
  }

  function kelly(number){
    console.log(number,` becommes...`)
    number = (number % 2 === 0 ? number : number +1)
    console.log(number)
    console.log("")
  }

//   changeNumber(2)
//   changeNumber(5)
//   changeNumber(-3)

kelly(2)
kelly(5)
kelly(-3)