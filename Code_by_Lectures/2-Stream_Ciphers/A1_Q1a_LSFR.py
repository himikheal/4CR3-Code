"""
General-purpose LFSR (Linear Feedback Shift Register) in Python

Usage conventions:
- State is stored as a list of bits (0/1).
- Taps can be indexed either from the LEFT (most-significant) or from the RIGHT (least-significant), depending on the chosen mode.
- When mode = 'left': index 0 = leftmost bit.
- When mode = 'right': index 0 = rightmost bit.

Features:
- Step the LFSR once, returning the output bit (0 or 1).
- Generate N bits of keystream as 0/1 values.
- Convert keystream to bytes.
- XOR with plaintext (bytes or binary string) for encryption/decryption.
"""

# left mode is whats in the slides

class LFSR:
    def __init__(self, initial_state, taps, tap_mode='left'):
        if isinstance(initial_state, str):
            state_list = []
            for ch in initial_state:
                if ch not in ('0', '1'):
                    raise ValueError('initial_state string must only contain "0" or "1"')
                state_list.append(int(ch))
        else:
            state_list = []
            for b in initial_state:
                if b not in (0, 1):
                    raise ValueError('initial_state iterable must contain 0/1 integers')
                state_list.append(int(b))

        if len(state_list) == 0:
            raise ValueError('initial_state must be non-empty')

        self.state = state_list
        self.n = len(self.state)

        if tap_mode not in ('left', 'right'):
            raise ValueError("tap_mode must be 'left' or 'right'")
        self.tap_mode = tap_mode

        taps_list = []
        for t in taps:
            if not isinstance(t, int):
                raise ValueError('taps must be integers')
            if t < 0 or t >= self.n:
                raise ValueError('tap position out of range: {}'.format(t))
            taps_list.append(t)
        self.taps = taps_list

    def _get_bit(self, pos):
        if self.tap_mode == 'left':
            return self.state[pos]
        else:
            return self.state[self.n - 1 - pos]

    def _shift_left_insert(self, bit):
        self.state.pop(0)
        self.state.append(int(bit))

    def step(self):
        feedback = 0
        i = 0
        while i < len(self.taps):
            t = self.taps[i]
            b = self._get_bit(t)
            feedback ^= b
            i += 1
        self._shift_left_insert(feedback)
        out_bit = int(self.state[-1])
        # print(self.state)
        return out_bit

    def generate_bits(self, count):
        if count < 0:
            raise ValueError('count must be non-negative')
        bits = list(self.state)
        i = 0
        while i < count:
            bits.append(self.step())
            i += 1
            # print(bits)
        return bits

    def generate_bytes(self, num_bytes):
        if num_bytes < 0:
            raise ValueError('num_bytes must be non-negative')
        bit_count = num_bytes * 8
        bits = self.generate_bits(bit_count)

        out = bytearray()
        i = 0
        while i < num_bytes:
            byte_val = 0
            j = 0
            while j < 8:
                bit = bits[i * 8 + j]
                byte_val = (byte_val << 1) | (bit & 1)
                j += 1
            out.append(byte_val)
            i += 1
        return bytes(out)


def xor_binary_plaintext(lfsr, plaintext_bits):
    if any(ch not in ('0','1') for ch in plaintext_bits):
        raise ValueError("plaintext_bits must only contain '0' and '1'")

    ks = lfsr.generate_bits(len(plaintext_bits))
    out = []
    i = 0
    while i < len(plaintext_bits):
        pt_bit = int(plaintext_bits[i])
        out_bit = pt_bit ^ ks[i]
        out.append(str(out_bit))
        i += 1
    return ''.join(out)


def xor_bytes_plaintext(lfsr, plaintext_bytes):
    keystream = lfsr.generate_bytes(len(plaintext_bytes))
    out = bytearray()
    i = 0
    while i < len(plaintext_bytes):
        out.append(plaintext_bytes[i] ^ keystream[i])
        i += 1
    return bytes(out)

def decrypt_binary_ciphertext(lfsr, ciphertext_bits):
    """
    Decrypts a binary string ciphertext using the given LFSR.
    Since XOR is symmetric, this is identical to encryption.
    """
    if any(ch not in ('0','1') for ch in ciphertext_bits):
        raise ValueError("ciphertext_bits must only contain '0' and '1'")
    
    ks = lfsr.generate_bits(len(ciphertext_bits))
    out = []
    i = 0
    while i < len(ciphertext_bits):
        ct_bit = int(ciphertext_bits[i])
        out_bit = ct_bit ^ ks[i]
        out.append(str(out_bit))
        i += 1
    return ''.join(out)


def decrypt_bytes_ciphertext(lfsr, ciphertext_bytes):
    """
    Decrypts a bytes ciphertext using the given LFSR.
    Since XOR is symmetric, this is identical to encryption.
    """
    keystream = lfsr.generate_bytes(len(ciphertext_bytes))
    out = bytearray()
    i = 0
    while i < len(ciphertext_bytes):
        out.append(ciphertext_bytes[i] ^ keystream[i])
        i += 1
    return bytes(out)


if __name__ == '__main__':
    # # Textbook example: 6-bit LFSR
    # initial_state = '011001'
    # taps = [0,1,3,5]
    # lfsr = LFSR(initial_state, taps, tap_mode='left')

    # # Generate 32 bits keystream matching textbook output
    # keystream = lfsr.generate_bits(26)
    # print('Keystream (bits):', ''.join(str(b) for b in keystream))

    # # Example plaintext (matching keystream length)
    # plaintext_bits = '01100100001001100100001001100100'
    # lfsr2 = LFSR(initial_state, taps, tap_mode='left')  # reinitialize to reset state
    # ciphertext_bits = xor_binary_plaintext(lfsr2, plaintext_bits)

    # print('Plaintext bits: ', plaintext_bits)
    # print('Ciphertext bits:', ciphertext_bits)

    # q1
    # initial_value = "00110110010101101111"
    # coef =[0,1,3,5,9,13,14,16,18] # tap positions   
    # lfsr3 = LFSR(initial_value, coef, tap_mode='left')

    # keystream2 = lfsr3.generate_bits(30) # number of bits to generate       
    # print('Alice\'s keystream:', ''.join(str(b) for b in keystream2))

    # plaintext2 = "00111101011100111000000111001100010011010110110100"
    # lfsr4 = LFSR(initial_value, coef, tap_mode='left')  # reinitialize to reset state
    # ciphertext2 = xor_binary_plaintext(lfsr4, plaintext2)
    # # print('Plaintext 2 bits: ', plaintext2)
    # print('Alice\'s ciphertext:', ciphertext2)

    # print('Bob\'s keystream:', ''.join(str(b) for b in keystream2))
    # lfsr5 = LFSR(initial_value, coef, tap_mode='left')
    # print('Bob\'s plaintext:', xor_binary_plaintext(lfsr5, ciphertext2))

    # q2
    # initial_value = "0010010100"
    # coef =[0,2,4]
    # lfsr3 = LFSR(initial_value, coef, tap_mode='left')

    # keystream2 = lfsr3.generate_bits(20) # number of bits to generate
    # print('keystream:', ''.join(str(b) for b in keystream2))
    
    initial_value = "01011"
    coef =[0,1,4]
    lfsr3 = LFSR(initial_value, coef, tap_mode='left')
    keystream2 = lfsr3.generate_bits(10) # number of bits to generate
    print('keystream:', ''.join(str(b) for b in keystream2))