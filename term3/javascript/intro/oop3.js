class Rectangle {
    #width
    #height
    constructor(width, height){
        this.#width = width
        this.#height = height
    }
    set width (value) {
        if (typeof value === 'number'){
            this.#width = value
        }else {
            // Exception
        }        

    }
    get width () {return this.#width}

    get area() {
        return this.#width * this.#height
    }
}


class Square extends Rectangle{    
    #width
    #height
    constructor(size=5){
        super(size, size)
        this.#width = size
        this.#height = size
    }
}

const square = new Square(10)
console.log(square.area)
console.log(square.width)