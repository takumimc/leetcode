/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length != t.length){
        return false
    }
    let array = t.split('')
    for(char of s){
        let index = array.indexOf(char)
        if(index > -1){
        array.splice(index, 1)
        }
    }
    return array.length === 0
};
