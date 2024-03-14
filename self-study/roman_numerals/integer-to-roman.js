/*
Convert integers to Roman numerals
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
1) Use string concatenation to build the Roman numeral
2) First check how many 1000s are in the number, then how many 100s, 10s, and 1s
*/

var intToRoman = function(num) {
    // example: 3524
    let remainder = num;
    let string = '';

    // count 1000s
    let thousands = 'M'.repeat(Math.floor(remainder / 1000)); // 3
    remainder = remainder % 1000; // 524

    let hundreds = Math.floor(remainder / 100);
    switch (hundreds) {
        case 9 :
            hundreds = 'CM';
            break
        case 8 :
        case 7 :
        case 6 :
        case 5 :
            hundreds = ('D').concat('C'.repeat(hundreds - 5))
            break
        case 4 :
            hundreds = 'CD';
            break
        case 3 :
        case 2 :
        case 1 :
            hundreds = 'C'.repeat(hundreds);
            break
        default :
            hundreds = '';
    }

    remainder = remainder % 100;

    let tens = Math.floor(remainder / 10);
    switch (tens) {
        case 9:
            tens = 'XC';
            break
        case 8:
        case 7:
        case 6:
        case 5:
            tens = ('L').concat('X'.repeat(tens - 5))
            break
        case 4:
            tens = 'XL';
            break
        case 3:
        case 2:
        case 1:
            tens = 'X'.repeat(tens);
            break
        default:
            tens = '';
    }
    remainder = remainder % 10;

    let ones = remainder; // 0
    switch (ones) {
        case 9:
            ones = 'IX';
            break
        case 8:
        case 7:
        case 6:
        case 5:
            ones = ('V').concat('I'.repeat(ones - 5))
            break
        case 4:
            ones = 'IV';
            break
        case 3:
        case 2:
        case 1:
            ones = 'I'.repeat(ones);
            break
        default:
            ones = '';
    }

    string = thousands.concat(hundreds, tens, ones);
    console.log(string);

}
// /Users/Kelly/projects/self-study/roman-to-integer/roman-to-integer.js
intToRoman(3); // III
intToRoman(47);
intToRoman(58);
intToRoman(1994); // MCMXCIV