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
  - `companion8.py` (the run, 6.8 processor hours, journal `data/companion8/journal.jsonl`), `test_scan3.py`
    (known solutions, odd-integer counts, 2868 pairs against complete factorisation) and `recheck.py` (a random sample
    of the run repeated with other parameters). Logs in `companion8/logs/`.
- **Pseudo-solutions prime to 3.** The product equation x₁⋯x_k ± 1 = 2∏(xᵢ − 1) has no solution in odd integers prime
  to 3 for k ≤ @@KI@@ (Theorem 8.3 (i)); the case k = 13 is new, by `pseudo/integer_tree_scan.py`, which runs the same
  kernel in its mode for odd integers prime to 3. Logs in `pseudo/logs/integer_tree_k13_*.log`.
- `paper/`: the LaTeX source, the TikZ sources of the figures with their PNG exports (`figures/build.sh`), and
  `make_arxiv.sh`, which builds the PDF and the arXiv source package.

Not settled: Lehmer's equation with sixteen prime factors (about 9·10¹³ two-prime problems, Section 8.1), the companion
equation with nine prime factors and 3 | n (about 1.6·10¹⁷, Section 8.2), and the existence of a pseudo-solution of
Lehmer's equation with pairwise coprime entries.
