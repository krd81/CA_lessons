import React from 'react'

function colourCalc(temp) {
    let r = 0
    let g = 0
    let b = 0
    let diff = 0
    let factor = 0
    console.log(temp)
    console.log(typeof temp)

    switch (temp) {
        case temp>45:
            console.log({r: 255, g: 0, b: 0})
            return {r: 255, g: 0, b: 0}
            break;
        case temp>35:
            diff = temp-35
            factor = Math.round(Math.abs((diff / 10) - 1))
            g = 255 * factor
            console.log({r: 255, g: g, b: 0})
            return {r: 255, g: g, b: 0}
            break
        case temp>25:
            diff = temp-25
            factor = Math.round(diff / 10)
            r = 255 * factor
            console.log({r: r, g: 255, b: 0})
            return {r: r, g: 255, b: 0}
            break;
        case temp>15:
            diff = temp-15
            factor = Math.round(Math.abs((diff / 10) - 1))
            b = 255 * factor
            console.log({r: 0, g: 255, b: b})
            return {r: 0, g: 255, b: b}
            break;
        case temp>-15:
            diff = temp+15
            factor = Math.round(diff / 30)
            g = 255 * factor
            console.log({r: 0, g: g, b: 255})
            return {r: 0, g: g, b: 255}
            break;
        default:
            factor = Math.abs(Math.abs(temp)/100 - 1)
            b = 255 * factor
            console.log({r: 0, g: 0, b: b})
            return {r: 0, g: 0, b: b}
        } 

}

export default colourCalc