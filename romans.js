var romanToInt = function(s) {
            const roman_nums = {
            'I' : 1,
            'V' : 5,
            'IV': 4,
            'IX': 9,
            'X' : 10,
            'XL':40,
            'L' : 50,
            'XC': 90,
            'C' : 100,
            'CD':400,
            'D' : 500,
            'CM':900,
            'M' : 1000,
        }
        let sum = 0
        for (let i = 0; i < s.length; i++){
            let num = 0
            if (roman_nums[s.slice(i,i+2)] !== undefined){
                num = roman_nums[s.slice(i,i+2)]
                i++
            } else {
                num = roman_nums[s[i]]
            }
            sum += num
        }
        return sum
    }




    // console.log(romanToInt("MCMXCIV"))

    var isPalindrome = function(head) {
        let reverse = []
        for (let i = head.length - 1; i > -1; i--){
            reverse.push(head[i])
        }
        for (let i = 0; i < head.length;i++){
            if (reverse[i] !== head[i]){
                return false
            }
        }
        // console.log(reverse)
        return true
    }
// const a = [1,2]
// console.log(isPalindrome(a))


// let arr = [1,2,3,4,5]
// arr.splice(2,1)
// console.log(arr)


var kWeakestRows = function(mat, k) {
    let scores = {}
    let order = []
    let i = -1
    for (let row of mat){
        i += 1
        let score = 0
        for (let num of row){
            if (num === 1){
                score += 1
            }
        }
        if (scores[score] === undefined){
            scores[score] = [i]
        } else{
        scores[score].push(i)
    }
}
    for (let key in scores){
        const arr = scores[key]
        for (let i of arr){
            order.push(i)
        }
    }
    return order.slice(0,k)
};

// const a = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
// const b = 2

const a = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
const b = 3

console.log(kWeakestRows(a,b))
