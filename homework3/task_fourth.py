from collections import defaultdict

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = defaultdict(list)
for key in set(list(a.keys()) + list(b.keys())):
    if key in a:
        ab[key].append(a[key])
    else:
        ab[key].append(None)
    if key in b:
        ab[key].append(b[key])
    else:
        ab[key].append(None)

print(sorted(ab.items()))
