class Car {
    constructor(brand) {
      this.carname = brand;
    }
    present() {
      return 'I have a ' + this.carname;
    }
  }

  class Model extends Car {
    constructor(brand, mod) {
      super(brand);
      this.model = mod;
    }
    show() {
      return this.present() + ', it was made in ' + this.model;
    }
  }

  let makes = ["Ford", "Holden", "Toyota"]
  let models = Array.from(new Array(40), (x,i) => i + 1980)

  function randomIntFromInterval(min,max) { // min and max included
      return Math.floor(Math.random()*(max-min+1)+min);
  }

  for (let model of models) {

    let make = makes[randomIntFromInterval(0,makes.length-1)]
    model = models[randomIntFromInterval(0,models.length-1)]

    let mycar = new Model(make, model);
    console.log(mycar.show())
  }
