### Q7

```
let age = prompt("Enter your age: ")

if (age > 64 ){
    return "User is a senior citizen"
} else if (age > 17 ) {
    return "User is an adult"
} else {
    return "User is a child"
}
```

```
let count = 0

while (count < 10) {
    console.log(count)
    count ++
}
```

### Q8
```
let num = 5 // num is type Number
num = "five" // num is type String
num = false // num is type Boolean
```

```
let a = 2 // a is type Number
let b = "5" // b is type String
let c = a + b // c is type String
```

> MozDevNet (no date c) Type coercion - MDN web docs glossary: Definitions of web-related terms: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion (Accessed: 05 February 2024).

### Q9
String: `let name = 'Sally'`
Number:
```
let a = 10
let b = 3
let c = a * b
```
BigInt: `let largeNumber = BigInt("9007199254741000")`

```
Boolean:

let score = prompt("Enter your test result: ")
let pass = false

if (score > 49 ){
    pass = true
}
return pass

```

```
Error example:

let age = prompt("Enter your age: ")

try {
    if (typeof (age) !== number) throw Error ('Age must be a number')

} catch (error) {
    console.log(error.message)
}
```

Q9 citations:
(No date) JavaScript data types. Available at: https://www.w3schools.com/js/js_datatypes.asp (Accessed: 05 February 2024).
MozDevNet (no date a) BigInt - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt (Accessed: 05 February 2024).
MozDevNet (no date b) Number - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number (Accessed: 05 February 2024).
(No date a) JavaScript sets. Available at: https://www.w3schools.com/js/js_sets.asp (Accessed: 08 February 2024).
MozDevNet (no date b) Date - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date (Accessed: 08 February 2024).