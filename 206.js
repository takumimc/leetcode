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
var reverseList = function(head) {

    let cur_node = head
    let reversed_list = null

    while (cur_node != null){
        if(reversed_list === null){
            reversed_list = new ListNode(cur_node.val)
        } else {
            let cur_rev = reversed_list
            reversed_list = new ListNode(cur_node.val)
            reversed_list.next = cur_rev
        }


    cur_node = cur_node.next

    }
    return reversed_list
};
