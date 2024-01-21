/**
 * @jest-environment jsdom
 */
const indexFile = require("./indexFile.js")
const eventFire = require("./eventFire.js")
const {
    challengeOne,
    challengeTwo,
    challengeThree
} = require("/home/script.js")

document.body.innerHTML = indexFile()

describe("challenge-one - ", () => {
    challengeOne()
    let counterOne = document.getElementById('counter-one')
    test("+5 should increment by 5", () => {
        counterOne.innerText = 0
        eventFire(five, 'click')
        expect(counterOne.innerText).toEqual(5)
    })
    test("+10 should increment by 10", () => {
        counterOne.innerText = 0
        eventFire(ten, 'click')
        expect(counterOne.innerText).toEqual(10)
    })
    test("+15 should increment by 15", () => {
        counterOne.innerText = 0
        eventFire(fifteen, 'click')
        expect(counterOne.innerText).toEqual(15)
    })
    test("all three work together", () => {
        counterOne.innerText = 0
        eventFire(five, 'click')
        eventFire(ten, 'click')
        eventFire(fifteen, 'click')
        expect(counterOne.innerText).toEqual(30)
    })
})



describe('challenge-two', () => {
    challengeTwo()
    let counterTwo = document.getElementById("counter-two")
    let [increment, decrement, stop] = counterTwo.parentElement.children
    test('increment by one with each click', () => {
        counterTwo.innerText = 0
        eventFire(increment, 'click')
        expect(counterTwo.innerText).toEqual(1)
        eventFire(increment, 'click')
        expect(counterTwo.innerText).toEqual(2)
        eventFire(increment, 'click')
        expect(counterTwo.innerText).toEqual(3)
    })

    test('decrement by one with each click', () => {
        counterTwo.innerText = 0
        eventFire(decrement, 'click')
        expect(counterTwo.innerText).toEqual(-1)
        eventFire(decrement, 'click')
        expect(counterTwo.innerText).toEqual(-2)
        eventFire(decrement, 'click')
        expect(counterTwo.innerText).toEqual(-3)
    })
    test("clicking stop stops the buttons", () => {
        counterTwo.innerText = 0
        eventFire(stop, 'click')
        eventFire(increment, 'click')
        eventFire(increment, 'click')
        eventFire(decrement, 'click')
        eventFire(decrement, 'click')
        expect(counterTwo.innerText).toEqual(0)
    })
})
