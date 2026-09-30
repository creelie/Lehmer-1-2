# Pseudo-solutions prime to 3

Programs and logs for Section 8 of the paper: Theorem 8.3 and the first-moment count of Section 8.6. The Lean
proofs of Lemma 8.2 and Proposition 8.4 are in `lean/LehmerTotient/Barrier.lean`.

The equation is

    x_1 x_2 ... x_k + eps = 2 (x_1 - 1)(x_2 - 1) ... (x_k - 1),        eps = -1 (Lehmer) or +1 (companion),

in odd integers 5 <= x_1 < ... < x_k, none divisible by 3, prime or not. Theorem 8.3 states that there is no solution
with k <= 12, and none with k <= 15 in which x_1, ..., x_{k-3} are prime. Each part is checked by two programs.

## Requirements

Those of the repository (Python 3, `sympy`, `python-flint`, `gmpy2`), a C compiler with GMP, and PARI/GP (`gp` on the
PATH) for the two `pari_*` programs. Build the C program first, in this directory:

    gcc -O2 -o tail3 tail3.c -lgmp -lm

## Files

| file | purpose | runtime |
|---|---|---|
| `tail3.c` | the last three entries for a whole interval of x_{k-2} (prime or integer), by the sum route of Section 4.5 | – |
| `tail3lib.py` | driver for `tail3`; problems where the sum route would be long are solved by a complete factorisation, with every prime factor proved prime | – |
| `integer_tree.py` | Theorem 8.3 (i), first program: the tree with integer entries prime to 3, k <= 12, both signs | seconds |
| `prime_prefixes.py` | Theorem 8.3 (ii), first program: the prime prefixes of the search of Theorems 1.1 and 1.3, then three integer entries | about 4 min of CPU time per sign for k = 15 |
| `pari_integer_tree.py` | Theorem 8.3 (i), second program: its own bounds and tree, and at every node with two entries left a complete factorisation with PARI/GP, every factor proved prime; no code shared with the rest of the repository | about an hour for k = 12 |
| `pari_prime_prefixes.py` | Theorem 8.3 (ii), second program, for k <= 14: the same prime prefixes, its own range for x_{k-2}, and a complete factorisation for every value | about half an hour for k = 14 |
| `validate_with3.py` | with the entry 3 allowed, `tail3` finds exactly the solutions listed by `pari_integer_tree.py --with3` whose first k - 3 entries are prime (k <= 7, both signs) | minutes |
| `validate_prime_mode.py` | `tail3` in prime mode treats the 33,865,004 values of p_13 of the case k = 15 (`logs/k15_run_*.log`) and finds no completion | 1 min per sign |
| `first_moment.py` | the first-moment count of Section 8.6; the calibration with the entry 3 allowed | seconds (k <= 6), minutes (k = 7) |
| `first_moment_node.py` | the count for solutions prime to 3 over the tree for k = 12, and below the prefix (5, 7, 13, 17, 19, 23, 25, 37, 119) for k = 12, 13, 14 | about 5 min |
| `logs/` | recorded output | |

## Commands of the recorded runs

Run from this directory.

    python3 integer_tree.py 12                                          > logs/integer_tree.log
    for k in $(seq 3 14); do for e in -1 1; do python3 prime_prefixes.py $k $e; done; done   > logs/prime_prefixes_k3_14.log
    python3 prime_prefixes.py 15 -1 P 4    (P = 0, 1, 2, 3, and the same for eps = 1)   > logs/prime_prefixes_k15.log
    for k in $(seq 3 12); do python3 pari_integer_tree.py $k -1; done  > logs/pari_integer_tree_m1.log   (and 1: _p1)
    for k in $(seq 3 7); do for e in -1 1; do python3 pari_integer_tree.py $k $e --with3; done; done   > logs/pari_integer_tree_with3.log
    for k in $(seq 3 13); do for e in -1 1; do python3 pari_prime_prefixes.py $k $e; done; done   > logs/pari_prime_prefixes_k3_13.log
    python3 pari_prime_prefixes.py 14 -1; python3 pari_prime_prefixes.py 14 1                > logs/pari_prime_prefixes_k14.log
    for k in $(seq 3 7); do for e in -1 1; do python3 pari_prime_prefixes.py $k $e --with3; done; done   > logs/pari_prime_prefixes_with3.log
    python3 validate_with3.py                                           > logs/validate_with3.log
    python3 validate_prime_mode.py -1; python3 validate_prime_mode.py 1 > logs/validate_prime_mode.log
    python3 first_moment.py K -1 --with3 --W0 100000   (K = 4, 5, 6)
    python3 first_moment.py 7 -1 --with3 --W0 1000 --reps 20            > logs/first_moment_with3.log
    python3 first_moment_node.py 1000 30 30 --tree                      > logs/first_moment_node.log

The first-moment counts are heuristic: they estimate how many solutions to expect, and prove nothing.
