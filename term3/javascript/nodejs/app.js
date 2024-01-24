const dice = require("./dice");

console.log(`The dice will roll ${process.env.ROLL_COUNT} times!`);

for (let index = 0; index < process.env.ROLL_COUNT; index++) {
    console.log(dice.rollDice(20));
    
}