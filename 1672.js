/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max = 0

    accounts.map((customer) =>{
        let tot = 0
        customer.map((account) =>{
            tot += account
        })
        if(tot > max){
            max = tot
        }
    })

    return max
};
