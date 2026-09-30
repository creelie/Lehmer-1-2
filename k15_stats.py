#!/usr/bin/env python3
"""Statistics for the paper (Sections 5 and 8).

(a) For every one of the 33,865,004 pairs (prefix of 12 primes, admissible p_13 = s) of the case k = 15:
    the modulus c = 2B' - A' and N = 2A'B' - c of the two-prime problem, and a histogram of log10(c^3/N).
    When c^3 > N the divisors of N in a residue class modulo c number at most 11 (Lenstra) and the lattice
    method needs only a few boxes; the factored instances sit in the far left tail.
(b) The totals of the runs recorded in data/k15/run_*.jsonl (for program C, 'tested' counts square tests and
    'direct' trial divisions).
(c) The frontier at depth 12 for k = 16 (four primes still to choose): number of prefixes and the widths of
    the intervals for p_13, and a first-order count of the pairs (p_13, p_14) that the three-prime completion
    would have to treat.
Output: data/k15/stats.json.  Runtime: a few minutes."""
import sys, os, json, math, gzip, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lastthree as L

out = {}
fr = json.load(open("data/k15/frontier.json"))
hist = collections.Counter(); ns = 0; lenstra = 0; minlog = 1e9
for chosen, lo, hi in fr:
    chosen = tuple(chosen)
    A = 1; B = 1
    for p in chosen: A *= p; B *= p - 1
    C = 2 * B - A
    ss = L.primes_in(lo, hi); ss = ss[L.admissible_mask(ss, chosen)]
    if len(ss) == 0: continue
    s_first = -((-2 * B) // C)                      # least integer with C s - 2B >= 0
    rho0 = C * s_first - 2 * B                      # exact, 0 <= rho0 < C
    d = (ss - s_first).astype(np.float64)
    c = d * float(C) + float(rho0)                  # c = C s - 2B, without cancellation
    assert np.all(c > 0)
    logN = math.log10(2 * A * B) + np.log10(ss.astype(np.float64)) + np.log10(ss.astype(np.float64) - 1)
    x = 3 * np.log10(c) - logN
    ns += len(ss); lenstra += int(np.sum(x > 0)); minlog = min(minlog, float(x.min()))
    for b, k in zip(*np.unique(np.floor(x).astype(int), return_counts=True)): hist[int(b)] += int(k)
out["k15_pairs"] = ns
out["k15_lenstra_regime"] = lenstra
out["k15_min_log10_c3_over_N"] = minlog
out["k15_hist_log10_c3_over_N"] = dict(sorted(hist.items()))
print(f"(a) {ns} pairs; c^3 > N for {lenstra}; min log10(c^3/N) = {minlog:.2f}")
print("    histogram of floor(log10(c^3/N)):", dict(sorted(hist.items())))

runs = {}
for name in ("run_A", "run_A_plus", "run_B", "run_B_plus", "run_C", "run_C_plus"):
    path = f"data/k15/{name}.jsonl"
    if os.path.exists(path): f = open(path)
    elif os.path.exists(path + ".gz"): f = gzip.open(path + ".gz", "rt")     # archived runs are gzipped
    else: continue
    rows = [json.loads(l) for l in f]
    keys = ("n_s", "boxes", "tested", "direct", "factored", "found", "sec")
    tot = {k: sum(r.get(k, 0) for r in rows) for k in keys}
    tot["tasks"] = len({tuple(r["task"]) for r in rows}); tot["sols"] = sum(len(r["sols"]) for r in rows)
    tot["cands"] = sum(len(r["cands"]) for r in rows)
    runs[name] = tot
    print(f"(b) {name}: {tot}")
out["runs"] = runs

fr16 = L.frontier(16, 5, 2, 1, -1, 4)
w16 = [hi - lo for c, A, B, lo, hi in fr16]
h16 = collections.Counter(int(math.floor(math.log10(w))) if w > 0 else 0 for w in w16)
est = 0.0; top = []
for c, A, B, lo, hi in fr16:
    delta = (2 * B - A) / A
    s = 0.0; K = 2000
    for i in range(K):                 # sum over p_13 = x of (number of primes p_14) ~ (2/d13) / log(1/d13)
        x = lo + (hi - lo + 1) * (i + 0.5) / K
        d13 = (1 + delta) * (x - 1) / x - 1
        if d13 > 0: s += (2 / d13) / math.log(2 / d13 + 3) / math.log(x) * (hi - lo + 1) / K
    est += s; top.append((s, list(c), hi - lo))
top.sort(reverse=True)
out["k16_depth12_nodes"] = len(fr16); out["k16_total_width"] = sum(w16)
out["k16_hist_log10_width"] = dict(sorted(h16.items())); out["k16_estimated_pairs"] = est
out["k16_top"] = top[:5]
print(f"(c) k=16: {len(fr16)} nodes at depth 12, total width {sum(w16):.3e}, estimated pairs {est:.2e}")
print("    histogram of floor(log10(width)):", dict(sorted(h16.items())))
json.dump(out, open("data/k15/stats.json", "w"), indent=1)
