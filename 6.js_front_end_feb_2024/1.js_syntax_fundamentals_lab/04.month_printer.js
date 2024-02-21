function printMonth(monthNumber) {
  if (monthNumber < 1 || monthNumber > 12) {
    console.log("Error!");
  } 
  else {
    let months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    console.log(months[monthNumber - 1]);
  }
}

// Example usage:
printMonth(2); // Output: February
printMonth(13); // Output: Error!
