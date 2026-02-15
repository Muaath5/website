---
title: "Is this biology?"
description: "A practice problem for Saudi Biology Olympiad"
tags: ["c++", "math", "cp"]
lang: en
usemathjax: true
---
## The problem
A scientist has isolated five different peptides (1 to 5) containing five amino acids (named A, B, C, D, E). He determined the mass and the sequence of each peptide. The data which he obtained is shown on the table below

| Peptide | Amino Acids Sequence | Mass (Da) |
|---------|---------------------|-----------|
| 1       | BCDACCDEDCB         | 966       |
| 2       | ABBCAEEDECB         | 1099      |
| 3       | BACDAEAEECA         | 1357      |
| 4       | CACADBACAEB         | 1279      |
| 5       | EDDCABBCCEE         | 1014      |

The mass of individual amino acids are shown in the table below

| Amino acids    | Mass (Da) | Amino acids    | Mass (Da) |
|----------------|-----------|----------------|-----------|
| Alanine        | 89        | Leucine        | 131       |
| Arginine       | 174       | Lysine         | 146       |
| Asparagine     | 132       | Methionine     | 149       |
| Aspartic Acid  | 133       | Phenylalanine  | 165       |
| Cysteine       | 121       | Proline        | 115       |
| Glutamic Acid  | 147       | Serine         | 105       |
| Glutamine      | 146       | Threonine      | 119       |
| Glycine        | 75        | Tryptophan     | 204       |
| Histidine      | 155       | Tyrosine       | 181       |
| Isoleucine     | 131       | Valine         | 117       |

Note: The mass of a water molecule is 18 Da.

Indicate if each of the following statements is True or False.

A. Amino acid named C is serine
B. Amino acid named A is tyrosine
C. Amino acid named E is cysteine
D. Amino acid named B is glycine

## Shorter mathematical simplification

Given these equations:
- $A + 2B + 4C + 3D + E = 1046$
- $2A + 3B + 2C + D + 3E = 1139$
- $3A + 1B + 2C + D + 3E = 1397$
- $4A + 2B + 3C + D + E = 1319$
- $A + 2B + 4C + 2D + 3E = 1054$

Indicate if each of the following statements is True or False.
1. $C = 105$
2. $A = 181$
3. $E = 121$
4. $B = 75$

## Solutions
- **Programming**:
  - Gaussian elimination in $O(n^3)$, so it runs in less than $0.0001$
  - Bruteforce in $O(20^5 \cdot log)$ which runs in less than 2 seconds.
- **Math:**
  - System of equations :))


## Bruteforce Solution
We would use recursion, you can [download the C++ code from here](/scripts/bio_problem.cpp)
Input:
```
5
BCDACCDEDCB 966
ABBCAEEDECB 1099
BACDAEAEECA 1357
CACADBACAEB 1279
EDDCABBCCEE 1014
4
C serine
A trysine
E cysteine
B glycine
```
Output:
```
A: tryptophan
B: glycine
C: alanine
D: serine
E: cystine
```







