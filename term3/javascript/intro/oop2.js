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

const rect = new Rectangle(10, 20)
console.log(rect.area)
console.log(rect.width)
