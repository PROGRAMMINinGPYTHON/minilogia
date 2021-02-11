def dostawa(x, y):
    a = y
    b = y
    c = y
    lcz_zrealiowanych = 0
    for i in range(len(x)):
        if a >= x[i].count("a") and b >= x[i].count("b") and c >= x[i].count("c"):
            lcz_zrealiowanych += 1
            a = a - x[i].count("a")
            b = b - x[i].count("b")
            c = c - x[i].count("c")
    return lcz_zrealiowanych


dostawa(["abc", "abaa", "caa", "bbbcc", "cac", "abc"], 5)

testy = [
    [["a"], 1, 1],
    [["abac", "baaba", "acac", "babc"], 6, 3],
    [["abc", "abaa", "caa", "bbbcc", "cac", "abc"], 5, 4],
    [["aaa", "bbb", "ccc"], 3, 3],
    [["baaacaaa", "bbb", "bbccbbb"], 5, 1],
    [["b", "bbb", "bbbbbbb"], 15, 3],
    [["baba", "baba", "baba"], 1, 0],
    [["baaacaaa", "bbccbbb", "bbb"], 5, 1],
    [["aacbacaaccbbbbbcbccbacaababcca", "bcaccaaabcacbbbbacbbabbacaaccc","abacaabacccabbbbcaaccccbbcbaab", "acabccbacaaabbccaaaabccbbbbbcc","ccbcbabbabacbacacbcaabcbaacacb", "baabcccabbbbccbaaabcabcabaaccc","cbabcbcabccabbabccaccaacbbbaaa", "bbacbbcbcbaacbcccabcbabaaaccaa","babbcaabbaaccacabcabcccbacbabc", "abbcaaabaabbcbbccccbcacacbaacb"], 50,5],
    [["cbacaaccbbbbbcbccbacaa", "ccaaabcacbbbbacbbabbacaac","bacccabbbbcaaccccb", "acaaabbccaaaabccbbbb", "abbabacbacacbcaabcbaacac","cabbbbccbaaabcabcabaac", "bcbcabccabbabccaccaacbbb", "cbcbaacbcccabcbab","baaccacabcabcccbacb", "bcaaabaabbcbbccccbcacacbaac"], 30,4],
    [["acca", "cccab","cbabacbc", "caabcbca", "baca", "acabba", "bcbc", "abc","ac", "bcca", "ccbaabc", "bacb", "bbac", "caabcb", "bbcc", "abacbab", "abbca", "ab","cbbc", "cbbaba", "abc", "ccba", "a", "abcaabc", "cabccaba", "aabcca", "ccb", "abaab","ccabac", "bcbb", "bbbacc", "c", "acba", "baccaabb", "bacac", "bba", "cccb", "abcaa","bcbaa", "cabbcc", "accacabbb", "caccbb", "caa", "cbcb", "acccb", "caba", "cccaa","bcabc", "aaab", "cbab", "bb", "ac", "cacbb", "cabacb", "acca", "bcaaac", "ccab","babca", "acacbbb", "bab", "cbbaacc", "cbbc", "abbccca", "abbac", "cbbc", "caabcacbb", "c", "abacbca", "caaabcb", "bcbac", "bccbacba", "bcca", "bbcaccaa", "accb", "cbbbcc","a", "bacaa", "cabca", "cca", "accbc", "bbac", "abaccbc", "bccaa", "bcc", "acbbca","ccabaabcb", "baca", "bbaacacc", "bac", "acabcac", "baaa", "ababccc", "aabab", "ccbcab", "cacca", "cabaabc", "bccacaab", "cabbb", "acbc", "cabcacba"],100,64],
[["acbcba", "bbaaacb", "accbb", "abccabac", "ac", "ccbbaacab", "baba",
"baaabc", "baac", "baccab", "bacc", "bbacc", "abcab", "abbb", "bcaa", "c", "cbabab",
"bbccbca", "abac", "aacbb", "cacabcab", "cabab", "aabbccac", "accbbba", "caaccb",
"abac", "bacacb", "acabb", "bccbca", "bb", "abccb", "aaaccbbc", "bbbc", "ba", "aaa",
"caacabcb", "bbcab", "baacba", "acaab", "bcab", "cbbaab", "bbaa", "bcbba", "cba",
"cbbcaa", "abaa", "cacc", "bccac", "acacb", "ccbcba", "cbbabacca", "aacabccb", "ccbb",
"bcbacaa", "cbcca", "babca", "acccb", "acbbbca", "babaa", "bbcbca", "aaccab", "bab",
"bbb", "b", "cbb", "bbbc", "abcc", "bbaba", "ac", "cab", "b", "baa", "accbb", "abaac",
"ccc", "cca", "baac", "cbccb", "abbaa", "bbcaabc", "c", "ab", "ba", "cbc", "cbac",
"bccba", "aaccbabc", "bbcbaacac", "ccbaa", "acca", "abccaa", "ac", "aaccbbab", "cba",
"aaaccb", "aaabcb", "bacc", "acca", "ccbab", "cabaa",
"bc", "cac", "acbccbaa", "cbacb",
"bbcbac", "cbabccbaa", "bacca", "aba", "bcacabbca", "bccabc", "aacb", "abbcb",
"acbcba", "cbac", "aacacb", "cac", "accbb", "cabcba", "a", "cbaaacb", "bbc", "cbabac",
"babcbcc", "cbabcc", "cbaccab", "ccbbabaca", "abbbac", "bcca", "cabbba", "ca",
"cbacbc", "aacbbacc", "cac", "bca", "caacbb", "bbacacc", "ccba", "abbcabc", "baba",
"bacba", "bcbaacb", "acbbba", "aaa", "bbbacac", "acb", "cbcaacb", "cabcaac",
"aabcbbcc", "bcbcacbaa", "baaccbc", "bcca", "abcb", "cac", "bcbac", "bcaabc", "babc",
"aaccb", "baacba", "accabbcb", "cb", "ca", "ccbbaaab", "caccbbaab", "bbca",
"bcacaabc", "cabbcb", "abca", "cabcba", "cc", "caabbbac", "abbaa", "caccb", "aa",
"baca", "aacbbcb", "cbbaacba", "bac", "caabbbca", "bbabccca", "aabccab", "bcacbbc",
"cbcaaa", "ccaab", "bcba", "cba", "b", "aabb", "abcaacb", "baccabba", "bcac", "bb",
"acac", "bbacbcc", "cb", "accbb", "ccbbcbaaa", "babca", "aaccc", "cbbcac", "aabccab"], 150,96],
[["cbab", "ccaaca", "acb", "babbaccc", "abc", "cbabca", "ccacbb", "acabcb","bacbaacc", "ccbbca", "bca", "ccbcaa", "ccabc", "cbbaabc", "bcaab", "caabab", "babac","aca", "bacab", "aabacbcb", "acbc", "bac", "ccb", "bac", "caac", "ba", "ccaab", "ccba","bac", "acbcab", "ba", "acbcac", "cbac", "aac", "abcbbc", "aacc", "aaccbca", "ccc","abcabac", "acbbaca", "cbcca", "ca", "ac", "acccb", "aaabbcc", "aaa", "cabbac", "baab","accbcb", "ccb", "bccaca", "cbcac", "ab", "cab", "bc", "cc", "b", "cbaacbc", "bba","cbacbcbaa", "aa", "bcabaac", "caaaccb", "aca", "baca", "acbacb", "bacaa","ccacbbaab", "abcba", "bcb", "abccb", "baaabc", "cabc", "cabccba", "bc", "cacbaacb","abbcb", "cbca", "abcca", "ccacb", "bcac", "abbcaa", "cabcba", "baccb", "bbca","abbcaa", "cabcbcab", "ac", "cbccbb", "ccb", "acabbbac", "cbcaa", "caabcbb", "babca","bab", "cbaccbbaa", "cba", "cabbb", "ababacccb", "aabcbcba", "bcabcba", "bcbacab","aabc", "cbaaacc", "cccab", "aba", "aaaccb", "bcbba", "cabbaba", "bb", "caa", "bab","bacca", "bcbbc", "ccbbbc", "babc", "caacac", "cabaa", "bccab", "bcba", "bab","ccbaac", "babba", "acacbb", "baabc", "bc", "cabbaac", "ca", "babac", "bcca", "caca","abacca", "caabb", "cac", "bb", "acbb", "b", "bacbbcaa", "bcbc", "cbabbc", "cb","bcbabaca", "ccabb", "bcbba", "cabacbba", "babba", "abccbb", "abcba", "baabcbca","cc", "b", "aa", "cbbbca", "accbb", "accaabb", "acbccaa", "bbcacaa", "aabccab", "ccbca","bacb", "cbacba", "aca", "ac", "cc", "aaacbcb", "ababccab", "bcb", "ccbac", "caca", "a","bbcaba", "aa", "ccaacbb", "aacabb", "abcccaabb", "cbacaa", "babcabc", "bccaa","aacb", "cbcabbaca", "baacc", "cbcca", "bcabaa", "abc", "cbcbaa", "cccabaab","cacbcab", "abbaca", "abaac", "abacba", "abac", "baabc", "bcaaca", "bc", "cbbaa","bba", "cbaacbbc", "accbbb", "aacbaccb", "abcabac"], 250,156],


]


def testowanie():
    for x in testy:
        # msg =
        print(dostawa(x[0], x[1]))
        assert dostawa(x[0], x[1]) == x[2]
    print("OK")


testowanie()
