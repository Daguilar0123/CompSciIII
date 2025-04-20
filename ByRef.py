# Some other examples:
x = 10
lx = [10]
ly = [5 + 5]
print("x:", x, "address:", hex(id(x)), "\n",
    "lx:", lx, "address:", hex(id(lx)), "\n",
    "ly:", ly, "address:", hex(id(ly)))
print()
print("x is lx: ", x is lx)
print("lx is lx: ", lx is lx)
print("lx is ly: ", lx is ly)
print("lx == ly: ", lx == ly)
print("lx[0] is ly[0]", lx[0] is ly[0])
print(x is lx[0])