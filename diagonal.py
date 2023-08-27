# return the diagonal line of given opint

def diagonal(arr,r,c):
    """
    arr => 2d array
    r => row
    c => column
    return diagonal
    """
    l = min(r,c)
    u = min(len(arr)-r,len(arr[0])-c)
    
    ans = list()
    for i,j in zip(range(r-l,r+u),range(c-l,c+u)):
        ans.append(arr[i][j])
    return ans

def diagonal2(arr,r,c):
    l = min(r,c)
    u = min(len(arr)-r,len(arr[0])-c)
    d = r-c
    ans = []
    for i in range(r-l,r+u):
        ans.append(arr[i][i-d])
    return ans


if __name__ == '__main__':
    n,m = 4,4
    r,c = 1,2
    arr = [[i*n+j for j in range(m)] for i in range(n)]
    print('\n'.join(map(str,arr)))
    print()
    print(r,c)
    print(diagonal(arr,r,c))
    print(diagonal2(arr,r,c))
