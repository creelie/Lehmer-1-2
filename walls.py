#!/usr/bin/env python3
"""Section 7 of the paper: the next cases.  (a) n - 1 = 2 phi(n), k = 15, p_1 >= 5: the nodes at depth 12 and the widths of
the intervals for p_13.  (b) n + 1 = 2 phi(n), k = 8, p_1 >= 3: the nodes at depth 5 and the widths of the
intervals for p_6.  Also the per-depth node counts for k = 7..14 used in Figure 2.  Runtime: about a minute."""
import sys, time, math, collections
sys.path.insert(0, ".")
from fractions import Fraction as Fr
from tree_search import Search
from sympy import primerange

def frontier(k, pmin, eps, stop_m):
    S = Search(k, 2, 1, pmin=pmin, eps=eps); out = []; prof = collections.Counter()
    def dfs(chosen, P, A, B):
        j = len(chosen); m = k - j; prof[j] += 1
        if P >= S.mu: return
        if m == stop_m: pass
        T = S.mu / P; pj = chosen[-1] if chosen else 1
        hi, lo = S.bounds(T, P, B, pj, m); lo = max(lo, pj + 1, pmin)
        if hi < lo: return
        if m == stop_m:
            out.append((hi - lo, tuple(chosen), float(T - 1))); return
        for p in primerange(lo, hi + 1):
            if S.ok_prime(p, chosen): dfs(chosen + [p], P * Fr(p, p - 1), A * p, B * (p - 1))
    dfs([], Fr(1), 1, 1)
    return sorted(out, key=lambda x: -x[0]), [prof[j] for j in range(k - stop_m + 1)]

def report(name, rows):
    w = [x[0] for x in rows]
    print(f"{name}: frontier nodes={len(rows)}, total width={sum(w):.3e}, "
          f"<1e3: {sum(x < 10**3 for x in w)}, 1e3..1e6: {sum(10**3 <= x <= 10**6 for x in w)}, "
          f">1e6: {sum(x > 10**6 for x in w)}, >1e7: {sum(x > 10**7 for x in w)}")
    for x in rows[:6]: print(f"   width={x[0]}  prefix={list(x[1])}  T-1={x[2]:.3e}")

t0 = time.time()
rows, _ = frontier(15, 5, -1, 3); report("n - 1 = 2 phi(n), k = 15, depth 12", rows)
rows, _ = frontier(8, 3, +1, 3); report("n + 1 = 2 phi(n), k = 8, depth 5", rows)
for eps in (-1, +1):
    for k in range(7, 15):
        _, prof = frontier(k, 5, eps, 2)
        print(f"profile eps={eps:+d} k={k:2d}: {prof}")
print(f"({time.time()-t0:.0f}s)")
