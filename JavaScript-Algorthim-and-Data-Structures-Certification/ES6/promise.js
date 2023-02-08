/**Promise is a constructor function,
 * so you need to use the new keyword to create one. It takes a function,
 * as its argument, with two parameters - resolve and reject.
 * These are methods used to determine the outcome of the promise. */
const makeServerRequest = new Promise((resolve, reject) => {
    // responseFromServer represents a response from a server
    let responseFromServer;

    if(responseFromServer) {
        // Change this line
        resolve('We got the data');
    } else {
        // Change this line
        reject('Data not received');
    }
});

//receive the good result
makeServerRequest.then(result => {
    console.log(result)
});

//receive the bad result

makeServerRequest.catch(error => {
    console.log(error);
});