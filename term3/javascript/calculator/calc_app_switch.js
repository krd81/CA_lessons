import express from 'express'

const app = express()
app.use(express.json())

app.get('/', (request, response) => {
    response.send({"message": "Test"})
})

app.put('/:num1/:operation/:num2', (request, response) => {
    
    let num1 = Number.parseInt(request.params.num1)
    let num2 = request.params.num2
    
    response.json({
        "num1": request.params.num1,
        "num2": request.params.num2,
        "operation": request.params.operation,
        "num1 type": typeof num1,
        "num2 type": typeof num2
    })

})

app.get('/:num1/:operation/:num2', async (request, response) => {
    let num1 = request.params.num1
    let num2 = request.params.num2
    let operation = request.params.operation

    // if (typeof num1 === Number && typeof num2 === Number){
    // try{
        num1 = Number.parseInt(num1)
        num2 = Number.parseInt(num2)
    // } catch (err) {
    //     response.status(400).send({"error": "Calculator operations can only be applied to integers"})
    // }

    let result = 25
    // response.status(200).send({"operation": `${num1} add ${num2}`}, {"result": result})
    // result = add(num1, num2)
    // response.status(200).send({"number": num1 , "result": result})

    switch (operation) {        
        case add:
            myPromise = new Promise ((resolve) => {
                resolve(add(num1, num2))})
            result = await myPromise
            response.status(200).send({"operation": "add", "result": result})
        break

        case subtract:
            result = subtract(num1, num2)
            response.status(200).send({"operation": `${num1} minus ${num2}`}, {"result": result})

        break

        case multiply:
            result = multiply(num1, num2)
            response.status(200).send({"operation": `${num1} multiplied by ${num2}`}, {"result": result})

        break

        case divide:
            result = divide(num1, num2)
            response.status(200).send({"operation": `${num1} divided by ${num2}`}, {"result": result})

        break

        default:
            response.status(404)
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
