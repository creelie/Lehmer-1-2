# v1.0.0

First archived release, accompanying the paper *Lehmer's totient problem and the companion equation φ(n) | n+1*.

- Two independent implementations of the exact branch-and-bound for n ± 1 = 2φ(n) (`tree_enum.py`, `tree_search.py`).
- Three independent implementations of the treatment of the last three primes. Once p_{k−2} is fixed, the last
  two primes correspond to a divisor of an explicit integer N in a known residue class modulo c. `lastthree.py`
  and `lastthree_b.py` find these divisors by listing lattice points of a coset near a hyperbola, or, when c³ is
  much smaller than N, by a complete factorisation with every prime factor proved prime. `lastthree_c.py` uses
  that t and N/t lie in the same class, so t + N/t is fixed modulo c²; it factors nothing.
- The case k = 15 (`k15_run.py`): no solution of n − 1 = 2φ(n) or of n + 1 = 2φ(n) with 3 ∤ n has exactly
  fifteen prime factors. Together with k ≤ 14 this gives ω(n) ≥ 16 in both cases. All three implementations ran
  over the same 33,865,004 choices of p₁₃ for each sign and agree task by task; the per-task records are in
  `data/k15/`.
- Tests for the three-prime methods in `tests/`: brute force on random integers, planted divisors at the scale of
  the k = 15 search, the 56 validation solutions, the Fermat-type solutions, and the cases k = 7..14.
- Drivers for every computational statement in the paper, with recorded logs in `logs/`.
- Factorisation data for the fifteen long terminal nodes of the case k = 14, and the 56 solutions used for validation.
- Change from the preprint code: the root of the search now uses p₀ = 1 in the bound φ(n) ≥ B_j (p_j + 1)^m, which is
  valid when p₁ = 3 is allowed. This changes only the node counts for k = 2 and k = 3 of n + 1 = 2φ(n); every result is unchanged.
- Note on SymPy: with `gmpy2` installed, SymPy's `isprime` uses the Baillie–PSW test at every size. The recorded
  k ≤ 14 runs were made without `gmpy2`; see the README.

Neither Lehmer's totient conjecture nor the question whether φ(n) | n+1 has further solutions is settled.
