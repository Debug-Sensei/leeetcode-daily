class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        L=list(text.split())
        count = 0
        for i in L:
            flag = 0
            for j in brokenLetters:
                if j in i:
                    flag=1
                    break
            if flag == 1:
                continue
            count+=1
        return count