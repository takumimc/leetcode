class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        smush = ''

        for char in s:
            if char.isalnum():

              smush += char.lower()
        reverse_smush = smush[::-1]

        return smush == reverse_smush
