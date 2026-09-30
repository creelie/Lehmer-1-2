# Lehmer's totient problem and the companion equation φ(n) | n+1

Code and data for the paper

> D. Bhattacharjee, P. Mandal, U. Bhattacharya,
> *Lehmer's totient problem and the companion equation φ(n) | n+1*.

What the computations establish (see the paper for the proofs they complete):

1. Every composite n with φ(n) | n−1 has at least 15 distinct prime factors.
2. The solutions of φ(n) | n+1 with at most 7 prime factors are exactly
   1, 2, 3, 15, 255, 65535, 83623935, 4294967295, 6992962672132095.
3. Every solution of φ(n) | n+1 with n > 3 and 3 ∤ n has at least 15 distinct prime factors.
4. Every solution of φ(n) | n+1 with n > 3 and (n+1)/φ(n) ≥ 3 has at least 33 prime factors (1540 if 3 | n).
5. The Fermat-type solutions (n+1 = 2φ(n)) are exactly the closure of 1 under one- and two-prime extensions.

Neither Lehmer's totient conjecture nor the question whether φ(n) | n+1 has further solutions is settled.

## Requirements

Python 3.8 or later with `sympy` (tested with sympy 1.14). `sieve_check.py` also needs `numpy`
and about 2 GB of memory.

## Files

| file | purpose | runtime (one core) |
|---|---|---|
| `tree_enum.py` | Program 2: the search by enumeration only; never factors anything | – |
| `tree_search.py` | Program 1: the same search, recursive, rational arithmetic, divisor route at long intervals | – |
| `thresholds.py` | exact thresholds of Section 2 (1540, 33, M = 2 regions) | seconds |
| `first_equation.py` | Theorem 1.1: both programs, n − 1 = 2φ(n), p₁ ≥ 5, k = 7..14 | ~10 min |
| `second_equation.py` | Theorems 1.2 and 1.3: n + 1 = 2φ(n), k ≤ 7 with p₁ ≥ 3, and k = 7..14 with p₁ ≥ 5 | ~3 min |
| `extensions.py` | Theorem 1.5: one- and two-prime extensions of the known solutions | seconds |
| `check_certificates.py` | re-derives the fifteen long terminal nodes of k = 14 and checks the stored factorisations | seconds |
| `validate.py` | both programs on 2^k(n−1) = (2^k+m)φ(n), k = 4, 5: must return the 56 listed solutions | ~10 min |
| `sieve_check.py` | independent totient sieve to 10^8 | ~3 min |
| `walls.py` | Section 7 statistics (k = 15 and k = 8 frontiers) and the depth profiles of Figure 2 | ~1 min |
| `data/known_solutions.json` | the 56 validation solutions (stored as half-gaps (p−1)/2) | |
| `data/k14_data.json` | level profile of k = 14 and factorisations of D for the fifteen long terminal nodes | |
| `logs/` | recorded output of every script | |

Run any script from the repository root, for example `python3 first_equation.py`.

## Authors

Deep Bhattacharjee, Priyabrata Mandal, Ushashi Bhattacharya.
The code was written by Deep Bhattacharjee with the assistance of Claude (Anthropic).
