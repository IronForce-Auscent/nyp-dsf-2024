array1 = [1,0,9,3,4,5,3];
array2 = [2,3,4,6,2,3,2,16, 9];

maxIndex = Math.max(array1.length, array2.length);
result = [];

for (i = 0; i < maxIndex; i++) {
    num1 = array1[i] || 0;
    num2 = array2[i] || 0;
    result.push(num1 + num2);
}

console.log(result);