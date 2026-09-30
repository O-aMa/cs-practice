a = int(input())
n = int(input())
ker = 0
kb = 0
kmax = 0
ksr = 0
print(n)
for i in range(n):
    z = input()
    if z != 'error':
        z = float(z)
        ksr += z
        if z > a:
            kb += 1
        if z > kmax:
            kmax = z
    else:
        ker += 1
        n -= 1
print(ker, kb, kmax, sep='\n')
print(f'{ksr/n:.1f}')
