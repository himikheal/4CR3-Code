def generate(initial, coefficients, n, log=False):
    # ret = initial value
    # bits = initial value in bits
    ret = initial
    bits = [int(bit) for bit in initial]
    print(bits)
    coeff = [int(bit) for bit in coefficients]
    print(coeff)
    new = 0

    for i in range(n):
        new = 0
        # new = indices of bits, indexed by coefficients
        
        for i in range(len(coefficients)):
            if coeff[i] == 1:
                new += bits[i]
        new = new % 2
        ret = ret + str(new)
        if log:
            print(
                "a"
                + str(20 + i)
                + "= a"
                + str(0 + i)
                + " + a"
                + str(1 + i)
                + " + a"
                + str(3 + i)
                + " + a"
                + str(5 + i)
                + " + a"
                + str(9 + i)
                + " + a"
                + str(13 + i)
                + " + a"
                + str(14 + i)
                + " + a"
                + str(16 + i)
                + " + a"
                + str(18 + i)
                + " (mod 2)"
            )
            print(
                "a" + str(20 + i) + "=",
                bits[0],
                "+",
                bits[1],
                "+",
                bits[3],
                "+",
                bits[5],
                "+",
                bits[9],
                "+",
                bits[13],
                "+",
                bits[14],
                "+",
                bits[16],
                "+",
                bits[18],
                "(mod 2) =",
                new,
            )
        bits = bits[1:] + [new]

    return ret

print("Generated Key Bits:")
print(generate("0010010100", "1010100000", 10, False))

# 0010010100 1110001001
# initial
# 0010010100
# coeff
# 1010100000

# 1110001001

# 0010010100
# 0+1+0 = 1
# 0100101001
# 0+0+1 = 1
# 1001010011
# 1+0+0 = 1
# 0010100111
# 0+1+1 = 0
# 0101001110
# 0+0+0 = 0
# 1010011100
# 1+1+0 = 0
# 0100111000
# 0+0+1 = 1
# 1001110001
# 1+0+1 = 0
# 0011100010
# 1+0+1 = 0
# 0111000100
# 0+1+0 = 1

def generateHARD(n, log=False):
    ret = "0010010100"
    bits = [0,0,1,0,0,1,0,1,0,0]
    # print(bits)
    for i in range(n):
        new = (
            bits[0]
            + bits[2]
            + bits[4]
        )
        new = new % 2
        ret = ret + str(new)
        bits = bits[1:] + [new]

    return ret

print(generateHARD(10, False))