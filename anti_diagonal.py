
def anti_diagonal(arr,r,c):
    s = r+c
    max_step = min(n,m)
    if s < max_step:
        rs=0
        step = s+1
    else:
        rs   = s - max_step +1
        step = max_step-rs

    print(f'start {rs} with {step} steps')
    ans = list()
    for i in range(rs,rs+step):
        print(i,s-i)
        ans.append(arr[i][s-i])
    return ans

def anti_diagonal_v2(arr,r,c):
    s = r+c
    if s < len(arr):
        r_e = s
    else:
        r_e = len(arr)-1
    ans = []
    for i in range(r_e,-1,-1):
        print(i,s-i)
        if s-i == len(arr[0]):
            break
        ans.append(arr[i][s-i])
    return ans

def anti_diagonal_v3(arr,r,c):
    s = r+c
    n = len(arr)
    m = len(arr[0])

    if s < n:
        r_e = s
    else:
        r_e = n-1
    c_e = s-r_e
    step = min(r_e+1,m-c_e)
    print(r_e,step)
    ans = []
    for i in range(r_e,r_e-step,-1):
        ans.append(arr[i][s-i])
    return ans

if __name__ == '__main__':
    n,m = 3,7
    r,c = 2,0
    arr = [[i*n+j for j in range(m)] for i in range(n)]
    print('\n'.join(map(str,arr)))
    print()
    print(f'point {r},{c}')
    print(anti_diagonal_v2(arr,r,c))
    print(anti_diagonal_v3(arr,r,c))
