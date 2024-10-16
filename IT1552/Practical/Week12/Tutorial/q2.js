var scores = [67, 90, 88, 70];

for (var score in scores) {
    console.log(score);
}

console.log(scores.reduce((partialSum, a) => partialSum + a, 0))