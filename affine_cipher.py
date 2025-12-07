# JQJWF ZYPWPZGJW DC BJZWJG ZHEJB EJXHCBGWPGJB GYJ JBBJCZJ HO OWJRLJCZF PCPSFBDB. JQJWF SJGGJW JCGJWJE DC GYJ XJBBPTJ YJSMB EJGJZG GYJ YDEEJC MPGGJWCB.


def print_frequency_analysis(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    for char, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{char}: {freq}")


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def find_affine_keys(ciphertext):
    frequency = {}
    for char in ciphertext:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    most_frequent_char = max(frequency, key=frequency.get)

    # Assuming 'E' is the most frequent letter in English
    y = ord(most_frequent_char) - ord("A")
    x = ord("E") - ord("A")

    possible_keys = []
    for a in range(1, 26):
        if mod_inverse(a, 26) is not None:  # a must be coprime with 26
            b = (y - a * x) % 26
            possible_keys.append((a, b))

    return possible_keys


def find_all_affine_keys(ciphertext):
    possible_keys = []
    for a in range(1, 26):
        if mod_inverse(a, 26) is not None:  # a must be coprime with 26
            for b in range(26):
                possible_keys.append((a, b))
    return possible_keys


def decrypt_affine(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            offset = ord("A") if char.isupper() else ord("a")
            decrypted_char = chr((a_inv * ((ord(char) - offset) - b)) % 26 + offset)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return "".join(decrypted_text)


# ciphertext = "JQJWF ZYPWPZGJW DC BJZWJG ZHEJB EJXHCBGWPGJB GYJ JBBJCZJ HO OWJRLJCZF PCPSFBDB. JQJWF SJGGJW JCGJWJE DC GYJ XJBBPTJ YJSMB EJGJZG GYJ YDEEJC MPGGJWCB."
ciphertext = "RCLLA"
print("Frequency Analysis of the Ciphertext:")
print_frequency_analysis(ciphertext)
possible_keys = find_all_affine_keys(ciphertext)
for a, b in possible_keys:
    decrypted_message = decrypt_affine(ciphertext, a, b)
    print(f"Decrypted Message with keys (a={a}, b={b}):")
    print(decrypted_message)
