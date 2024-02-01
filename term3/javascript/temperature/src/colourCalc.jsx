function colourCalc(temp) {
    // 1 colours are for background
    // 2 colours are for font
    let r1 = 0
    let g1 = 0
    let b1 = 0
    let r2 = 0
    let g2 = 0
    let b2 = 0
    let diff = 0
    let factor = 0
    // console.log(temp)
    // console.log(typeof temp)
    // console.log(temp>35 ? "Yes" : "No")

    switch (true) {
        case (temp > 45):
            diff = 100 - temp
            factor = diff / 55
            g1 = Math.round(255 * factor)
            g2 = Math.round(255 * Math.abs(factor-1))
            // return {r: 255, g: 0, b: 0}
            return {r1: 255, g1: g1, b1: 0, r2: 0, g2: g2, b2: 255}
        case (temp > 35):
            diff = temp-35
            factor = Math.abs((diff / 10) - 1)
            g1 = Math.round(255 * factor)
            g2 = Math.round(255 * Math.abs(factor-1))
            // return {r: 255, g: g1, b: 0}
            return {r1: 255, g1: g1, b1: 0, r2: 0, g2: g2, b2: 255}
        case (temp > 25):
            diff = temp-25
            factor = diff / 10
            r1 = Math.round(255 * factor)
            r2 = Math.round(255 * Math.abs(factor-1))
            // return {r: r1, g: 255, b: 0}
            return {r1: r1, g1: 255, b1: 0, r2: r2, g2: 0, b2: 255}
        case (temp > 15):
            diff = temp-15
            factor = Math.abs((diff / 10) - 1)
            b1 = Math.round(255 * factor)
            b2 = Math.round(255 * Math.abs(factor-1))
            // return {r: 0, g: 255, b: b1}
            return {r1: 0, g1: 255, b1: b1, r2: 255, g2: 0, b2: b2}
        case (temp > -15):
            diff = temp+15
            factor = diff / 30
            g1 = Math.round(255 * factor)
            g2 = Math.round(255 * Math.abs(factor-1))
            // return {r: 0, g: g1, b: 255}
            return {r1: 0, g1: g1, b1: 255, r2: 255, g2: g2, b2: 0}
        default:
            factor = Math.abs(Math.abs(temp)/100 - 1)
            b1 = Math.round(255 * factor)
            b2 = Math.round(255 * Math.abs(factor-1))
            // return {r: 0, g: 0, b: b1}
            return {r1: 0, g1: 0, b1: b1, r2: 255, g2: 255, b2: b2}
        }
}

export default colourCalc