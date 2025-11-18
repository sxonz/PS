for test in range(int(input())):
    n = int(input())
    d = [input() for i in range(n)]
    m = int(input())
    tmp = [input() for i in range(m)]
    no = set()
    for i in tmp:
        for j in range(len(i)):
            no.add(i[:j+1])
    if not no:
        print(1)
        continue
    trie = dict()
    for s in d:
        cur = trie
        for i in s:
            if i not in cur:
                cur[i] = dict()
            cur = cur[i]
    
    ans = 0
    for s in d:
        cur = trie
        for i in range(len(s)):
            if s[i] not in cur:
                break
            if s[:i+1] not in no:
                cur.pop(s[i])
                ans += 1
                break
            cur = cur[s[i]]
        else:
            ans += 1
    print(ans)