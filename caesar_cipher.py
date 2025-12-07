# Assuming the letter "E" is the most frequent in the english language, decrypt the following ciphertext from the Caesar Cipher.
# MDMZ GFMZAMZQMV QV AMKZMB KWLMU LMWVBABZMABM BPM MAAUMKM WN NZMYYCVMG IZTMQAQA. MDMZ TMBBMZ MVBZMZM QV BPM UMUUIOM PMTXA LMUMKB BPM PQLLMV XI BBMZVA.

def print_frequency_analysis(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    for char, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{char}: {freq}")

def find_shift(ciphertext):
    # Frequency analysis to find the most common letter in the ciphertext
    frequency = {}
    for char in ciphertext:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    most_frequent_char = max(frequency, key=frequency.get)
    
    # Assuming 'E' is the most frequent letter in English
    shift = (ord(most_frequent_char) - ord('E')) % 26
    return shift

def decrypt_caesar(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

ciphertext = "MDMZ GFMZAMZQMV QV AMKZMB KWLMU LMWVBABZMABM BPM MAAUMKM WN NZMYYCVMG IZTMQAQA. MDMZ TMBBMZ MVBZMZM QV BPM UMUUIOM PMTXA LMUMKB BPM PQLLMV XI BBMZVA."
# print("Frequency Analysis of the Ciphertext:")
# print_frequency_analysis(ciphertext)
shift = find_shift(ciphertext)
decrypted_message = decrypt_caesar(ciphertext, shift)
print("Decrypted Message:")
print(decrypted_message)

# EVERY CHARACTER IN SECRET CODES DEMONSTRATES THE ESSENCE OF FREQUENCY ANALYSIS.
# EVERY LETTER ENTERED IN THE MESSAGE HELPS DETECT THE HIDDEN PATTERNS

for i in range(26):
    print(f"Shift {i}: {decrypt_caesar("GFMZAMZQMV", i)}")