# Lehmer's totient problem with fewer than sixteen prime factors

Code, data and Lean proofs for the paper

> D. Bhattacharjee, P. Mandal, U. Bhattacharya,
> *Lehmer's totient problem with fewer than sixteen prime factors*.

What the computations establish (see the paper for the proofs they complete):

1. Every composite n with φ(n) | n−1 has at least 16 distinct prime factors.
2. The solutions of φ(n) | n+1 with at most 7 prime factors are exactly
   1, 2, 3, 15, 255, 65535, 83623935, 4294967295, 6992962672132095.
3. Every solution of φ(n) | n+1 with n > 3 and 3 ∤ n has at least 16 distinct prime factors.
4. Every solution of φ(n) | n+1 with n > 3 and (n+1)/φ(n) ≥ 3 has at least 33 prime factors (1540 if 3 | n).
5. The Fermat-type solutions (n+1 = 2φ(n)) are exactly the closure of 1 under one- and two-prime extensions.
6. Every Fermat-type n₀ = p₁⋯p_m gives a pseudo-solution (p₁, …, p_m, n₀) of x₁⋯x_k − 1 = 2∏(xᵢ − 1) that passes
   the congruence prune, so a proof for all k has to use the primality of the factors.
7. These pseudo-solutions have two entries divisible by 3. No solution of x₁⋯x_k ± 1 = 2∏(xᵢ − 1) in odd integers
   prime to 3 exists for k ≤ 12, nor for k ≤ 15 when x₁, …, x_{k−3} are prime (`pseudo/`). The number of entries
   divisible by 3 is even for the sign −1 and odd or zero for +1, and Lemma 2.2 is the only congruence obstruction to
   completing a prefix.

The lemmas and propositions behind 1–3 and 7, and statements 4, 5 and 6 in full, are proved in Lean 4 in `lean/`
(see `lean/README.md`). The exhaustive searches are checked by independent programs, not formalised.

Neither Lehmer's totient conjecture nor the question whether φ(n) | n+1 has further solutions is settled.

## Requirements

Python 3.8 or later with `sympy` (tested with Python 3.11 and sympy 1.14). `sieve_check.py` also needs `numpy`
and about 2 GB of memory. The fifteen-prime programs (`lastthree.py`, `lastthree_b.py`, `lastthree_c.py`, `k15_run.py`,
`k15_stats.py` and the scripts in `tests/`) need `numpy`, `gmpy2` and `python-flint` (tested with numpy 2.4,
gmpy2 2.3 and python-flint 0.9, which bundles FLINT 3.6).

**Primality tests.** Without `gmpy2`, SymPy's `isprime` is a strong probable-prime test to the first thirteen
prime bases below 3.3·10^24, which is a proof there (Sorenson and Webster), and a Baillie–PSW test above.
With `gmpy2` installed, SymPy applies Baillie–PSW at every size. The recorded runs of the scripts for k ≤ 14
were made without `gmpy2`. This matters only for the statement that the factorisations of D below 10^25 used
by `tree_search.py` are certified; the enumeration-only program `tree_enum.py` relies on no primality proof.
To reproduce that statement, run the k ≤ 14 scripts in an environment without `gmpy2`. The fifteen-prime
programs do not use SymPy's test: every prime factor that the lattice programs rely on is proved prime, by the
thirteen-base test below 3.3·10^24 and by FLINT's primality prover above, and the sum route (`lastthree_c.py`)
factors nothing, so its negative answers rely on no primality test.

## Files

