# Lehmer's totient problem with fewer than sixteen prime factors

Code, data and Lean proofs for the paper

> P. Mandal, D. Bhattacharjee, U. Bhattacharya,
> *Lehmer's totient problem with fewer than sixteen prime factors*.

What the computations establish (see the paper for the proofs they complete):

1. Every composite n with φ(n) | n−1 has at least 16 distinct prime factors; at least 16001 if (n−1)/φ(n) ≥ 3,
   and more than 10^8 if 3 | n (`bound/`, Proposition 2.5 of the paper).
2. The solutions of φ(n) | n+1 with at most 8 prime factors are exactly
   1, 2, 3, 15, 255, 65535, 83623935, 4294967295, 6992962672132095 (`companion8/` for eight prime factors).
3. Every solution of φ(n) | n+1 with n > 3 and 3 ∤ n has at least 16 distinct prime factors.
4. Every solution of φ(n) | n+1 with n > 3 and (n+1)/φ(n) ≥ 3 has at least 16001 prime factors (more than 10^8
   if 3 | n).
5. The Fermat-type solutions (n+1 = 2φ(n)) are exactly the closure of 1 under one- and two-prime extensions.
6. Every Fermat-type n₀ = p₁⋯p_m gives a pseudo-solution (p₁, …, p_m, n₀) of x₁⋯x_k − 1 = 2∏(xᵢ − 1) that passes
   the congruence prune, so a proof for all k has to use the primality of the factors.
7. These pseudo-solutions have two entries divisible by 3. No solution of x₁⋯x_k ± 1 = 2∏(xᵢ − 1) in odd integers
   prime to 3 exists for k ≤ 13, nor for k ≤ 15 when x₁, …, x_{k−3} are prime (`pseudo/`). The number of entries
   divisible by 3 is even for the sign −1 and odd or zero for +1, and Lemma 2.2 is the only congruence obstruction to
   completing a prefix.
8. In odd integers prime to 3, with gcd(xᵢ, xⱼ − 1) = 1 for all i, j, the equation x₁⋯x_k + 1 = 2∏(xᵢ − 1) has a
   solution for every k ≥ 25, and x₁⋯x_k − 1 = 2∏(xᵢ − 1) has one for every k ≥ 26 (`pseudo/companion_k25.txt`).
   Some entries are composite, so the primality of the factors has to enter beyond the prime 3.
9. A composite n with φ(n) | n−1 and k distinct prime factors satisfies n < 2^(2^(k−7)); moreover
   n < 2^(2^(k−15981)) if (n−1)/φ(n) ≥ 3, and n < 2^(2^(k−10^8)) if 3 | n (`bound/`, Theorem 1.2 of the paper).
10. With three entries left, x₁⋯x_k ± 1 = 2∏(xᵢ − 1) is never a product of linear forms plus a constant, as it is
   with two. An entry x with a^(A±1) ≡ 1 (mod x) for every a prime to x, where A = x₁⋯x_k, is squarefree and
   q − 1 | A ± 1 for every prime q | x; for pairwise coprime entries and the sign −1, A is then a Carmichael number
   (Section 9.7). The tuples of statement 8 all contain the entry 25 and fail this test.

The lemmas and propositions behind 1–4, 7 and 9, and statements 5, 6, 8 and 10 in full, are proved in Lean 4 in
`lean/` (see `lean/README.md`); for 2 and 7 this includes the reduction, the identities and the sieve of the
eight-prime program, and the 21 completions it finds; for 4 it includes the bounds 33 and 1540 that the products
alone give; for 9 it includes Theorem 6.2 with its equality case, the lemma of Cook and Nielsen, and the step from
the product lemma to the size of a solution (a solution that is not s-heavy has n < 2^(2^(k−s)), Corollary 6.10).
The exhaustive searches are checked by independent programs, not formalised.

Neither Lehmer's totient conjecture nor the question whether φ(n) | n+1 has further solutions is settled.

## Requirements

