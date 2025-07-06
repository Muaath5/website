---
title: "C++ Random"
description: "About different random functions in C++"
tags: ["c++", "cpp"]
lang: en
usemathjax: true
updates_history:
    05_17: "Inital write"
    06_10: "Added external links, completed content and published"
---

## How does random work?
There are multiple random generator algorithms, here is a famous one:

This is called [Linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) works like this:

$$X_{n+1} = ((X_{n} \cdot A + B)) \mod C$$

For some constants $0 < A < m$, $0 \le B < C$, $0 < C$, it generates a value in range $[0, C)$

So at first it should be seeded by a value $X_0$, and to generate the next, you could have the following code:

```c++
const ll
    A = 123456789,
    B = 654321,
    C = 1e9+7;

int lcg(int x) {
    return (A * x + B) % C;
}

int prev = 0;
void seed_my_rand(int seed) {
    prev = seed;
}
int my_rand() {
    return prev = weird_func(prev);
}
```

There are other easy algorithms like [Xorshift](https://en.wikipedia.org/wiki/Xorshift) you can check in case of you want to write your own random.

## Where to get seeds?
- Current time (`time(0)` returns current linux timestamp) [Have problems will be discussed later]
- Machine random stream in Linux (`/dev/urandom`)
uncontrollable seeds, like: current time (`time(0)`), or random input from the machine (could be like `/dev/urandom`).

## About default `rand()` problems
### Low range of values
This is bounded by [`RAND_MAX` macro](https://en.cppreference.com/w/cpp/numeric/random/RAND_MAX.html), which is usually $2^15$ in 32-bit machines, and $2^31$ in 64-bit machines.

### The fixed seed
You can use [`void srand(unsigned seed)` function](https://en.cppreference.com/w/cpp/numeric/random/srand.html), default seed is $1$, but you must put an unpredictable seed.

### Not really random
