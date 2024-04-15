x = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
prime = [853, 857, 859, 863, 877, 881, 883, 887, 907, 911,919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
check=False
for p in prime:
    for a in range(2,1000):
        for i in range(len(x)-1):
            if x[i] * a % p == x[i + 1]:
                check = True
            else:
                check = False
                break
        if check:
            print(p, a)
            break
    if check:
        break

     