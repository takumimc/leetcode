/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let length = 0
    let cur = head
    while(cur){
        length += 1
        cur = cur.next
    }

    let mid = head
    for(let i=0; i < parseInt(length/2 + 1) - 1; i++){
        mid = mid.next
    }
    return mid
};

var middleNode = function(head) {
    let once = head
    let twice = head

    while(twice){
        twice = twice.next
        if(twice){
            twice = twice.next
        } else{
            return once
        }
        once = once.next
    }
    return once
};
