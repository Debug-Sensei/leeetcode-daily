class Solution(object):
    def sortVowels(self, s):
        vowels = []
        for ch in s:
            if ch in "aeiouAEIOU":
                vowels.append(ch)
        
        vowels.sort()   # sort vowels in ascending order
        
        # Convert string to list so we can modify it
        s_list = list(s)
        k = 0
        for i in range(len(s_list)):
            if s_list[i] in "aeiouAEIOU":
                s_list[i] = vowels[k]
                k += 1
        
        return "".join(s_list)  # return back as string