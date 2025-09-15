class Solution:
    def spellchecker(self, a: List[str], q: List[str]) -> List[str]:
        m1,f = {s:s for s in a},lambda s:re.sub('[aeiou]','a',s.lower())
        m2,m3 = {s.lower():s for s in a[::-1]},{f(s):s for s in a[::-1]}
        return [m1.get(s,m2.get(t:=s.lower(),m3.get(f(t),''))) for s in q]