
def driver(pep):
    n= len(pep)
    prefixMass = [0]
    for i in range(0, n):
        prefixMass.append(prefixMass[i]+aminoMass(pep[i]))
    linearSpectrum = [0]
    for i in range(0,n):
        for j in range(i+1, n+1):
            linearSpectrum.append(prefixMass[j] - prefixMass[i])
        linearSpectrum.sort()
    s = ''
    for i in linearSpectrum:
        s = s + ' ' + str(i)
    print(s)

def aminoMass(a):
    mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113,
            'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131,
            'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
    return mass[a]

driver("NLYV")