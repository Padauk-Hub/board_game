def ngram_v2(arr,n,w=4):
     l = max(0,n-w+1)
     u = min(len(arr),n+w)

     for i in range(l,u-w+1):
         print(arr[i:i+w])

if __name__ == '__main__':
    arr = list(range(9))
    i=1
    ngram_v2(arr,i)

