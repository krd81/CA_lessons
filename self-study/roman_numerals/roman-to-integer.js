/*
Convert Roman numerals to integers
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Process:
1) Variable to store the running total
2) Use a switch statement to check for different cases, it may be necessary to check for the next character to determine the value

*/

function romanToInt(string) {
    let total = 0

    for (let i = 0; i < string.length; i++) {
        switch (string[i]) {
            case 'I':
                if (i === string.length - 1 || string[i + 1] !== 'V' && string[i + 1] !== 'X') {
                    total += 1;
                } else if (string[i + 1] === 'V' || string[i + 1] === 'X') {
                    total -= 1;
                } else {
                    total += 0;
                }
                break;
            case 'V':
                total += 5;
                break;
            case 'X':
                if (i === string.length - 1 || string[i + 1] !== 'L' && string[i + 1] !== 'C') {
                    total += 10;
                } else if (string[i + 1] === 'L' || string[i + 1] === 'C') {
                    total -= 10;
                } else {
                    total += 0;
                }
                break;
            case 'L':
                total += 50;
                break;
            case 'C':
                if (i === string.length - 1 || string[i + 1] !== 'D' && string[i + 1] !== 'M') {
                    total += 100;
                } else if (string[i + 1] === 'D' || string[i + 1] === 'M') {
                    total -= 100;
                } else {
                    total += 0;
                }
                break;
            case 'D':
                total += 500;
                break;
            case 'M':
                total += 1000;
                break;
            default:
                total += 0;
            }
    }

let integer = total
console.log(`${string} = ${integer}`)
}

romanToInt('MCMXCIV')
romanToInt('MCMLXXXI')
romanToInt('MCMXCIX')
romanToInt('MMXXIV')
romanToInt('MCMLXXXV')


