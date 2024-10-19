N, Q = map(int, input().split())  
H = []
T = []

for i in range(Q):
    h, t = input().split()
    H.append(h) 
    T.append(int(t))  

L_now = 1
R_now = 2
ans = 0  

for i in range(Q):
    h = H[i]
    t = T[i]
    
    if L_now < R_now:
        if h == 'L':
            if L_now < t and t < R_now:
                ans += t-L_now
            elif t < L_now:
                ans += L_now-t
            elif R_now < t:
                ans += N-t+L_now
            L_now = t
        elif h == 'R':  
            if L_now < t and t < R_now:
                ans += R_now-t
            elif t < L_now:
                ans += N-R_now+t
            elif R_now < t:
                ans += t-R_now
            R_now = t
    else:
        if h == 'L':
            if R_now < t and t < L_now:
                ans += L_now-t
            elif t < R_now:
                ans += N+t-L_now
            elif L_now < t:
                ans += t-L_now
            L_now = t
        elif h == 'R':  
            if R_now < t and t < L_now:
                ans += t-R_now
            elif L_now < t:
                ans += N-t+R_now
            elif t < R_now :
                ans += R_now-t
            R_now = t
print(ans) 
