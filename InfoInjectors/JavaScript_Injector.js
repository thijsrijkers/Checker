var jsonSource = "D:\!!!!!Checker\Storage\data.json";
var dataString = "";
const fs = require('fs');

const data = {
    "Word": dataString
};

const data = JSON.stringify(dataString);

fs.writeFile(jsonSource, data, (err) => {
    if (err) {
        throw err;
    }
    console.log("JSON data is saved.");
});