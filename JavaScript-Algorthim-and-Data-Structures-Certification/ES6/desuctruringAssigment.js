const HIGH_TEMPERATURES = {
    yesterday: 75,
    today: 77,
    tomorrow: 80
};

// Only change code below this line

const {today, tomorrow} = HIGH_TEMPERATURES

const {today: highToday, tomorrow: highTomorrow} = HIGH_TEMPERATURES

// Only change code above this line

const LOCAL_FORECAST = {
    yesterday: { low: 61, high: 75 },
    today: { low: 64, high: 77 },
    tomorrow: { low: 68, high: 80 }
};

// Only change code below this line
const { today: { low: lowToday, high: highToday }} = LOCAL_FORECAST;

// Only change code above this line

let a = 8, b = 6;
// Only change code below this line
[b, a]= [a, b];