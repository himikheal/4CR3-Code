def square_and_multiply(a, e, n):
    """
    Computes a^e mod n using the Square-and-Multiply algorithm.
    """
    result = 1
    base = a % n

    # Process exponent bits from MSB to LSB
    for bit in bin(e)[2:]:
        # Square step
        result = (result * result) % n

        # Multiply step (only if bit is 1)
        if bit == '1':
            result = (result * base) % n

    return result


print(square_and_multiply(7, 128, 13))
