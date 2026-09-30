# v1.0.0

First archived release, accompanying the paper *Lehmer's totient problem and the companion equation φ(n) | n+1*.

- Two independent implementations of the exact branch-and-bound for n ± 1 = 2φ(n) (`tree_enum.py`, `tree_search.py`).
- Drivers for every computational statement in the paper, with recorded logs in `logs/`.
- Factorisation data for the fifteen long terminal nodes of the case k = 14, and the 56 solutions used for validation.
- Change from the preprint code: the root of the search now uses p₀ = 1 in the bound φ(n) ≥ B_j (p_j + 1)^m, which is
  valid when p₁ = 3 is allowed. This changes only the node counts for k = 2 and k = 3 of n + 1 = 2φ(n); every result is unchanged.
