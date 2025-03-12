class Solution:
    def reverseWords(self, s: str) -> str:
        # split s into all of its words
        # ss is a list
        ss = s.split()
        ss.reverse()

        # use " " with a space, so it does the reversed list, then space, then list element, and then space and then so on
        string = " ".join(ss) # or ss[::-1]
        # can append these words to a empty string or use .join method

        return string

# one line approach
# return " ".join(s.split().reversed())