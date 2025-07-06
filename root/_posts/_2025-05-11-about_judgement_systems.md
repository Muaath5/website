---
title: "Online Judgement Systems"
description: "Terminology, and a tour on different types of tasks"
tags: ["cp", "judgement"]
lang: en
usemathjax: true
---

# Intro
I'm going to write about the components and how they are merged to form a different types of problems.

I'm focusing on making components clear, and show how does Polygon and CMS use them.

## Prerequisites
- Authored a problem on Polygon before
- Know interactive/communication tasks
<!-- - [Prefered] Know [IOI 2024 message](https://oj.uz/problem/view/IOI24_message), will be used in examples -->

# Terminology
## General terminology
- I/O: Input/Output
- OJ: Online Judge, a system that performs judgement.
- Sandbox: A secure environment that runs untrusted programs

## Judge terminology
- Task: A problem with clear I/O format, that's solving usually requires doing some coding.
- ModelCode: The solution of the problem author
- UserCode: The code that the users submits for judgement 
- Testcases: A set of tests that judge tests them on the User solution
- TestcaseInput: A text file that contains a testcase, a task usually consists of many of it.
- ModelOutput: Output of the model solution
- UserInput: Standard input (stdin) for UserCode
- UserOutput: Standard output (stdout) for UserCode

# Judgement Components

## [Testlib.h](https://github.com/MikeMirzayanov/testlib)
A library header usually judges provide to help problems authors.

Usually Compiled with grader/scorer/interactor/validator/manager.

It makes handling I/O, exit codes, formatting output, and output messages easier.

## Checker
A program that reads from TestcaseInput, UserOutput, ModelOutput, and returns a judgement either a score or a verdict, with a messsage sometimes.

The <u>CheckerOutput</u> format should be provided by the judge that you are using, Usually matches `testlib.h` default output and exit code.

## Validator
A program that reads an input and checks if it's correct or not, used usually to prevent mistakes and in case the hacks are allowed.

## Interactor
In general it reads from UserOutput and any other files, and writes to InteractorOutput and UserInput and any other files.

Usually reads TestcaseInput and UserOutput, and writes to InteractorOutput and to UserInput

## Scorer
> [Used to compute the final score based on verdicts on all tests. This was used for several problems in the IOI archive, but it's kinda work-in-progress](https://codeforces.com/blog/entry/104869?#comment-931781)

If you know details of it [contact me](me@muaath.dev).

## Grader (called _"stub"_)
An additional file compiled with UserCode that handles I/O.

## Manager
A program that runs multiple codes, usually used in communication/two-steps problems.

# Types of tasks

## By type that changes the type
- Batch, have some different types in case of grader
  - Online: User must provide procedures to be called ()
  - Offline: All the data are given in the begining
- Interactive _(named "Communication" in CMS)_
  - Adaptive: Interactor have a strategy
  - Inadaptive: Interactor just performs operations based on input data
- [Communcation (named "Two-Steps" in CMS)](https://muaath.dev/blog/communication_tasks)
  - Encoder/Decoder style (APIO 2023 Practice)
  - Encoder/Messanger/Decoder style (APIO 2024 Magic Show)
  - Two Encoders/Decoder style (Only APIO 2023 ABC, new style of tasks)
- Output-only

#### Ideas about some tasks
- You can implement Online batch tasks using Interactive, you don't give him the next answer except if he outputs for the current query.
- 

### Grader _(named "Implementer" in UOJ)_
- Have a grader
- Normal I/O
 
**Good sides:**
- Easy forcing of Online solutions
- Unified I/O code
- Makes people care less about technicalities and more about thinking
- Faster than programs communicating in Interactive/Communication problems

**Down sides:**
- Could be hacked on Interactive/Communication problems
- Can't measure the program alone without  if the interactor was merged with the 

### Scoring
You can read [CMS defenitions](https://cms.readthedocs.io/en/v1.5/Score%20types.html):
- The total score is divided for every testcase, and every testcase could get you a point (Sum in CMS)
- 


# Current systems method

## Examples for the same task from different judges
- Polygon ([Example]())
- CMS ([IOI 2024](https://github.com/ioi-2024/tasks))
- UOJ ([APIO 2024](https://github.com/APIO-2024/apio2024_tasks))

## Polygon
Idk I have to read & try so much

### How to make it secure?
#### Main security issues
- Memory violation for the grader
- Trying to read/rewrite model solution precalculated output
- Accessing other users compiled program and being a man in the middle

### 