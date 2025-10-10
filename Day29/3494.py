class Solution:
    def minTime(self, skill, mana):
        n, m = len(skill), len(mana)

        def job_prefix(j):
            pref = [0] * (n+1)
            for i in range(n):
                pref[i+1] = pref[i] + skill[i] * mana[j]
            return pref

        prev_pref = job_prefix(0)
        s0 = [0]*m
        for j in range(1, m):
            cur_pref = job_prefix(j)
            best = -10**30
            for i in range(n):
                candidate = s0[j-1] + prev_pref[i+1] - cur_pref[i]
                if candidate > best:
                    best = candidate
            s0[j] = best
            prev_pref = cur_pref

        return s0[-1] + prev_pref[-1]