/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let steps = 0
    while(num != 0){
        steps += 1
        if(num % 2 == 0){
            num = num/2
        } else {
            num -= 1
        }
    }
    return steps
};
