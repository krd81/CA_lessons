import express from 'express'

const app = express()
app.use(express.json())


app.get('/:num1/:operation/:num2', (request, response) => {
    let num1 = Number.parseInt(request.params.num1)
    let num2 = Number.parseInt(request.params.num2)
    let operation = request.params.operation


    if (Number.isInteger(num1) && Number.isInteger(num2)){
        let result
        if (operation === "add") {
            result = add(num1, num2)
            response.status(200).send({"operation": num1 + " add "+ num2, "result": result})
            
        } else if (operation === "subtract") {
            result = subtract(num1, num2)
            response.status(200).send({"operation": num1 + " minus "+ num2, "result": result})
            
        } else if (request.params.operation === "multiply") {
            result = multiply(num1, num2)
            response.status(200).send({"operation": num1 + " multiplied by "+ num2, "result": result})

        } else if (operation === "divide") {
            result = divide(num1, num2)
            response.status(200).send({"operation": num1 + " divided by "+ num2, "result": result})
            
        } else {
            console.log("Else statement executed")
            response.sendStatus(404)
        }

    } else {
        response.status(400).send({"error": "Calculator operations can only be applied to integers"})
    }

})


function add(num1, num2) {
    return num1 + num2
}

function subtract(num1, num2) {
    return num1 - num2
}

function multiply(num1, num2) {
    return num1 * num2
}

function divide(num1, num2) {
    return num1 / num2
}

app.listen(4001)
