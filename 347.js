/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let counts = {}

    for(let num of nums){
        if(counts[num] === undefined){
            counts[num] = 1
        } else {
            counts[num] += 1
        }
    }
    let array = []
    for(let num in counts){
        array.push([counts[num],num])
    }

    array.sort(function(a,b) {
        return a[0] - b[0]
    }).reverse()

    let answer = []
    for(let i = 0; i < k; i++){
        answer.push(parseInt(array[i][1]))
    }
    return  answer
};
