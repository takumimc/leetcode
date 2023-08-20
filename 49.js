/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let groups = []
    for(word of strs){
        let pushed = false
        if(groups.length === 0){
            groups.push([word])
            continue
        } else {
            for(base of groups){
                if(word.length != base[0].length){
                    continue
                }
                let array = word.split('')
                    for(char of base[0]){
                        let i = array.indexOf(char)
                        if(i > -1){
                            array.splice(i,1)
                        }
                    }
                    if(array.length === 0){
                        base.push(word)
                        pushed = true
                    }
                }
        }
        if(pushed === false){
            groups.push([word])
        }
    }
    return groups
};
