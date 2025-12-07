def sigma0(num: int):
    num = _rotate_right(num, 17) ^ _rotate_right(num, 11) ^ (num >> 13)
    return num


def sigma1(num: int):
    num = _rotate_right(num, 7) ^ _rotate_right(num, 9) ^ (num >> 12)
    return num


def capsigma0(num: int):
    num = _rotate_right(num, 2) ^ _rotate_right(num, 23) ^ _rotate_right(num, 12)
    return num


def capsigma1(num: int):
    num = _rotate_right(num, 16) ^ _rotate_right(num, 21) ^ _rotate_right(num, 15)
    return num


def choose(x: int, y: int, z: int):
    return (x & y) ^ (x & z)


def majority(x: int, y: int, z: int):
    return (x & y) ^ (x & ~z) ^ (y & z)


def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)


def generate_hash(
    byteString: bytes = b"The quick brown fox jumped over the lazy dog.",
) -> bytes:
    data = bytearray(byteString)

    # Initialize hash values
    h0 = 0x6A09E667
    h1 = 0xBB67AE85
    h2 = 0x3C6EF372
    h3 = 0xA54FF53A
    h4 = 0x510E527F
    h5 = 0x9B05688C
    h6 = 0x1F83D9AB
    h7 = 0x5BE0CD19

    K = [
        0x428A2F98,
        0x71374491,
        0xB5C0FBCF,
        0xE9B5DBA5,
        0x3956C25B,
        0x59F111F1,
        0x923F82A4,
        0xAB1C5ED5,
        0xD807AA98,
        0x12835B01,
        0x243185BE,
        0x550C7DC3,
        0x72BE5D74,
        0x80DEB1FE,
        0x9BDC06A7,
        0xC19BF174,
        0xE49B69C1,
        0xEFBE4786,
        0x0FC19DC6,
        0x240CA1CC,
        0x2DE92C6F,
        0x4A7484AA,
        0x5CB0A9DC,
        0x76F988DA,
        0x983E5152,
        0xA831C66D,
        0xB00327C8,
        0xBF597FC7,
        0xC6E00BF3,
        0xD5A79147,
        0x06CA6351,
        0x14292967,
        0x27B70A85,
        0x2E1B2138,
        0x4D2C6DFC,
        0x53380D13,
        0x650A7354,
        0x766A0ABB,
        0x81C2C92E,
        0x92722C85,
        0xA2BFE8A1,
        0xA81A664B,
        0xC24B8B70,
        0xC76C51A3,
        0xD192E819,
        0xD6990624,
        0xF40E3585,
        0x106AA070,
        0x19A4C116,
        0x1E376C08,
        0x2748774C,
        0x34B0BCB5,
        0x391C0CB3,
        0x4ED8AA4A,
        0x5B9CCA4F,
        0x682E6FF3,
        0x748F82EE,
        0x78A5636F,
        0x84C87814,
        0x8CC70208,
        0x90BEFFFA,
        0xA4506CEB,
        0xBEF9A3F7,
        0xC67178F2,
    ]

    # Padding the data
    data.append(0x80)
    while (len(data) * 8) % 512 != 448:
        data.append(0x00)

    # Append the length of the original message as a 64-bit big-endian integer
    data += (len(byteString) * 8).to_bytes(8, byteorder="big")

    # Split data into 512-bit chunks
    blocks = []
    for i in range(0, len(data), 64):
        blocks.append(data[i : i + 64])

    # Process each block
    for block in blocks:
        message_schedule = []
        for j in range(0, 64):
            if j < 16:
                word = block[j * 4 : (j * 4) + 4]
                message_schedule.append(word)
            else:
                s0 = sigma0(int.from_bytes(message_schedule[j - 15], byteorder="big"))
                s1 = sigma1(int.from_bytes(message_schedule[j - 2], byteorder="big"))
                word = (
                    (
                        int.from_bytes(message_schedule[j - 16], byteorder="big")
                        + s0
                        + int.from_bytes(message_schedule[j - 7], byteorder="big")
                        + s1
                    )
                    % (2**32)
                ).to_bytes(4, byteorder="big")
                message_schedule.append(word)

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    # Compression function main loop
    for i in range(64):
        S1 = capsigma1(e)
        ch = choose(e, f, g)
        temp1 = (
            h + S1 + ch + K[i] + int.from_bytes(message_schedule[i], byteorder="big")
        ) % (2**32)
        S0 = capsigma0(a)
        maj = majority(a, b, c)
        temp2 = (S0 + maj) % (2**32)
        h = g
        g = f
        f = e
        e = (d + temp1) % (2**32)
        d = c
        c = b
        b = a
        a = (temp1 + temp2) % (2**32)

    # Add the compressed chunk to the current hash value
    h0 = (h0 + a) % (2**32)
    h1 = (h1 + b) % (2**32)
    h2 = (h2 + c) % (2**32)
    h3 = (h3 + d) % (2**32)
    h4 = (h4 + e) % (2**32)
    h5 = (h5 + f) % (2**32)
    h6 = (h6 + g) % (2**32)
    h7 = (h7 + h) % (2**32)

    ret = "".join(format(x, "02x") for x in [h0, h1, h2, h3, h4, h5, h6, h7])
    return ret


print("Hash for 'The quick brown fox jumped over the lazy dog.':")
print(generate_hash(b"The quick brown fox jumped over the lazy dog."))
