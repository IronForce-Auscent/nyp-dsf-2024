userInput = parseInt(prompt("Enter a number: "));
switch (userInput) {
    case userInput == 0:
        alert("You have entered a zero");
        break;
    case userInput > 0:
        alert("You have entered a positive number");
        break;
    case userInput < 0:
        alert("You have entered a negative number");
        break;
    case isNaN(userInput):
        alert("Please enter a number");
        break;
    default:
        break;
}