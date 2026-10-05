# Sharper bounds in Lehmer's totient problem

Programs, logs and LaTeX source for the note

> P. Mandal, D. Bhattacharjee, U. Bhattacharya,
> *Sharper bounds in Lehmer's totient problem*.

The note proves that a composite n with φ(n) | n−1 and k distinct prime factors satisfies
n < 2^(2^(k−7)); n < 2^(2^(k−24)) when (n−1)/φ(n) ≥ 3; and n < 2^(2^(k−1524)) when 3 | n.
Burek and Żmija had n ≤ 2^(2^k) − 2^(2^(k−1)). The proof combines a sharp form of the product lemma
of Cook and Nielsen (Theorem 1.2 of the note, proved by hand) with an exhaustive search over the
smallest prime factors (Section 5), which the two programs below carry out independently.

| file | purpose | runtime |
|---|---|---|
| `search.py` | the search of Section 5 (tree T_s, rules R1–R4), exact rationals; `python3 search.py 7` | 25 s for s = 7 |
| `search.gp` | the same search written independently in PARI/GP, explicit stack, rule R4(iii) by bisection; `printf 's = 7\n\\r search.gp\n' \| gp -q` | 9 s for s = 7 |
| `search_without_deficit.py` | the search with only the ratio test (no R2, no R4(iii)); `python3 search_without_deficit.py 6` gives 4,469 nodes | 18 s for s = 6 |
| `ratio_bound.py` | the exact values R_24 = 2.99488… < 3 and R_1524 = 3.99986… < 4 of Section 6 | 4 s |
| `tree_stats.py`, `tree_profile.py` | nodes and last-prime tests by depth (Table 1, Figure 4) and the ranges of Figure 3 | seconds |
| `logs/` | recorded output: `search_py_s*.log`, `search_gp_s*.log` (s = 4..7), `ratio_bound.log`, `search_without_deficit_s6.log`, `hist_s*.json`, `prof_s7.json` | |
| `paper/` | LaTeX source (`main.tex`), TikZ figures with PNG exports (`figures/build.sh`, `figures/make_figs.py`), `make_arxiv.sh` | |

Both programs report the same trees for s = 4, 5, 6, 7: 12, 24, 118 and 33,678 nodes, depth 13 for s = 7,
14,814 values of M tested for a last prime, none giving an integer. Requirements: Python 3 with `gmpy2` and
`sympy`, PARI/GP 2.15, pdflatex with TikZ and pgfplots for the paper.

The programs were written by Deep Bhattacharjee with the assistance of Claude (Anthropic).
