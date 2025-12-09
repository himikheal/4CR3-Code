import math
import time

# Input values
a = 1095369562025702556403033673059514719985657846060999038001272754193712036128714475110343472959833158083894277499580078770116751707887313066350958894258
m = 1486849462548131038391075744532018339748969593030811665429204557155898771386352512821463245755183336883785007564272951579651325540287779851348210497897

# --- (a) Euler’s theorem method ---
def mod_inverse_euler(a, m):
    """Compute modular inverse using Euler's theorem."""
    # Euler's totient φ(m) when m is prime is m-1
    # (if not prime, we'd compute phi(m) via factorization)
    return pow(a, m - 2, m)  # assuming m is prime

# --- (b) Extended Euclidean Algorithm method ---
def extended_gcd(a, b):
    """Return gcd, x, y such that ax + by = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

def mod_inverse_eea(a, m):
    """Compute modular inverse using Extended Euclidean Algorithm."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse does not exist since gcd(a, m) ≠ 1.")
    else:
        return x % m

# --- Measure performance ---
start = time.perf_counter()
inv_euler = mod_inverse_euler(a, m)
time_euler = (time.perf_counter() - start) * 1000  # in milliseconds

start = time.perf_counter()
inv_eea = mod_inverse_eea(a, m)
time_eea = (time.perf_counter() - start) * 1000  # in microseconds

# --- Output results ---
print("Modular inverse using Euler's theorem:")
print(inv_euler)
print(f"Time (Euler): {time_euler:.4f} ms\n")

print("Modular inverse using Extended Euclidean Algorithm:")
print(inv_eea)
print(f"Time (EEA): {time_eea:.4f} ms\n")

# Check equality
print("Results are equal:", inv_euler == inv_eea)