Python 3.8 or later with `sympy` (tested with Python 3.11 and sympy 1.14). `sieve_check.py` also needs `numpy`
and about 2 GB of memory. The fifteen-prime programs (`lastthree.py`, `lastthree_b.py`, `lastthree_c.py`, `k15_run.py`,
`k15_stats.py` and the scripts in `tests/`) need `numpy`, `gmpy2` and `python-flint` (tested with numpy 2.4,
gmpy2 2.3 and python-flint 0.9, which bundles FLINT 3.6). The eight-prime search in `companion8/` and
`pseudo/integer_tree_scan.py` also need a C compiler with GMP and PARI/GP 2.15 or later (`gp` on the PATH).

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
| `second_equation.py` | Theorem 1.3, and Theorem 1.4 for k ≤ 14: n + 1 = 2φ(n), k ≤ 7 with p₁ ≥ 3, and k = 7..14 with p₁ ≥ 5 | ~3 min |
| `lastthree.py` | Section 4, first implementation: the last three primes through divisors in a residue class, boxes in u | – |
| `lastthree_b.py` | Section 4, second implementation: boxes in v, Lagrange-reduced lattice bases, own frontier and prime generation | – |
| `lastthree_c.py` | Section 4.5, third implementation: the sum t + N/t is fixed modulo C'², found by a short scan with one square test per value; no boxes, no factoring, no primality proof | – |
| `k15_run.py` | the case k = 15 of Theorems 1.1 (`--eps -1`) and 1.4 (`--eps 1`) with any of the three implementations (`--program A`, `B` or `C`); resumable, multi-core | 15–45 min of CPU time per run |
| `k15_stats.py` | Figure 9 (the ratio c³/N over the k = 15 search), the run totals of Table 3, and the k = 16 statistics of Section 9 | a few minutes |
| `extensions.py` | Theorem 1.6: one- and two-prime extensions of the known solutions | seconds |
| `check_certificates.py` | re-derives the fifteen long terminal nodes of k = 14 and checks the stored factorisations | seconds |
| `validate.py` | both programs on 2^k(n−1) = (2^k+m)φ(n), k = 4, 5: must return the 56 listed solutions | ~10 min |
| `sieve_check.py` | independent totient sieve to 10^8 | ~3 min |
| `walls.py` | the k = 15 frontier of Section 5, the k = 8 frontier of Section 7.4, and the depth profiles of Figure 8 | ~1 min |
| `companion8/` | Theorem 1.3 for eight prime factors (Section 7.4): the C program `scan3.c` for the last three primes (trial division and the sum of the two factors, sieved by congruences), the PARI/GP fallback `factor_class.gp`, the driver `companion8.py` (resumable, multi-core), the tests `test_scan3.py` and the partial repetition `recheck.py`; see `companion8/README.md` | 6.9 h of CPU time, 2.0 h on 4 cores |
| `data/companion8/journal.jsonl` | one line per batch of the eight-prime run: pieces, counts, timings and completions | |
| `paper/` | LaTeX source of the paper, the TikZ sources of the figures with their PNG exports (`figures/build.sh`) | |
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
| `pseudo/` | Section 9: pseudo-solutions prime to 3 (Theorem 9.3) and the first-moment count; see `pseudo/README.md` | |
| `logs/` | recorded output of every script | |
| `bound/` | Proposition 2.5 (independent sets of primes) and Section 6 (Theorem 1.2): two independent programs for each search, the computation of Section 6.5, and their logs; see `bound/README.md` | see `bound/README.md` |
| `lean/` | Lean 4 formalisation (Lean and Mathlib v4.34.1); `lake build`, then `lake env lean Check.lean` for the axiom audit | ~1 min with the Mathlib cache |

Run any script from the repository root, for example `python3 first_equation.py` or
`python3 k15_run.py data/k15/run_A.jsonl --program A --eps -1 --workers 4`.

## Authors

Priyabrata Mandal, Deep Bhattacharjee (corresponding author), Ushashi Bhattacharya.
The code and the Lean proofs were written by Deep Bhattacharjee with the assistance of Claude (Anthropic).
