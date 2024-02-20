function calculateTicketPrice(dayType, age) {
    let price;

    if (age >= 0 && age <= 18) {
        switch (dayType.toLowerCase()) {
            case 'weekday': price = '12$'; break;
            case 'weekend': price = '15$'; break;
            case 'holiday': price = '5$'; break;
        }
    } else if (age > 18 && age <= 64) {
        switch (dayType.toLowerCase()) {
            case 'weekday': price = '18$'; break;
            case 'weekend': price = '20$'; break;
            case 'holiday': price = '12$'; break;
        }
    } else if (age > 64 && age <= 122) {
        switch (dayType.toLowerCase()) {
            case "weekday": price = "12$"; break;
            case "weekend": price = "15$"; break;
            case "holiday": price = "10$"; break;
      }
    } else {
      console.log("Error!"); return;  
    }

    console.log(price);
}

// Test with different day types and ages
calculateTicketPrice('Weekday', 42); // Should print: 18$
calculateTicketPrice('Holiday', -12); // Should print: Error!
calculateTicketPrice('Holiday', 15); // Should print: 5$