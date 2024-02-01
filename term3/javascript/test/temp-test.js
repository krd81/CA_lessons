function colourCalc(temp) {
    let r = 0
    let g = 0
    let b = 0
    let diff = 0
    let factor = 0
    // console.log(temp)
    // console.log(typeof temp)
    // console.log(temp>35 ? "Yes" : "No")
    
    switch (true) {
        case (temp > 45):
            r = 255
            g = 0
            b = 0
            break;
        case (temp > 35):
            diff = temp-35
            factor = Math.abs((diff / 10) - 1)
            g = Math.round(255 * factor)
            r = 255
            b = 0
            break;
        case (temp > 25):
            diff = temp-25
            factor = diff / 10
            r = Math.round(255 * factor)
            g = 255
            b = 0
            break;
        case (temp > 15):
            diff = temp-15
            factor = Math.abs((diff / 10) - 1)
            b = Math.round(255 * factor)
            r = 0
            g = 255
            break;
        case (temp > -15):
            diff = temp+15
            factor = diff / 30
            g = Math.round(255 * factor)
            r = 0
            b = 255
            break;
        default:
            factor = Math.abs(Math.abs(temp)/100 - 1)
            b = Math.round(255 * factor)
            r = 0
            g = 0

        }
        
        console.log(temp, {r: r, g: g, b: b})

}

colourCalc(Math.floor(Math.random() * 100))
colourCalc(Math.floor(Math.random() * 100))
colourCalc(Math.floor(Math.random() * 100))
colourCalc(Math.floor(Math.random() * 100))
