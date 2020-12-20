

def neon(a):
    max = [0,1]
    for i in range(len(a)-1):
        print(len(a))
        if a[i]+a[i+1]>max[0]+max[1]:
            max[0] = a[i]
            max[1] = a[i+1]
        print(max[0],max[1])
neon([9,8,0,1,10,0,11])

