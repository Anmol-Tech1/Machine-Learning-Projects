def countSubarrays(ar,mcnt): 
    count=0
    n=len(a)
    for m in range(mcnt+1):
        prefix = [0] * n 
        odd = 0
        # traverse in the array 
        for i in range(n): 
            prefix[odd] += 1
            # if array element is odd 
            if (a[i] & 1): 
                odd += 1
            # when number of odd elements>=M 
            if (odd >=m): 
                count += prefix[odd - m] 
    return count 
        
# Driver Code 
a = [2,1,2,1,3] 
n = len(a) 
m = 2

print(countSubarrays(a,m)) 


