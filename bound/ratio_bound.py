# R(s): upper bound for prod p/(p-1) over p_1<...<p_k from an admissible set Q,
# given (P): P_i >= 2^(2^(i-s)) for s <= i <= k-1.  p_i >= w_i = max(q_i, rho_i),
# rho_i = least m with m^i >= 2^(2^(i-s)) (since P_i <= p_i^i), p_k >= max(q_k, w_{k-1}+2).
import sympy, gmpy2, math
from fractions import Fraction
def rho(i, s):
    if i < s: return 1
    T = 1 << (1 << (i - s)) if i - s < 40 else None
    if T is None: return 10**40
    m = int(gmpy2.iroot(gmpy2.mpz(T), i)[0])
    if m ** i < T: m += 1
    return m
def R(s, Q, need):
    # returns True if the sup over k of the ratio bound is <= need
    prod = Fraction(1); best = Fraction(0); i = 1
    while True:
        q = Q[i - 1]
        w_last_prev = None
        # case k = i: p_k >= max(q_i, w_{i-1}+2)
        wk = max(q, (wprev + 2) if i > 1 else q)
        cand = prod * Fraction(wk, wk - 1)
        if cand > best: best = cand
        w = max(q, rho(i, s))
        if w > 10**30 and i > s + 3:
            best = max(best, prod * (1 + Fraction(16, w - 2)))
            return best
        prod *= Fraction(w, w - 1); wprev = w
        i += 1
# (b) 3 does not divide n, M >= 3: primes >= 5 (coprimality ignored)
Qb = list(sympy.primerange(5, 10**6))
s = 1
while float(R(s + 1, Qb, 3)) <= 3: s += 1
print("(b) M>=3, 3 !| n: largest s with R(s) <= 3:", s, float(R(s, Qb, 3)), float(R(s + 1, Qb, 3)))
# (a) 3 | n: admissible primes 3 and p = 2 mod 3, M >= 4
Qa = [3] + [p for p in sympy.primerange(5, 2 * 10**6) if p % 3 == 2]
lo, hi = 1000, 1600
while hi - lo > 1:
    mid = (lo + hi) // 2
    if R(mid, Qa, 4) <= 4: lo = mid
    else: hi = mid
print("(a) 3 | n: largest s with R(s) <= 4:", lo, float(R(lo, Qa, 4)), float(R(lo + 1, Qa, 4)))
