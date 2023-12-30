---
title: 'Cards Trick'
description: 'A trick between 2 magicians'
lang: en
---
This is a communicational technique, in pocker cards (Baloot).

## Idea
- Give $A$ 5 cards (arbitiraly/randomly)
- He will throw some card to the garbage, and give the cards to $B$
- $B$ will know the card in the grabage

## Explaination
**Steps for $A$:**
- Find two cards with same type (♥/♦/♣/♠), and will meet formula $C_2 = (C_1 + N) \text{ mod } 13$ such that $1 \leq N \leq 6$
- Throw card $C_2$ to the grabage
- Put card $C_1$ to the first
- The rest of the three cards, order then in $N$-th lexicographical order

**Steps for $B$:**
- The type of the card in the garbage is the same as the first card
- Calculate the lexicographical order of the three cards
- The card in the garbage is $C_1 + N \text{ mod } 13$

## Implementation
Here is a [C++ code](/scripts/cards_trick.cpp) that does this