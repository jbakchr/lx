# lx - PROJECT_CONTEXT.md

> Learn command-line tools by using real commands.

---

# Project Overview

lx is a CLI tool designed to help developers learn command-line tools through guided, interactive usage.

Unlike traditional wrappers, lx does not attempt to hide underlying commands.

Instead, lx intentionally exposes, explains, and executes real commands so that users gradually internalize how those commands work.

The project's primary goal is educational.

The long-term success metric is that users eventually stop needing lx because they have learned how to use the commands directly.

---

# Problem Statement

Many developers understand basic terminal navigation:

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

lx aims to bridge that gap.

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

with no visibility into what happens.

Good:

```text
Generated grep command

👉 grep -r "TODO" .
```

The user sees the real command and learns from it.

---

## Learn By Doing

lx prioritizes:

- interaction
- experimentation
- execution

over passive reading.

The ideal flow is:

```text
Learn
→ Build
→ Run
→ Reflect
```

---

## Confidence Over Abstraction

Many tools reduce complexity by hiding it.

lx should reduce fear without hiding complexity.

The goal is not:

> Never learn grep.

The goal is:

> Learn grep gradually.

---

## Independence Over Dependency

Most software aims to create long-term usage.

lx aims for the opposite.

A successful user eventually stops using lx because they have learned the commands themselves.

---

# Inspiration

This project is strongly inspired by the author's dx Docker learning tool.

One of the most valuable aspects of dx is that it teaches Docker while helping users accomplish real tasks.

Example:

```bash
dx run nginx
```

generates:

```bash
docker run -d -p 8080:80 --name web nginx
```

The generated command is explained before execution.

Over time, users begin remembering and writing Docker commands themselves.

lx applies the same philosophy to general command-line tools.

---

# Most Important Discovery So Far

Originally, the plan was to build:

- grep
- find
- curl
- jq
- infrastructure
- models
- shared abstractions

all within the first phase.

During development we discovered a better approach:

> Build one complete command-learning experience first.

The project now follows this principle:

> Build first.
>
> Learn from usage.
>
> Extract abstractions later.

This is currently one of the most important design principles in the project.

---

# Current Scope

## Version 0.1

The first release intentionally focuses on:

```text
grep
find
curl
jq
```

However, only grep is currently implemented.

Future versions may support:

```text
ssh
tar
xargs
sed
awk
git
docker
```

These remain intentionally out of scope today.

---

# Primary Modes

lx is currently built around four conceptual modes.

## Learn

Purpose:

Teach what a command does.

Example:

```bash
lx learn grep
```

Should explain:

- purpose
- common use cases
- examples
- practical exercises

---

## Build

Purpose:

Help users construct a real command interactively.

Example:

```bash
lx build grep
```

Current workflow:

```text
What text are you looking for?

> TODO

Which file or directory should be searched?

> .

Search recursively?

> y
```

Generates:

```text
👉 grep -r "TODO" .
```

and explains the generated command before optionally executing it.

This is currently considered the core experience of lx.

---

## Challenge

Purpose:

Allow users to practice independently.

Example:

```bash
lx challenge grep
```

Not yet implemented.

Potential features:

- realistic scenarios
- hints
- solutions
- increasing difficulty

---

## Explain

Purpose:

Help users understand commands they encounter elsewhere.

Example:

```bash
lx explain 'grep -r "TODO" .'
```

Not yet implemented.

Potential output:

```text
grep       → search text

-r         → search recursively

"TODO"     → search pattern

.          → target directory
```

---

# Current Implementation

## Completed

### Core CLI

- Typer application
- Rich output
- Command groups

### grep Learn Mode

```bash
lx learn grep
```

Implemented:

- Why Learn grep?
- Common Use Cases
- Examples
- Try It exercise

### grep Build Mode

```bash
lx build grep
```

Implemented:

- Interactive prompts
- Command generation
- Command explanation
- Command execution

Example:

```bash
grep -r "TODO" .
```

is generated and executed for the user.

---

# Current Development Phase

Current Phase:

✅ Phase 1A — grep Vertical Slice Complete

🚧 Phase 1B — Improve grep Experience

Current focus:

- Improve grep workflow
- Improve formatting
- Improve explanations
- Improve execution output
- Discover patterns through usage

Important:

Do not introduce major abstractions yet.

The grep workflow should mature before extracting shared architecture.

---

# Intended User

The primary user is:

- a developer who knows basic terminal navigation
- wants to become more comfortable with command-line tools
- learns best by doing
- prefers practical examples over extensive theory

The project is being built primarily for the author's own learning journey.

If others find it useful, that is a bonus.

---

# Technical Preferences

Current assumptions:

- Python
- Typer
- Rich

The project should follow the same philosophy used in the author's other CLI projects.

Prefer:

- simple structure
- minimal abstraction
- incremental development
- practical usability
- clear terminal output

Avoid:

- unnecessary frameworks
- plugin systems
- premature architecture
- abstraction before validation

Whenever possible:

- implement the simplest thing that works
- prefer clarity over flexibility
- delay complexity until it is truly needed

---

# Success Criteria

lx succeeds if users gain confidence using real command-line tools.

A successful user should eventually feel comfortable typing:

```bash
grep -r "TODO" .
```

instead of:

```bash
lx build grep
```

The objective is not dependency.

The objective is understanding.

The ideal outcome is that users eventually stop needing lx because they have learned the commands themselves.
