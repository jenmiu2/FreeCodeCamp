class Thermostat {
    constructor(temperature) {
        this._temperature = (5/9) * (temperature - 32);
    }

    get temperature() {
        return this._temperature;
    }

    set temperature(celsius) {
        this._temperature = celsius;
    }
}

const thermos = new Thermostat(76);
let temp = thermos.temperature; // 24.44 in Celsius
thermos.temperature = 26;
temp = thermos.temperature; // 26 in Celsius