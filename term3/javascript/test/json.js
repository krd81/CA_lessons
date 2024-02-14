let parent = {name: "Sandy", role: "PTA", toJSON() {return this.name}}

let child = {name: "Chloe", age: 6}
child.parent = parent
parent.child = child.name

let room = {
    number: 23,
    toJSON() {
      return this.number;
    }
  };

let meetup = {
    title: "Conference",
    room
  };

console.log( JSON.stringify(child) );

// console.log( JSON.stringify(parent) )