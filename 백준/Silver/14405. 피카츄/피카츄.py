s = input().replace("pi","Ǽ").replace("ka","Ǽ").replace("chu","Ǽ")
if len(set(list(s))) == 1 and s[0] == "Ǽ":
    print("YES")
else:
    print("NO")