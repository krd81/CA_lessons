import React from 'react'

const tempCalc = () => {



    function colourCalc(temp) {
        let r = 0
        let g = 0
        let b = 0
        let diff = 0
        let factor = 0
        switch (temp) {
            case temp>45:
                return {r: 255, g: 0, b: 0}
                // break;
            case temp>35:
                diff = temp-35
                factor = Math.round(Math.abs((diff / 10) - 1))
                g = 255 * factor
                return {r: 255, g: g, b: 0}
            case temp>25:
                diff = temp-25
                factor = Math.round(diff / 10)
                r = 255 * factor
                return {r: r, g: 255, b: 0}
            case temp>15:
                diff = temp-15
                factor = Math.round(Math.abs((diff / 10) - 1))
                b = 255 * factor
                return {r: 0, g: 255, b: b}
            case temp>-15:
                diff = temp+15
                factor = Math.round(diff / 30)
                g = 255 * factor
                return {r: 0, g: g, b: 255}
            default:
                factor = Math.abs(Math.abs(temp)/100 - 1)
                b = 255 * factor
                return {r: 0, g: 0, b: b}
            } 

        
    }



  return (
    <div>tempCalc</div>
  )
}

export default tempCalc


// HOT: 255, 0, 0 = RED
// MEDIUM RANGE 255, 255, 0 = YELLOW
// MEDIUM RANGE 0, 255, 0 = GREEN
// MEDIUM RANGE 0, 255, 255 = LT BLUE
// COLD: 0, 0, 255 = DK BLUE

// > 45c = 255, 0, 0
// > 35c = 255, 255, 0
// > 25c = 0, 255, 0
// > 15c = 0, 255, 255
// > -50c = 0, 0, 255