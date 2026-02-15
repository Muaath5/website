---
title: "C++ Random"
description: "About different random functions in C++"
tags: ["c++", "resource", "cp"]
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
const int
    A = 12345,
    B = 54321,
    C = 1e9+7;

int lcg(int x) {
    return (A * x + B) % C;
}

int prev = 0;
void seed_my_rand(int seed) {
    prev = seed;
}
int my_rand() {
    return prev = lcg(prev);
}
```

There are other easy algorithms like [Xorshift](https://en.wikipedia.org/wiki/Xorshift) you can check in case of you want to write your own random.

## Where to get seeds?
- Current time (`time(0)` returns current linux timestamp) [Have problems will be discussed later]
- OS random stream in Linux (`/dev/urandom`)
- CPU tick count (Windows: `GetTickCount64()`, Linux: `clock_gettime` or assembly `rdtsc`)
- High precision wall clock (`<chrono>` library)

## About default `rand()` problems
### Low range of values
This is bounded by [`RAND_MAX` macro](https://en.cppreference.com/w/cpp/numeric/random/RAND_MAX.html), which is usually $2^15$ in 32-bit machines, and $2^31$ in 64-bit machines.

### The fixed seed
You can use [`void srand(unsigned seed)` function](https://en.cppreference.com/w/cpp/numeric/random/srand.html), default seed is $1$, but you must put an unpredictable seed.

### Not really random
Because [`rand()`]() depends on compiler implementation, it could have some issues

### Low precision of `time(0)`
It returns precision in seconds, so in some cases if the second the code will run was determined then it could be hacked.

## The good random
```c++
#include <chrono>

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

long long rnd(long long l, long long r) {
    return uniform_int_distribution<long long>(l, r)(rng);
}

```

Note that `std::random_device` could be deterministic in some platforms like Codeforces.

