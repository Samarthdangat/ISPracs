g = int(input('Public Key G: '))
p = int(input('Public Key P: '))

a = int(input('Private Key a: '))
b = int(input('Private Key b: '))

Xa = pow(g, a, p)
Xb = pow(g, b, p)

print('Generated Keys:')
print('Key for a:', Xa)
print('Key for b:', Xb)

Ka = pow(Xb, a, p)
Kb = pow(Xa, b, p)

print('Symmetric Keys:')
print('Key for a:', Ka)
print('Key for b:', Kb)
