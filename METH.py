#version 2
L=5

if L <3: print("100%")

if L == 3: print("80%")

if L > 3:
    N = (L+2)*((L+1)/2)
    A = 3
    B = 6
    C = 3*L-9
    D = 3 if L>3 else 0
    E = (3 * (L-4)) if L>4 else 0
    F = N - A - B - C - D - E

    AT = A*5
    BT = B*8
    CT = C*11
    DT = D*12
    ET = E*15
    FT = F*18
    NT = (AT+BT+CT+DT+ET+FT)/2
    print(NT)
    print(N*(N-1)/2)
    print(str((NT  /  (N*(N-1)/2))*100)+"%")







