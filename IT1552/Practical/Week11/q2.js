let userInput = 0;
while (userInput != "Q") {
    userInput = parseInt(prompt("Enter a number, or Q to quit: ").toUpper());
    if (userInput == "Q") {
        alert("Alright, see you soon!");
    } else if (isNaN(userInput)) {
        alert("Please enter a number");
    } else if (userInput == 0) {
        alert("You have entered a zero");
    } else if (userInput > 0) {
        alert("You have entered a positive number");
    } else {
        alert("You have entered a negative number");
    }
}