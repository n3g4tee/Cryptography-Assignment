# Hash là chuỗi nhị phân 11 bit
n = 1 << 11         
# Xác suất để nhóm n secret có ít nhất 1 cái gặp collision với secret của Jack
P = 1
for i in range(1, n):
    P = pow((1 - 1/n), i)
    nP = 1 - P
    if nP > 0.5:
        print(i)
        break 