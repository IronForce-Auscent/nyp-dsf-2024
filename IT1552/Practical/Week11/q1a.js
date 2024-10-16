var userInput = parseInt(prompt("Enter a number: "));
if (isNaN(userInput)) {
    alert("Please enter a number");
} else if (userInput == 0) {
    alert("You have entered a zero");
} else if (userInput > 0) {
    alert("You have entered a positive number");
} else {
    alert("You have entered a negative number");
}