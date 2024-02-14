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
> freeCodeCamp.org (2019) JavaScript type coercion explained, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/ (Accessed: 11 February 2024). 

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

```
let currencyMap = new Map([
    ["Australia", "AUD"],
    ["United States", "USD"],
    ["Italy", "EUR"],
])
```

Q9 citations:
>(No date) JavaScript data types. Available at: https://www.w3schools.com/js/js_datatypes.asp (Accessed: 05 February 2024).
> MozDevNet (no date a) BigInt - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt (Accessed: 05 February 2024).
> MozDevNet (no date b) Number - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number (Accessed: 05 February 2024).
> (No date a) JavaScript sets. Available at: https://www.w3schools.com/js/js_sets.asp (Accessed: 08 February 2024).
> MozDevNet (no date b) Date - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date (Accessed: 08 February 2024).
> MozDevNet (no date c) Map - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map (Accessed: 10 February 2024).


Q10
(No date) JavaScript array methods. Available at: https://www.w3schools.com/js/js_array_methods.asp (Accessed: 10 February 2024).

Q11

```
Example object:
pet = {
    name: "Riley",
    age: "3",
    weight: "8"
    sex: "male",
    type: "dog",
    breed: "cavalier king charles spaniel",
    colour: "blenheim",
    registered: true
}

Function definition - methods applied on object properties:

pet.summary = function () {
    return this.name + " is a " + this.type + " who is " + this.age + " years old, weighing " + this.weight + "kg."
}

```

```
For in:

let text = ""
for (let property in pet){
    text += pet[property] + " "
}

```

```
For in:

let text = ""
for (let property in pet){
    text += property + " "
}

```

(No date a) JavaScript objects. Available at: https://www.w3schools.com/js/js_objects.asp (Accessed: 10 February 2024).

(No date b) JavaScript for in. Available at: https://www.w3schools.com/js/js_loop_forin.asp (Accessed: 10 February 2024).



Q12
```
let data = '{val1: 1, val2: 2, val3: 3, text: "some text"}

let JSONData = JSON.parse(data, function(key, value){
    if (typeof value === "number") {
        return value * 2
    }
    return value
})

Result:
JSONData = {"val1": 2, "val2": 4, "val3": 6, "text": "someText"}
```

```
let user ={fname: "Paula", lname: "Smith" , title: "Accounts Clerk", dept: "Finance", type: "full-time"}

let obj = JSON.stringify(user, ["fname", "lname", "dept"])

Result:
obj = '{"fname": "Paula","lname": "Smith" , "dept": "Finance"}'

```

```
Without toJSON():

let parent = {name: "Sandy", role: "PTA"}

let child = {name: "Chloe", age: 6}
child.parent = parent

console.log(JSON.stringify(child))

Result:
'{"name": "Chloe", "age": 6, "parent": {"name": "Sandy", "role": "PTA"}}'
```

```
With toJSON():

let parent = {name: "Sandy", role: "PTA", toJSON() {return this.name}}

let child = {name: "Chloe", age: 6}
child.parent = parent

console.log(JSON.stringify(child))

Result:
'{"name": "Chloe", "age": 6, "parent": "Sandy"}'

```


(No date a) JavaScript JSON. Available at: https://www.w3schools.com/js/js_json.asp (Accessed: 10 February 2024).

MozDevNet (no date) JSON - javascript: MDN, MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON (Accessed: 10 February 2024).

freeCodeCamp.org (2021) JSON object examples: Stringify and parse methods explained, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/json-stringify-method-explained/ (Accessed: 11 February 2024).