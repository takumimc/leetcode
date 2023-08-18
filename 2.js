/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**

 */

// Doesn't work when numbesr too big
// var addTwoNumbers = function(l1, l2) {
//     let num1 = []
//     let cur1 = l1
//     while(cur1 != undefined){
//         num1.push(cur1.val)
//         cur1= cur1.next
//     }
//     let num2 = []
//     let cur2 = l2
//     while(cur2 != undefined){
//         num2.push(cur2.val)
//         cur2= cur2.next
//     }

//     const tot1 = parseInt(num1.reverse().join(''))
//     const tot2 = parseInt(num2.reverse().join(''))

//     console.log(tot1)

//     const tot = tot1 + tot2
//     const tot_array = Array.from(String(tot), Number).reverse()

//     let sum = new ListNode(tot_array[0])
//     tot_array.map((x,index) => {
//         if(index === 0){
//             return
//         }
//         else{
//             let cur_node = sum
//             for(let i=0; i < index - 1; i ++){
//                 cur_node = cur_node.next
//             }
//             cur_node.next = new ListNode(x)
//         }
//     })
//     return sum
// };

var addTwoNumbers = function(l1, l2) {

    let l3 = null

    let cur_l1 = l1
    let cur_l2 = l2

    let index = 0
    let sum = 0
    let carry = 0

    while(cur_l1 != null || cur_l2 != null){
        if(cur_l1 === null){
            sum = cur_l2.val
        } else if (cur_l2 === null){
            sum = cur_l1.val
        } else {
        sum = cur_l1.val + cur_l2.val
        }

        if(carry > 0){
            sum = sum + carry
            carry = 0
        }

        if(sum > 9){
            carry += 1
            sum -= 10
        }

        if(index === 0){
            l3 = new ListNode(sum)
        } else {
            let cur_node = l3
            for(let i=0; i < index -1; i++){
                cur_node = cur_node.next
            }
            cur_node.next = new ListNode(sum)
        }

        if(cur_l1 !== null){
            cur_l1 = cur_l1.next
        }
        if(cur_l2 !== null){
            cur_l2 = cur_l2.next
        }
        index += 1
  if(cur_l1 === null){
            if(carry > 0){
                let cur_node = l3
                for(let i=0; i < index -1; i++){
                    cur_node = cur_node.next
                }
                cur_node.next = new ListNode(carry)
            }
        }
    }
    return l3
};
