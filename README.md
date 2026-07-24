# lx

> Learn command-line tools by using real commands.

`lx` is an interactive CLI that helps developers learn tools like `grep`, `find`, `curl`, and `jq` by building, explaining, and running real commands.

Unlike traditional wrappers, `lx` does not hide the underlying commands.

Instead, it reveals them.

The goal is not to make developers dependent on `lx`.

The goal is for developers to eventually stop needing `lx` because they have internalized the commands themselves.

---

## Why?

Many developers know command-line tools are important.

Tools like:

- grep
- find
- curl
- jq
- ssh
- sed
- awk

show up everywhere.

But learning them can be difficult because documentation often focuses on syntax instead of real-world usage.

`lx` aims to bridge that gap.

It teaches command-line tools through:

- explanations
- examples
- guided command building
- exercises
- challenges
- real command execution

---

## Philosophy

### Don't hide the command.

Many tools abstract complexity away.

`lx` does the opposite.

Every interaction should help the user understand the command being generated.

### Learn by doing.

Reading documentation is useful.

Running commands is better.

`lx` encourages hands-on learning with real commands on a real system.

### Build confidence gradually.

Most command-line tools feel overwhelming because they expose many options at once.

`lx` introduces concepts incrementally.

### The ultimate goal is to stop using lx.

Success is when a user naturally types:

```bash
grep -r "TODO" src/
```

instead of:

```bash
lx build grep
```

---

## Features

### Learn

Learn what a command does.

```bash
lx learn grep
```

Example output:

```text
grep

Purpose:
Search text for patterns.

Common use cases:
- Find TODO comments
- Search log files
- Locate references in code

Examples:
grep "TODO" *.py
grep -r "error" logs/
```

---*
### Build

Build commands interac*ively.

```bash
lx build grep
```
*Example:

```text
What text are yo* looking for?

> TODO

Which files*should be searched?

> *.py
*``

Generated output:

```text
Gen*rated command:

👉 grep "TODO* *.py
```

Explanation:

```text
g*ep      → search text

"TODO*    → search for this text

*.py      → search all Python files*```

Optionally execute:

```text
*un? (Y/n)
```

*--

### Challenge

Practice withou* being told the answer.

```bash
l* challenge grep
*``

Example:

```text
Challenge

F*nd all TODO comments in*this project.
```

Users solve the*challenge themselves*and receive feedback.

*--

### Explain

Explain an existi*g command.

```bash
lx explain 'gr*p -r "TODO" src/'
```

Output:

``*text
grep      → search text

-r  *     → recursively search director*es

"TODO"    → search for this te*t

src/      → search within src/
*``

---

## Supported Commands

##* Version 0.1

The initial release*intentionally focuses on only four*tools.

- grep
* find
- curl
- jq

These commands*provide a strong foundation for:

* searching files
- searching text*- working with APIs
- working*with JSON

*uture versions*may support:

* ssh
- tar
- xargs
- sed** awk
- git
- docker

---

## Examp*e Session*
```bash
lx build curl
```

```tex*
What URL should be requested?

> *ttps://api.github.com/users/oct*cat
``*

Generated command:

```text
👉 c*rl https://api.github.com/users/oc*ocat
```

Explanation:

```text
cu*l

Makes an HTTP*request.

https://api.github.com/users/octocat

The URL being request*d.

Request method:

GET
```

Run?*
```text
(Y/n)
```

---

## Projec* Goals*
- Make*command*line tools approachable
- Remove f*ar around terminal usage
- Teach t*rough real commands
- Encourage ex*erimentation
- Help developers bec*me independent terminal users

---*
## Non-Goals

- Replacing existin* tools
- Hiding complexity
- Creat*ng proprietary syntax
- Abstractin* away commands

---

## Inspiratio*

`lx* was inspired by the idea*that the best learning happens thr*ugh use.

Just as*some tools*teach Docker by generating*real Docker commands, `lx` teaches*command-line tools by generating a*d explaining real commands.

The c*mmand is not the implementation*detail.

The command is the lesson*
