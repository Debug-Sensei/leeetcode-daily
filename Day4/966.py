class Solution(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)
        
        exact = set(wordlist)
        case_map = {}
        vowel_map = {}
        
        for word in wordlist:
            lower = word.lower()
            dev = devowel(lower)
            if lower not in case_map:
                case_map[lower] = word
            if dev not in vowel_map:
                vowel_map[dev] = word
        
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            elif q.lower() in case_map:
                ans.append(case_map[q.lower()])
            elif devowel(q.lower()) in vowel_map:
                ans.append(vowel_map[devowel(q.lower())])
            else:
                ans.append("")
        
        return ans