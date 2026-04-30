def solution(babbling):
    ans = 0
    baby = {"aya":3,"ye":2,"woo":3,"ma":2}
    for s in babbling:
        flag = False
        for i in range(4):
            for b in baby:
                if s[:baby[b]] == b:
                    s = s[baby[b]:]
                    if not s:
                        ans+=1
                        flag = True
                        break
            if flag:
                break
    return ans
                        
        