/**Use Destructuring Assignment to Extract Values from Objects*/
const HIGH_TEMPERATURES = {
    yesterday: 75,
    today: 77,
    tomorrow: 80
};
const {today, tomorrow} = HIGH_TEMPERATURES
const {today: highToday, tomorrow: highTomorrow} = HIGH_TEMPERATURES

/**Use Destructuring Assignment to Assign Variables from Nested Objects*/
const LOCAL_FORECAST = {
    yesterday: { low: 61, high: 75 },
    today: { low: 64, high: 77 },
    tomorrow: { low: 68, high: 80 }
};
const { today: { low: lowToday, high: highToday }} = LOCAL_FORECAST;

/**Use Destructuring Assignment to Assign Variables from Arrays*/
let a = 8, b = 6;
[b, a]= [a, b];

/**Destructuring via rest elements*/
function removeFirstTwo(list) {
    const [,,...shorterList] = list;
    return shorterList;
}

const source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const sourceWithoutFirstTwo = removeFirstTwo(source);
/**Use Destructuring Assignment to Pass an Object as a Function's Parameters*/
const stats = {
    max: 56.78,
    standard_deviation: 4.34,
    median: 34.54,
    mode: 23.87,
    min: -0.75,
    average: 35.85
};

const half = ({max, min}) =>  (max + min) / 2 ;
//const half = (stats) => (stats.max + stats.min) / 2.0;
console.log(half(stats))