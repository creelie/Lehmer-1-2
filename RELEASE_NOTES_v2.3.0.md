# v2.3.0

Code and data for the revised paper *Lehmer's totient problem with fewer than sixteen prime factors*
(`paper/main.tex`). Two results are extended, both by computations whose negative answers are complete.

- **The companion equation with eight prime factors.** φ(n) | n+1 has no solution with exactly eight prime factors,
  so its solutions with at most eight prime factors are the nine known ones (Theorem 1.2, Section 6.4). Such a
  solution has n + 1 = 2φ(n) and p₁ = 3; the search runs over the 10458 prefixes of five primes and 228,260,561 admissible
  sixth primes, 131,788,942 of them under 3, 5, 17, 257, 65537. Programs in `companion8/`:
  - `scan3.c`: the last three primes for a whole interval of the sixth prime, by trial division for the small divisors
    and by the sum of the two complementary divisors for the large ones, both sieved by congruences that primes
    satisfy; every completion is checked with GMP.
  - `factor_class.gp`: the 1,967,265 cases in which this would be slow, by a complete factorisation with PARI/GP and
    every prime factor proved prime (`factor_proven = 1`).
  - `companion8.py` (the run, 6.9 processor hours, journal `data/companion8/journal.jsonl`), `test_scan3.py`
    (known solutions, odd-integer counts, 2868 pairs against complete factorisation) and `recheck.py` (a random sample
    of the run repeated with other parameters). Logs in `companion8/logs/`.
- **Pseudo-solutions prime to 3.** The product equation x₁⋯x_k ± 1 = 2∏(xᵢ − 1) has no solution in odd integers prime
  to 3 for k ≤ 13 (Theorem 8.3 (i)). The case k = 13 is new: `pseudo/integer_tree_scan.py` runs the same kernel in its
  mode for odd integers prime to 3 over the 16,360,285,828 admissible values of x₁₁ under the 86,459 nodes of depth
  10, for each sign, and factors N completely for 73,106 of them; about 15 processor hours per sign. Journals in
  `data/pseudo/`, logs in `pseudo/logs/integer_tree_k13_*.log`.
- **Lean.** `lean/LehmerTotient/Eight.lean` proves the reduction of the eight-prime case to n + 1 = 2φ(n) with
  p₁ = 3, the identities behind trial division and the sum route, and that the sieve of `scan3` keeps every
  completion, for primes and for odd integers prime to 3; `EightData.lean` checks the 21 completions of the
  eight-prime search in the kernel. `lake env lean lean/Check.lean` audits 64 theorems, each depending only on
  `propext`, `Classical.choice` and `Quot.sound`.
- `paper/`: the LaTeX source, the TikZ sources of the figures with their PNG exports (`figures/build.sh`), and
  `make_arxiv.sh`, which builds the PDF and the arXiv source package.

Not settled: Lehmer's equation with sixteen prime factors (about 9·10¹³ two-prime problems, Section 8.1), the companion
equation with nine prime factors and 3 | n (about 1.6·10¹⁷, Section 8.2), and the existence of a pseudo-solution of
Lehmer's equation with pairwise coprime entries.
