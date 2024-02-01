
function colorInfo(color){
    switch(color) { 
        case 'red': 
            console.log("Red's a good color!"); 
            break;
        case 'blue': 
            console.log("That's my favorite color, too!"); 
            break; 
        case 'yellow': 
            console.log("Yuck!"); 
            break; //Add your case here! 
        default: 
            console.log("I don't think that's a primary color!"); 
    }
}

colorInfo("red")
colorInfo("blue")
colorInfo("purple")