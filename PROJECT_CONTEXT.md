# lx - PROJECT_CONTEXT.md

> _Learn command-line tools by using real commands._

---

## Project Overview

`lx` is a CLI tool designed to help developers learn command-line tools through guided, interactive usage.

Unlike traditional wrappers, `lx` does not attempt to hide underlying commands.

Instead, `lx` intentionally exposes, explains, and executes real commands so that users gradually internalize how those commands work.

The project's primary goal is educational.

The long-term success metric is that users eventually stop needing lx because they have learned how to use the commands directly.

---

# Problem Statement

Many developers understand the basics of terminal navigation:

```bash
cd
ls
pwd
```

but often feel uncomfortable using tools such as:

```bash
grep
find
curl
jq
ssh
sed
awk
```

Documentation for these tools is often:

- syntax-heavy
- reference-oriented
- difficult for beginners
- disconnected from real-world workflows

As a result, developers know these tools are important but never become comfortable using them.

`lx` aims to bridge that gap.

---

# Core Philosophy

## Don't Hide The Command

The command is not an implementation detail.

The command is the lesson.

Every feature should reinforce understanding of the underlying command.

Bad:

```bash
lx search todo
```

with no visibility into what actually happens.

Good:

```text
Generated command:

👉 grep "TODO" *.py
```

The user sees the real co\*mand and can learn from it.

---

\*# Learn By Doing

`lx` should priori\*ize:

- interaction
- experimentat\*on
- execution

over passive readi\*g.

The ideal flow is:

````text*Learn
→ Build
→ Run
→*Reflect*```

---

## Confidence Over Abstr*ction

Many tools reduce complexit* by hiding it.

lx should reduce f*ar without hiding complexity.

The*goal is*not:

> "Never learn*grep."

The goal is:

> "*earn grep gradually*"

---

## Independence Over Depen*ency

Most software aims to create*long-term usage.

`lx` aims for*the opposite.

A successful*user eventually stops using lx bec*use they have learned the commands*themselves.

---

# Inspiration

T*is project was strongly inspired b* the "dx" Docker learning tool*

One of the most valuable aspects*of dx is*that it teaches Docker while helpi*g users accomplish real tasks.

Ex*mple:

```bash
dx run nginx
````

g\*nerates:

```bash
docker run -d -* 8080:80 --name web nginx
```

The*generated command*is explained before execution.

Ov*r time, users begin remembering an* writing Docker commands themselve\*.

`lx` applies the same idea to gen\*ral command-line tools.

---

# In\*tial Scope (v0.1)

*he first*version deliberately focuses on on\*y four commands.

```text
grep
fin*
curl
*q
```

These commands provide a st\*ong foundation for:

- searching f\*les
- searching text
- interacting\*with APIs
- processing JSON

Futur\* versions may support:

*``text
ssh
tar
xargs
sed
awk
git
*ocker

````

However, those*are intentionally out*of scope for the first release.

-*-

# Primary Modes*
`lx` is*currently envisioned*around four primary*modes.

## Learn

Purpose:

Teach *hat a command does.

Example:

```*ash
lx learn grep
````

Should expl\*in:

- purpose
- common use cases

* examples

- common mistakes

---

\*# Build

Purpose:

Help users cons\*ruct a command interactively.

Exa\*ple:

```bash
lx build grep
```

P\*ompts the user with questions.

Ex\*mple:

```text
What text are you s*arching for?

> TODO

Which files *hould be searched?

> *.py
```

Pr\*duces:

```text
Generated command:*
👉 grep "TODO" *.py
```

with exp\*anations.

This is currently consi\*ered the core experience of `lx`.

-\*-

## Challenge

Purpose:

Allow u\*ers to practice independently.

Example:

```bash
lx challenge grep
```

Should provide:

- realistic scenarios
- hints
- solutions
- incre*sing difficulty

---

## Explain

*urpose:

Help users understand com*ands they encounter elsewhere.

Ex*mple:

```bash
lx explain 'grep -r*"TODO" src/'
```

Produces a detailed explanation of:

- command
- arguments
- flags

---

# Intended User

The primary user is:

- a developer who knows basic terminal navig*tion
- wants to become more comfor\*able with command-line tools
- lea\*ns best by doing
- prefers practic\*l examples over extensive theory

The project is being built primarily for the author's own learning journey.

If others find it useful, that is a bonus.

---

- Technical Preferences
  Current assumptions:

- Python

* Typer
* Rich
  the project should follow the same *hilosophy seen in the author's oth\*r CLI tools:

* simple structure minimal abstraction
* incremental development - avoid premature architecture

Whenever possible:

- implement the simplest thing that works
- prefer clarity over flexibility
- delay complexity until it is truly needed

---

# Current States

Current Phase:

✅ Phase 0 — Protect Definition

Completed:

- Proj\*ct idea established
- Initial phil\*sophy established
- README drafted\*- ROADMAP drafted
- PROJECT_CONTEX\* drafted

Next Step:

Begin Phase \* (Foundation / MVP)

Focus on:

- creating Typer application
- creating command structure
- implementing first command (`grep`)
- validating the Learn + Build workflow

---

- Success Criteria

`lx` succeeds if users gain confidence using real command-line tools.

A successful user should eventually feel comfortable typing:

```bash
grep -r "TODO" src/
```

instead of:

```bash
lx build grep
```

The objective is not dependency.

The objective is understanding.
