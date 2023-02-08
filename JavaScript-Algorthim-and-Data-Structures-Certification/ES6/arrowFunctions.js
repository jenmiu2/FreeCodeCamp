const magic = () => new Date();
console.log(magic());
const myConcat = (arr1, arr2) => arr1.concat(arr2);

console.log(myConcat([1, 2], [3, 4, 5]));

const increment = (number, value = 1) => number + value;

const sum = (...args) => {
    return args.reduce((a, b) => a + b, 0);
}