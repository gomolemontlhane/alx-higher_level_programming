#!/usr/bin/node

const request = require('request');

// Get the URL from the command-line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  
  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
