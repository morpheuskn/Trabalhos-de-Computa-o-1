s=str(input())
n=int(input())
def retira(s,n):
    if s=="" or n<0 or n>=len(s):
        return
    return s[:n] + s[n+1:]
    
print(retira(s,n))
