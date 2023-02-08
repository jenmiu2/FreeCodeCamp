function randomRange(myMin, myMax) {
    // Only change code below this line
    return Math.floor(Math.random() * (myMax - myMin + 1)) + myMin;
    // Only change code above this line
}

function convertToInteger(str) {
    return parseInt(str,2);
}

console.log(randomRange(5,3))