| file | purpose | runtime |
|---|---|---|
| `tree_enum.py` | Program 2: the search by enumeration only; never factors anything | – |
| `tree_search.py` | Program 1: the same search, recursive, rational arithmetic, divisor route at long intervals | – |
| `thresholds.py` | exact thresholds of Section 2 (1540, 33, M = 2 regions) | seconds |
| `first_equation.py` | Theorem 1.1 for k ≤ 14: both programs, n − 1 = 2φ(n), p₁ ≥ 5, k = 7..14 | ~10 min |
| `second_equation.py` | Theorem 1.2, and Theorem 1.3 for k ≤ 14: n + 1 = 2φ(n), k ≤ 7 with p₁ ≥ 3, and k = 7..14 with p₁ ≥ 5 | ~3 min |
| `lastthree.py` | Section 4, first implementation: the last three primes through divisors in a residue class, boxes in u | – |
| `lastthree_b.py` | Section 4, second implementation: boxes in v, Lagrange-reduced lattice bases, own frontier and prime generation | – |
| `lastthree_c.py` | Section 4.5, third implementation: the sum t + N/t is fixed modulo C'², found by a short scan with one square test per value; no boxes, no factoring, no primality proof | – |
| `k15_run.py` | the case k = 15 of Theorems 1.1 (`--eps -1`) and 1.3 (`--eps 1`) with any of the three implementations (`--program A`, `B` or `C`); resumable, multi-core | 15–45 min of CPU time per run |
| `k15_stats.py` | Figure 4 (the ratio c³/N over the k = 15 search), the run totals of Table 3, and the k = 16 statistics of Section 8 | a few minutes |
| `extensions.py` | Theorem 1.5: one- and two-prime extensions of the known solutions | seconds |
| `check_certificates.py` | re-derives the fifteen long terminal nodes of k = 14 and checks the stored factorisations | seconds |
| `validate.py` | both programs on 2^k(n−1) = (2^k+m)φ(n), k = 4, 5: must return the 56 listed solutions | ~10 min |
| `sieve_check.py` | independent totient sieve to 10^8 | ~3 min |
| `walls.py` | the k = 15 frontier of Section 5, the k = 8 frontier of Section 8, and the depth profiles of Figure 3 | ~1 min |
| `tests/test_divisors.py`, `tests/test_divisors_b.py`, `tests/test_divisors_c.py` | the three divisor routines against brute force on random integers with known factorisation (the recorded run of `test_divisors_b.py` used a box limit of 200000, given as its argument) | minutes |
| `tests/planted_k15.py` | planted divisors at the scale of the k = 15 search, for all three implementations (4 processes) | ~15 min |
| `tests/validate_lastthree.py`, `tests/validate_b.py` | both lattice programs on the 56 validation solutions, on n + 1 = 2φ(n) with k ≤ 7, and on k = 7..14 | seconds |
| `tests/validate_c.py` | the sum route on k = 7..14 for both signs, and on the prefixes of the 61 known solutions | seconds |
| `tests/lattice_finds_solutions.py` | the known solutions are found by the lattice route with factoring switched off | seconds |
| `tests/compare_runs.py` | task-by-task agreement of the k = 15 runs of the three implementations, for both signs | seconds |
| `data/known_solutions.json` | the 56 validation solutions (stored as half-gaps (p−1)/2) | |
| `data/k14_data.json` | level profile of k = 14 and factorisations of D for the fifteen long terminal nodes | |
| `data/k15/frontier.json` | the 54,985 prefixes of twelve primes for k = 15 with their intervals for p₁₃ | |
| `data/k15/run_*.jsonl.gz` | one line per task of each k = 15 run (A, B, C, and `_plus` for n + 1 = 2φ(n)), gzipped | |
| `data/k15/stats.json` | output of `k15_stats.py` | |
| `pseudo/` | Section 8: pseudo-solutions prime to 3 (Theorem 8.3) and the first-moment count; see `pseudo/README.md` | |
| `logs/` | recorded output of every script | |
| `lean/` | Lean 4 formalisation (Lean and Mathlib v4.34.1); `lake build`, then `lake env lean Check.lean` for the axiom audit | ~1 min with the Mathlib cache |

Run any script from the repository root, for example `python3 first_equation.py` or
`python3 k15_run.py data/k15/run_A.jsonl --program A --eps -1 --workers 4`.

## Authors

Deep Bhattacharjee, Priyabrata Mandal, Ushashi Bhattacharya.
The code and the Lean proofs were written by Deep Bhattacharjee with the assistance of Claude (Anthropic).
