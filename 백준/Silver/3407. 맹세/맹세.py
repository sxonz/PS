import sys
input = sys.stdin.readline
d = 'H	 	 	 	 	 	 	 	 	 	 	 	 	 	 	 	 	He Li	Be	 	 	 	 	 	 	 	 	 	 	B	C	N	O	F	Ne Na	Mg	 	 	 	 	 	 	 	 	 	 	Al	Si	P	S	Cl	Ar K	Ca	Sc	Ti	V	Cr	Mn	Fe	Co	Ni	Cu	Zn	Ga	Ge	As	Se	Br	Kr Rb	Sr	Y	Zr	Nb	Mo	Tc	Ru	Rh	Pd	Ag	Cd	In	Sn	Sb	Te	I	Xe Cs	Ba		Hf	Ta	W	Re	Os	Ir	Pt	Au	Hg	Tl	Pb	Bi	Po	At	Rn Fr	Ra	Rf	Db	Sg	Bh	Hs	Mt	Ds	Rg	Cn	 	Fl	 	Lv	 	 La	Ce	Pr	Nd	Pm	Sm	Eu	Gd	Tb	Dy	Ho	Er	Tm	Yb	Lu Ac	Th	Pa	U	Np	Pu	Am	Cm	Bk	Cf	Es	Fm	Md	No	Lr'.split()
d = [i.lower() for i in d]
r = [[],[]]
for i in d:
    if len(i) == 1:
        r[0].append(i)
    else:
        r[1].append(i)
for t in range(int(input())):
    s = input().strip()
    n = len(s)
    dp = [0]*(n+2)
    dp[-1] = 1
    for i in range(n):
        if dp[i-1]:
            for j in r[0]:
                if s[i] == j:
                    dp[i] = 1
                    break
        if i<n-1 and dp[i-1]:
            for j in r[1]:
                if s[i:i+2] == j:
                    dp[i+1] = 1
    print("YNEOS"[dp[n-1]^1::2])
