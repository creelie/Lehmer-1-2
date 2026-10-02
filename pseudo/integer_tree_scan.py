#!/usr/bin/env python3
"""Theorem 8.3 (i) for k = 13: no odd integers 5 <= x_1 < ... < x_k, none divisible by 3, prime or not, satisfy
    x_1 ... x_k + eps = 2 (x_1 - 1) ... (x_k - 1).

The tree down to depth k - 3 is that of integer_tree.py (depth_k3_nodes).  At depth k - 3 the admissible values of
x_{k-2} in the interval of each node are passed to the program scan3 of ../companion8 in mode 1 (odd integers prime
to 3, with x != 0 mod the odd primes of the earlier x_i - 1 and x != 1 mod the primes of the earlier x_i), which finds
every completion (x, p, q) in integers prime to 3 by trial division and by the sum of the two factors, and passes the
values of x for which this would be slow to PARI/GP, which factors N completely, proves every prime factor prime and
lists the divisors of N in the class (factor_class.gp).  The intervals are cut into pieces, and a journal records each
finished batch of pieces, so that an interrupted run resumes where it stopped.

usage:  integer_tree_scan.py k eps [workers] [journal]
output: a report on stdout; the journal in data/pseudo/integer_tree_k{k}_{m1|p1}.jsonl"""
import sys, os, json, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "companion8"))
import integer_tree as IT
from tail3lib import odd_primes_of
from common import build, run_scan3, run_gp, check_completion

WIDTH = 2 * 10 ** 8          # integers x per piece (about 1.7e7 admissible values, some 20 s)
EPS = None


def line1(eps, xs, lo, hi):
    R0 = odd_primes_of([x - 1 for x in xs]); R1 = odd_primes_of(list(xs))
    return (f"{eps} 1 {len(xs)} {' '.join(map(str, xs))} {lo} {hi} {len(R0)} {' '.join(map(str, R0))} "
            f"{len(R1)} {' '.join(map(str, R1))}")


def key(p): return f"{','.join(map(str, p[0]))}:{p[1]}-{p[2]}"


def pieces(k, eps):
    nodes, visited = IT.depth_k3_nodes(k, eps)
    ps = []
    for xs, lo, hi in nodes:
        a = lo
        while a <= hi:
            b = min(hi, a + WIDTH - 1); ps.append((list(xs), a, b)); a = b + 1
    batches = []; cur = []; w = 0
    for p in sorted(ps, key=lambda p: -(p[2] - p[1])):
        cur.append(p); w += p[2] - p[1] + 1
        if w >= WIDTH: batches.append(cur); cur = []; w = 0
    if cur: batches.append(cur)
    return nodes, visited, batches


def work(batch):
    t0 = time.time()
    tot, comps, defs = run_scan3([line1(EPS, *p) for p in batch])
    t1 = time.time()
    g, dmax, gsec = run_gp(defs, EPS)
    # completions found by factoring may have p or q divisible by 3; keep those prime to 3, as scan3 does
    allc = sorted({tuple(c) for c in comps} | {tuple(c[:-2]) for c in g if c[-3] % 3 and c[-4] % 3})
    for c in allc: assert check_completion(c, EPS), c
    return dict(keys=[key(p) for p in batch], nx=int(tot["nx"]), nempty=int(tot["nempty"]), ntd=tot["ntd"],
                nsig=tot["nsig"], nsurv=int(tot["nsurv"]), ndef=len(defs), dmax=dmax, scan_sec=round(t1 - t0, 2),
                gp_sec=round(gsec, 2), completions=[list(c) for c in allc])


def main():
    global EPS
    k = int(sys.argv[1]); EPS = int(sys.argv[2])
    W = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    jpath = sys.argv[4] if len(sys.argv) > 4 else os.path.join(
        ROOT, "data", "pseudo", f"integer_tree_k{k}_{'m1' if EPS < 0 else 'p1'}.jsonl")
    os.makedirs(os.path.dirname(jpath), exist_ok=True)
    build(); t0 = time.time()
    nodes, visited, batches = pieces(k, EPS)
    width = sum(hi - lo + 1 for xs, lo, hi in nodes)
    print(f"k = {k}, eps = {EPS:+d}: {visited} nodes visited, {len(nodes)} nodes at depth {k - 3}, total width of "
          f"the intervals for x_{k - 2} {width}, {len(batches)} batches", flush=True)
    done = set()
    if os.path.exists(jpath):
        for l in open(jpath):
            if l.strip(): done.update(json.loads(l)["keys"])
    todo = [b for b in batches if not all(key(p) in done for p in b)]
    print(f"{len(batches) - len(todo)} batches already in the journal, {len(todo)} to do", flush=True)
    with Pool(W) as P, open(jpath, "a") as J:
        for i, r in enumerate(P.imap_unordered(work, todo)):
            J.write(json.dumps(r) + "\n"); J.flush()
            if i % 50 == 0 or i == len(todo) - 1:
                print(f"  {i + 1}/{len(todo)} batches, {time.time() - t0:.0f}s", flush=True)
    tot = dict(nx=0, nempty=0, ntd=0.0, nsig=0.0, nsurv=0, ndef=0, scan_sec=0.0, gp_sec=0.0); dmax = 0
    comps = set(); seen = set()
    for l in open(jpath):
        if not l.strip(): continue
        r = json.loads(l)
        if any(x in seen for x in r["keys"]): continue
        seen.update(r["keys"])
        for x in tot: tot[x] += r[x]
        dmax = max(dmax, r["dmax"]); comps |= {tuple(c) for c in r["completions"]}
    allkeys = {key(p) for b in batches for p in b}
    missing = allkeys - seen
    print(f"pieces treated {len(seen & allkeys)} of {len(allkeys)}" + (f"; MISSING {len(missing)}" if missing else ""))
    print(f"admissible x_{k - 2} {tot['nx']}; trial divisions {tot['ntd']:.4e}, values of the sum {tot['nsig']:.4e}, "
          f"candidates tested exactly {tot['nsurv']}; x treated by factoring N {tot['ndef']} (N up to {dmax} digits)")
    print(f"processor time: scan3 {tot['scan_sec'] / 3600:.2f} h, PARI/GP {tot['gp_sec'] / 3600:.2f} h")
    print(f"completions in odd integers prime to 3: {len(comps)}")
    for c in sorted(comps): print("   COMPLETION", c)
    print(f"wall {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
