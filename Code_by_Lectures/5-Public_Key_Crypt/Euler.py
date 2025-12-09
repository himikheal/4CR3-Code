def gcd(a, b):
    """Euclidean gcd."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def phi_with_trace(n):
    """Compute phi(n) with detailed factorization trace."""
    trace = []
    trace.append(f"Computing phi({n})")

    result = n
    x = n
    p = 2

    # factor 2
    if x % p == 0:
        trace.append("Factor 2 divides n")
        count = 0
        while x % p == 0:
            x //= p
            count += 1
        trace.append(f"  2^{count} extracted")
        result = result // p * (p - 1)

    # other primes
    p = 3
    while p * p <= x:
        if x % p == 0:
            trace.append(f"Factor {p} divides n")
            count = 0
            while x % p == 0:
                x //= p
                count += 1
            trace.append(f"  {p}^{count} extracted")
            result = result // p * (p - 1)
        p += 2

    # last prime > 1
    if x > 1:
        trace.append(f"Remaining factor is prime: {x}")
        result = result // x * (x - 1)

    trace.append(f"Final phi({n}) = {result}")
    return result, trace


def powmod_with_trace(base, exponent, modulus):
    """Fast modular exponentiation with step-by-step trace."""
    trace = []
    trace.append(f"Computing {base}^{exponent} mod {modulus}")

    result = 1 % modulus
    base = base % modulus
    e = exponent

    step = 0
    while e > 0:
        trace.append(f"Step {step}: result={result}, base={base}, exponent={e}")
        if e & 1:
            result = (result * base) % modulus
            trace.append(f"  exponent is odd -> multiply result -> {result}")
        base = (base * base) % modulus
        e >>= 1
        step += 1

    trace.append(f"Final result of modular exponentiation = {result}")
    return result, trace


def euler_theorem_trace(a, n):
    """Check Euler's theorem and return complete reasoning trace."""
    full_trace = []
    full_trace.append(f"Checking Euler's theorem for a={a}, n={n}")

    g = gcd(a, n)
    full_trace.append(f"gcd(a, n) = {g}")

    if g != 1:
        full_trace.append("Since gcd ≠ 1, Euler's theorem does NOT apply.")
        return False, None, full_trace

    # phi(n) with trace
    ph, trace_phi = phi_with_trace(n)
    for line in trace_phi:
        full_trace.append(line)

    # compute a^phi(n) mod n with trace
    lhs, trace_pow = powmod_with_trace(a, ph, n)
    for line in trace_pow:
        full_trace.append(line)

    # final statement
    if lhs == 1 % n:
        full_trace.append("Euler's theorem holds: a^phi(n) === 1 (mod n).")
        return True, lhs, full_trace
    else:
        full_trace.append("Euler's theorem FAILS (unexpected).")
        return False, lhs, full_trace


# Example usage:
if __name__ == "__main__":
    a = 3
    n = 10
    holds, value, trace = euler_theorem_trace(a, n)

    print("\n".join(trace))
