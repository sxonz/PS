d = [input() for i in range(int(input()))]
print("INCREASING" if d == list(sorted(d)) else ("DECREASING" if d == list(sorted(d,reverse=True)) else "NEITHER"))