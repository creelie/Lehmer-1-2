# v1.0.0

First archived release, accompanying the paper *Lehmer's totient problem with fewer than sixteen prime factors*.

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
- A Lean 4 formalisation (`lean/`, Lean and Mathlib v4.34.1) of Lemmas 2.1–2.3, Corollary 2.4, Propositions 3.1, 3.2,
  3.4, 4.1, 8.1 and 8.4, Lemmas 4.2, 4.3 and 8.2, the identities of Section 4.5 and Remark 6.1, and Theorems 1.4 and 1.5 in
  full, including the thresholds 7, 32 and 1540 and Lucas certificates for the large primes of Table 5. Every
  theorem depends only on Lean's three standard axioms (`lean/Check.lean`).
- Pseudo-solutions prime to 3 (`pseudo/`, Section 8): no solution of x₁⋯x_k ± 1 = 2∏(xᵢ − 1) in odd integers prime to
  3 for k ≤ 12, and none for k ≤ 15 with x₁, …, x_{k−3} prime (Theorem 8.3), each by two programs, one of them
  factoring with PARI/GP. With the entry 3 allowed, the PARI program finds the 59 pseudo-solutions of Lehmer's
  equation with k ≤ 7, and the other program finds exactly those with x₁, …, x_{k−3} prime. Lemma 8.2 and
  Proposition 8.4 are proved in Lean (`lean/LehmerTotient/Barrier.lean`).
- The k = 16 statistics of Section 8 (`k15_stats.py`): the exact number of admissible p₁₃ and a first-order count
  of the admissible pairs (p₁₃, p₁₄), with the sizes of N and of c³/N.
- Drivers for every computational statement in the paper, with recorded logs in `logs/`.
- Factorisation data for the fifteen long terminal nodes of the case k = 14, and the 56 solutions used for validation.
- Change from the preprint code: the root of the search now uses p₀ = 1 in the bound φ(n) ≥ B_j (p_j + 1)^m, which is
  valid when p₁ = 3 is allowed. This changes only the node counts for k = 2 and k = 3 of n + 1 = 2φ(n); every result is unchanged.
- Note on SymPy: with `gmpy2` installed, SymPy's `isprime` uses the Baillie–PSW test at every size. The recorded
  k ≤ 14 runs were made without `gmpy2`; see the README.

Neither Lehmer's totient conjecture nor the question whether φ(n) | n+1 has further solutions is settled.
