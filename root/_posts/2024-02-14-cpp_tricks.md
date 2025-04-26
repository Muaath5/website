---
title: "C++ Tricks"
description: "Hidden features that could be useful in optimizing time, memory, and code length!"
tags: ["c++", "cp"]
lang: en
usemathjax: false
---
## Compiler Optimizations & Target
Pragmas is used for speeding up some codes, sometimes it gets a submission from TLE to AC.

The default optimization in most online judges is `O2`.

```cpp
#pragma GCC optimize("O3,Ofast,unroll-loops")
#pragma GCC target("avx2,sse3,sse4,avx")
```

For optimizing `__builtin_popcount`, use this:

```cpp
#pragma GCC target("popcnt")
```

**Resources:**
- Main: [GCC - Optimization Options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)
- Additional: [Codeforces Blog - \[Tutorial\] GCC Optimization Pragmas - @nor](https://codeforces.com/blog/entry/96344)
- Additional: [USACO Advanced - Vectorization](https://usaco.guide/adv/vectorization?lang=cpp)

# C++ Language
## Optimization keywords: `inline` & `register`
- `inline` is used in functions, which may optimize time & memory in recursion (`inline void check()`)
- `register` is used in variables, which will store your variable in a register in the CPU which will make it faster.

## Comments
The known comments are `//` for line comments, and `/**/` for inline comments.

However, you can use `\` at the end of line-comment to extend it further

## Logging
- Same as output stream, there are error stream which is usually used for logging, it's `cerr` for logging
- You can define keywords like `#define LOCAL_PC`, and use it `#ifdef LOCAL_PC` and put code then `#endif`
- In some online judges, there is a predefined `ONLINE_JUDGE`

## Exit
- **`return x;` in `main`**: this exits the program with an exit code, which you can print in Linux using `echo $?`
- **`goto LABEL;`**: You can jump between lines using labels, write a label in format `LABELWHATEVER:`, then you can jump to that line using `goto LABELWHATEVER;`
- **`exit(int _exit_code)`**: this does same as `return _exit_code` from any function


# Input/Output
## Fast I/O
```cpp
ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
```
which is same as `printf`/`scanf`. But it will make the I/O not immediate, and it will flush at the end of the program or when you print `endl`. so you should use `\n` as a new line.

## File I/O
For using file input output, use `ifstream`, `ofstream`.

For changing `std::cin` & `std::cout` to a file, use this code:
```cpp
freopen("input_filename", "r", stdin);
freopen("output_filename", "w", stdout);
```

## Superfast I/O
`getchar()` & `putchar()` probably is faster

```cpp
static inline int read()
{
    int x = 0;char ch = getchar();
    while (ch < '0' || ch>'9') ch = getchar();
    while (ch >= '0' && ch <= '9') x = (x << 3) + (x << 1) + (ch ^ 48), ch = getchar();
    return x;
}

static inline void print(const int &x) {
    if (x > 9)print(x / 10);
    putchar('0' + x % 10);
}
```

# STD Library
## `vector` & `stack`
- `std::stack` is much worse than `std::vector` in time
- `vector.reserve(x)` preallocates the space for the vector, which may saves time while using `push_back`

## `std::map[x]` vs. `std::map.count(x)`
When using `map[x]`, it is actually saved in the map with the default value, so if you are only about to check, only use `map.count` which won't save it.

## `std::map` vs. `std::unordered_map`
`unordered_map` operations is `O(1)` in average, but it may get to `O(n)`, so you must try both when you get a TLE


# Additional

## Stack vs. Heap
- Allocation in Heap is slower than Stack
- Too many reading in the memory is worse for stack
- **Global** variables are **stored in the heap**
- **Local** variables inside the functions are **stored in the stack**
- In case of TLE **try switching arrays between global & local**

## Array with negitive bounds
```cpp
int a_[3000];
int* a = a_ + 1000;
// Now you can use a[-1000] to a[1999]
```

## Array size with characters
You can use `int a['  '];`, just to let you know :)

## Extra
- Usually pointers & binary operations are pretty fast
- You can use `#import` instead of `#include`
