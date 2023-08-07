class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dict_alpha = {}

        def get_parent(a):
            if dict_alpha[a] == a:
                return a
            return get_parent(dict_alpha[a])

        def union_parent(a,b):
            aa,bb = get_parent(a),get_parent(b)
            if aa < bb:
                dict_alpha[bb] = aa
            else:
                dict_alpha[aa] = bb


        for i in range(97,123):
            dict_alpha[i] = i

        compare_size = len(s1)
        for idx in range(compare_size):
            union_parent(ord(s1[idx]), ord(s2[idx]))


        answer = ""

        for word in baseStr:
            answer += chr(get_parent(ord(word)))

        return answer