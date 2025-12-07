# initial value = 00110110010101101111
# coefficients = 11010100010001101010

# bits = [0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1]


def generate(n, log=False):
    ret = "00110110010101101111"
    bits = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    # print(bits)
    for i in range(n):
        new = (
            bits[0]
            + bits[1]
            + bits[3]
            + bits[5]
            + bits[9]
            + bits[13]
            + bits[14]
            + bits[16]
            + bits[18]
        )
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


def encrypt(generated, plaintext, log=False):
    ciphertext = ""
    for i in range(len(plaintext)):
        bit = int(generated[i]) ^ int(plaintext[i])
        ciphertext += str(bit)
        if log:
            print(
                "bit "
                + str(i)
                + " of ciphertext = "
                + generated[i]
                + " XOR "
                + plaintext[i]
                + " = "
                + str(bit)
            )

    return ciphertext


# Generated Key Bits
print("Generated Key Bits:")
print(generate(30, False))
# Alice xor's generated key bits with plain text
print("Ciphertext")
print(
    encrypt(generate(30), "00111101011100111000000111001100010011010110110100", False)
)
# Bob xor's generated key bits with cipher text
print("Decrypted Plaintext")
print(
    encrypt(
        generate(30),
        encrypt(generate(30), "00111101011100111000000111001100010011010110110100"),
        False,
    )
)
print(
    encrypt(generate(30), "00001011001001010111111101111011100100110010111001", False)
)

# 00110110010101101111111010110111110111100100001101
# 00111101011100111000000111001100010011010110110100
# manual xor
# 00001011001001010111111101111011100100110010111001
# code output
# 00001011001001010111111101111011100100110010111001


# 1b
# inital value = 00110110010101101111
# s20 = s0p0 + s1p1 + s2p2 + ... + s19p19 (mod 2)
# s20 = s0p0 + s1p1 + s2p2 + s3p3 + s4p4 + s5p5 + s6p6 + s7p7 + s8p8 + s9p9 + s10p10 + s11p11 + s12p12 + s13p13 + s14p14 + s15p15 + s16p16 + s17p17 + s18p18 + s19p19
# s20 = 0(p0) + 0(p1) + 1(p2) + 1(p3) + 0(p4) + 1(p5) + 1(p6) + 0(p7) + 0(p8) + 1(p9) + 0(p10) + 1(p11) + 0(p12) + 1(p13) + 1(p14) + 0(p15) + 1(p16) + 1(p17) + 1(p18) + 1(p19) (mod 2)
# s20 = p2 + p3 + p5 + p6 + p9 + p11 + p13 + p14 + p16 + p17 + p18 + p19 (mod 2)


# s21 = 0(p0) + 0(p1) + 1(p2) + 1(p3) + 0(p4) + 1(p5) + 1(p6) + 0(p7) + 0(p8) + 1(p9) + 0(p10) + 1(p11) + 0(p12) + 1(p13) + 1(p14) + 0(p15) + 1(p16) + 1(p17) + 1(p18) + 1(p19) (mod 2)


def create_linear_equations(
    n, log_full=False, log_subbed=False, log_reduced=True, matrix_form=True
):
    bits = generate(50)
    print(bits)
    equations = []
    for i in range(n):
        if log_full:
            print(
                "s"
                + str(20 + i)
                + " = s"
                + str(0 + i)
                + "p0 + s"
                + str(1 + i)
                + "p1 + s"
                + str(2 + i)
                + "p2 + s"
                + str(3 + i)
                + "p3 + s"
                + str(4 + i)
                + "p4 + s"
                + str(5 + i)
                + "p5 + s"
                + str(6 + i)
                + "p6 + s"
                + str(7 + i)
                + "p7 + s"
                + str(8 + i)
                + "p8 + s"
                + str(9 + i)
                + "p9 + s"
                + str(10 + i)
                + "p10 + s"
                + str(11 + i)
                + "p11 + s"
                + str(12 + i)
                + "p12 + s"
                + str(13 + i)
                + "p13 + s"
                + str(14 + i)
                + "p14 + s"
                + str(15 + i)
                + "p15 + s"
                + str(16 + i)
                + "p16 + s"
                + str(17 + i)
                + "p17 + s"
                + str(18 + i)
                + "p18 + s"
                + str(19 + i)
                + "p19 (mod 2)"
            )
        if log_subbed:
            equation = "s" + str(20 + i) + " = "
            for j in range(20):
                if bits[i + j] == "1":
                    if j == 0:
                        equation += "1(p" + str(j) + ")"
                    else:
                        equation += " + 1(p" + str(j) + ")"
                elif bits[i + j] == "0":
                    if j == 0:
                        equation += "0(p" + str(j) + ")"
                    else:
                        equation += " + 0(p" + str(j) + ")"
            print(equation + " (mod 2)")

        if log_reduced:
            reduced = "s" + str(20 + i) + " = " + bits[20 + i] + " = "
            for j in range(20):
                if bits[i + j] == "1":
                    if reduced == "s" + str(20 + i) + " = " + bits[20 + i] + " = ":
                        reduced += "p" + str(j)
                    else:
                        reduced += " + p" + str(j)
            print(reduced + " (mod 2)")

        if matrix_form:
            row = ""
            for j in range(20):
                if bits[i + j] == "1":
                    if j == 0:
                        row += "1"
                    else:
                        row += " 1"
                elif bits[i + j] == "0":
                    if j == 0:
                        row += "0"
                    else:
                        row += " 0"            
            print(row, bits[20 + i])
            # if i < 10:
                # print("s" + str(i) + " ", row + " = " + bits[20 + i])
            # else:
                # print("s" + str(i), row + " = " + bits[20 + i])
            # print("s" + (str(i) if (i < 10) else (str(i) + " ")), row)


create_linear_equations(40, False, False, False, True)
