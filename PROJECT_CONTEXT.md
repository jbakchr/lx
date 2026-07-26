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
→ Understand
→ Run
```

The project should always encourage users to actively use commands rather than simply read about them.

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

# Most Important Discoveries So Far

## Discovery #1

Originally, the plan was to build:

- grep
- find
- curl
- jq
- infrastructure
- models
- shared abstractions

all within the first phase.

Development revealed a better approach:

> Build one complete command-learning experience first.

This remains one of the project's most important design principles.

---

## Discovery #2

The most valuable educational output is not a technical explanation of flags.

Instead, users learn best when a command is explained from a beginner's perspective.

Example:

Instead of:

```text
-r → search recursively
```

lx now prefers:

```text
-r
→ search all files underneath this directory
```

The goal is understanding what a command does rather than memorizing flag definitions.

---

## Discovery #3

Project structure should mirror user workflows.

Instead of organizing around abstract systems, lx now organizes around:

```text
lx learn grep
lx build grep

lx learn find
lx build find
```

This makes the code easier to navigate and understand.

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

Current status:

✅ grep implemented

✅ find implemented

🚧 curl planned

🚧 jq planned

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

---

## Learn

Purpose:

Teach what a command does.

Examples:

```bash
lx learn grep
```

```bash
lx learn find
```

Learn mode should explain:

- purpose
- common use cases
- examples
- practical exercises

Current lesson structure:

```text
Why Learn?

Common Use Cases

Examples

Try It
```

---

## Build

Purpose:

Help users construct a real command interactively.

Examples:

```bash
lx build grep
```

```bash
lx build find
```

A build workflow should:

1. Ask simple questions
2. Generate a real command
3. Explain how to read the command
4. Optionally execute the command

Example:

```text
Generated grep command

👉 grep -r "TODO" .
```

Followed by:

```text
How To Read This Command

grep
→ the tool we are using

-r
→ search all files underneath this directory

"TODO"
→ the text we want to find

.
→ start searching from this location
```

Build mode is currently considered the core lx experience.

---

## Challenge

Purpose:

Allow users to practice independently.

Example:

```bash
lx challenge grep
```

Status:

🚧 Not implemented

Potential features:

- realistic scenarios
- hints
- solutions
- answer validation

---

## Explain

Purpose:

Help users understand commands they encounter elsewhere.

Example:

```bash
lx explain 'grep -r "TODO" .'
```

Possible output:

```text
grep
→ search text

-r
→ search recursively

"TODO"
→ search pattern

.
→ target directory
```

Status:

🚧 Not implemented

---

# Current Implementation

## Completed

### Core CLI

Implemented:

- Typer application
- Rich output
- Project packaging via pyproject.toml
- Installable `lx` command
- Command routing

---

### grep Learn Mode

```bash
lx learn grep
```

Implemented:

- Why Learn?
- Common Use Cases
- Examples
- Try It

---

### grep Build Mode

```bash
lx build grep
```

Implemented:

- Interactive prompts
- Command generation
- Educational command breakdown
- Command execution

Example generated command:

```bash
grep -r "TODO" .
```

---

### find Learn Mode

```bash
lx learn find
```

Implemented:

- Why Learn?
- Common Use Cases
- Examples
- Try It

Example:

```bash
find . -name "*.py"
```

---

### find Build Mode

```bash
lx build find
```

Implemented:

- Interactive prompts
- Command generation
- Educational command breakdown
- Command execution

Example generated command:

```bash
find . -name "*.py"
```

---

# Current Project Structure

```text
src/lx/
├── commands/
├── content/
├── tools/
│   ├── grep/
│   │   ├── learn.py
│   │   └── build.py
│   │
│   └── find/
│       ├── learn.py
│       └── build.py
│
├── ui/
└── cli.py
```

### Structure Philosophy

The structure intentionally mirrors the user experience.

Example:

```text
lx learn grep
        ↓
tools/grep/learn.py

lx build grep
        ↓
tools/grep/build.py
```

This design prioritizes clarity and discoverability over abstraction.

---

# Current Development Phase

Current Phase:

✅ grep vertical slice complete

✅ find vertical slice complete

🚧 Multi-command validation

Current focus:

- Implement curl
- Compare grep, find, and curl workflows
- Identify real duplication
- Discover patterns through implementation
- Continue improving educational value

Important:

Do not introduce abstractions unless multiple commands clearly benefit from them.

The project should continue following:

```text
Build first.

Learn from usage.

Extract abstractions later.
```

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

The project follows the same philosophy used throughout the author's other CLI projects.

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
- delay complexity until truly needed

---

# Success Criteria

lx succeeds if users gain confidence using real command-line tools.

A successful user should eventually feel comfortable typing:

```bash
grep -r "TODO" .
```

or:

```bash
find . -name "*.py"
```

instead of:

```bash
lx build grep
```

or:

```bash
lx build find
```

The objective is not dependency.

The objective is understanding.

The ideal outcome is that users eventually stop needing lx because they have learned the commands themselves.

---

# Next Major Milestone

Implement a third command:

```text
curl
```

and use it to answer an important question:

> What abstractions naturally emerge once lx supports multiple fundamentally different command-line tools?

The goal is not to build architecture.

The goal is to discover architecture through implementation.
