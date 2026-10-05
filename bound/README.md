# The size of a solution (Section 6 of the paper)

Programs and logs for Theorem 1.2 of the paper

> P. Mandal, D. Bhattacharjee, U. Bhattacharya,
> *Lehmer's totient problem with fewer than sixteen prime factors*.

Theorem 1.2 states that a composite n with φ(n) | n−1 and k distinct prime factors satisfies
n < 2^(2^(k−7)); n < 2^(2^(k−24)) when (n−1)/φ(n) ≥ 3; and n < 2^(2^(k−1524)) when 3 | n.
Burek and Żmija had n ≤ 2^(2^k) − 2^(2^(k−1)). The proof combines a sharp form of the product lemma
of Cook and Nielsen (Theorem 6.2, proved by hand) with an exhaustive search over the smallest prime
factors (Section 6.3), which the two programs below carry out independently. The programs write
P_j, F_j, r_j and t_i for the quantities A_j, B_j, P_j and θ_i of the paper.

| file | purpose | runtime |
|---|---|---|
| `search.py` | the search of Section 6.3 (tree T_s, rules R1–R4), exact rationals; `python3 search.py 7` | 25 s for s = 7 |
| `search.gp` | the same search written independently in PARI/GP, explicit stack, rule R4(iii) by bisection; `printf 's = 7\n\\r search.gp\n' \| gp -q` | 9 s for s = 7 |
| `search_without_deficit.py` | the search with only the ratio test (no R2, no R4(iii)); `python3 search_without_deficit.py 6` gives 4,469 nodes | 18 s for s = 6 |
| `ratio_bound.py` | the exact values R_24 = 2.99488… < 3 and R_1524 = 3.99986… < 4 of Section 6.5 | 4 s |
| `tree_stats.py`, `tree_profile.py` | nodes and last-prime tests by depth (Table 4, Figure 13) and the ranges of Figure 12 | seconds |
| `logs/` | recorded output: `search_py_s*.log`, `search_gp_s*.log` (s = 4..7), `ratio_bound.log`, `search_without_deficit_s6.log`, `hist_s*.json`, `prof_s7.json` | |

The five figures of Section 6 are drawn from TikZ sources in `../paper/figures` (`fig_dichotomy`, `fig_bases`, `fig_rules`,
`fig_margins`, `fig_trees`); `make_heavy.py` there writes the last two from `logs/`.

Both programs report the same trees for s = 4, 5, 6, 7: 12, 24, 118 and 33,678 nodes, depth 13 for s = 7,
14,814 values of M tested for a last prime, none giving an integer. Requirements: Python 3 with `gmpy2` and
`sympy`, PARI/GP 2.15.

The programs were written by Deep Bhattacharjee with the assistance of Claude (Anthropic).
