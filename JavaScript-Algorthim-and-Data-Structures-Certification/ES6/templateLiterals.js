/**Create Strings using Template Literals*/
const result = {
    success: ["max-length", "no-amd", "prefer-arrow-functions"],
    failure: ["no-var", "var-on-top", "linebreak"],
    skipped: ["no-extra-semi", "no-dup-keys"]
};

function makeList(arr) {
    // Only change code below this line
    const failureItems = arr.map(function(element){
        return `<li class="text-warning">${element}</li>`
    });
    // Only change code above this line

    return failureItems;
}

const failuresList = makeList(result.failure);
console.log(failuresList)

/**Write Concise Object Literal Declarations Using Object Property Shorthand*/
const createPerson = (name, age, gender) => ({name,age,gender});
/**Write Concise Declarative Functions with ES6*/

const bicycle = {
    gear: 2,
    setGear: function(newGear) {
        this.gear = newGear;
    }
};
const bicycle = {
    gear: 2,
    setGear(newGear) {
        this.gear = newGear;
    }
};

bicycle.setGear(3);
console.log(bicycle.gear);

/**Use class Syntax to Define a Constructor Function*/
class Vegetable {
    constructor(name) {
        this.name = name;
    }
}
const carrot = new Vegetable('carrot');
console.log(carrot.name); // Should display 'carrot'
