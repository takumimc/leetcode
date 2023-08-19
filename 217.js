/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let counts = {}
    nums.map((num)=>{
        if(counts[num] === undefined){
            counts[num] = 1
        } else {
        counts[num] += 1
        }
    })
    let repeats = false
    let values = Object.values(counts)
    values.map((num)=>{
        if(num > 1){
            repeats = true
        }
    }
    )
    return repeats
};

var containsDuplicate = function(nums) {
    set = new Set(nums)
    return set.size != nums.length
};

var containsDuplicate = function(nums) {
    let counts = {}
    nums.map((num)=>{
        if(counts[num] === undefined){
            counts[num] = 1
        } else {
        counts[num] += 1
        }
    })
    return Object.keys(counts).length != nums.length
};
