# lx - PROJECT_CONTEXT.md

> Learn command-line tools by using real commands.

---

# Project Overview

lx is a CLI tool designed to help developers learn command-line tools through guided, interactive usage.

Unlike traditional wrappers, lx does not hide underlying commands.

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

Bad:

```bash
lx search todo
```

Good:

```text
Generated grep command

👉 grep -r "TODO" .
```

Users should always see the real command they are learning.

---

## Learn By Doing

lx prioritizes:

- interaction
- experimentation
- execution

over passive reading.

The ideal learning flow is:

```text
Learn
→ Build
→ Understand
→ Run
```

---

## Confidence Over Abstraction

Many tools reduce complexity by hiding it.

lx should reduce fear without hiding complexity.

The goal is not:

```text
Never learn grep.
```

The goal is:

```text
Learn grep gradually.
```

---

## Independence Over Dependency

Most software aims for long-term usage.

lx aims for the opposite.

A successful user eventually stops using lx because they have learned the commands themselves.

---

# Most Important Discoveries

## Discovery #1

Build before abstracting.

The original idea was to plan infrastructure and abstractions early.

Actual development showed that building complete command-learning experiences first led to much better decisions.

This remains a core project principle.

---

## Discovery #2

Educational explanations outperform technical explanations.

Bad:

```text
-r
→ recursive
```

Good:

```text
-r
→ search all files underneath this directory
```

Users care more about understanding what a command does than memorizing flag names.

---

## Discovery #3

Project structure should mirror user workflows.

Example:

```text
lx learn grep
        ↓
tools/grep/learn.py

lx build grep
        ↓
tools/grep/build.py
```

This remains one of the most successful decisions in the project.

---

## Discovery #4

Far fewer abstractions are needed than originally expected.

After implementing:

```text
grep
find
curl
jq
```

very little shared architecture emerged.

The workflow is similar:

```text
Ask questions
↓
Generate command
↓
Explain command
↓
Execute command
↓
Explain result
```

but the educational content remains highly tool-specific.

Current conclusion:

```text
Avoid abstractions unless repeated pain appears.
```

---

# Current Scope

## Version 0.1

Current supported commands:

```text
grep
find
curl
jq
```

Current status:

```text
✅ grep learn
✅ grep build

✅ find learn
✅ find build

✅ curl learn
✅ curl build

✅ jq learn
✅ jq build
```

Current command progression:

```text
grep
→ search text

find
→ locate files

curl
→ retrieve data

jq
→ extract data
```

This progression is intentional and currently forms the core lx learning path.

---

# Current Learn Structure

All Learn lessons currently follow:

```text
Why Learn?

Common Use Cases

Examples

Try It
```

Example:

```bash
lx learn curl
```

```text
CURL - RETRIEVE DATA FROM THE INTERNET.

Why Learn?

Common Use Cases

Examples

Try It
```

The current lesson size should ideally fit within a single visible terminal screen.

---

# Current Build Structure

Build mode is currently the most important lx experience.

Typical flow:

```text
1. Ask questions

2. Generate command

3. How To Read This Command

4. Optional execution

5. What Came Back?

6. What Happened?
```

Example:

```text
Generated curl command

👉 curl "https://jsonplaceholder.typicode.com/todos/1"
```

Followed by:

```text
How To Read This Command

curl
→ make an HTTP request

https://...
→ the address we want to contact
```

Followed by:

```text
What came back?
```

and:

```text
What happened?
```

---

# Current Command Status

## grep

Status:

```text
✅ learn complete
✅ build complete
```

Teaches:

```text
Search text.
```

---

## find

Status:

```text
✅ learn complete
✅ build complete
```

Teaches:

```text
Locate files and directories.
```

---

## curl

Status:

```text
✅ learn complete
✅ build complete
```

Teaches:

```text
Retrieve data from the internet.
```

Example command:

```bash
curl https://jsonplaceholder.typicode.com/todos/1
```

---

## jq

Status:

```text
✅ learn complete

✅ build functional

🚧 build experience not yet considered fully polished
```

Teaches:

```text
Explore and extract JSON data.
```

Example command:

```bash
jq .title
```

Current build workflow uses example JSON data and demonstrates field extraction.

Future improvements remain possible.

---

# Known Improvement Areas

## jq Build Experience

Current jq build experience works well but is not yet fully polished.

Current concerns:

- example data is hardcoded
- result presentation could improve
- educational explanations could evolve
- field extraction is intentionally very simple

Current status:

```text
✅ Functional

🚧 Not considered finished
```

---

# Current Project Structure

```text
src/lx/
├── commands/
│
├── tools/
│   ├── grep/
│   │   ├── learn.py
│   │   └── build.py
│   │
│   ├── find/
│   │   ├── learn.py
│   │   └── build.py
│   │
│   ├── curl/
│   │   ├── learn.py
│   │   └── build.py
│   │
│   └── jq/
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

This approach prioritizes clarity and discoverability over abstraction.

---

# Future Directions

These ideas are currently being explored.

Nothing here is committed.

---

## lx combine

Purpose:

Teach how command-line tools work together.

Possible examples:

```bash
curl https://jsonplaceholder.typicode.com/todos/1 | jq .title
```

```bash
find . -name "*.py" | grep test
```

Educational concept:

```text
pipes (|)
```

Current thinking:

This feels like one of the most promising future additions because it teaches how real-world command-line workflows are constructed.

---

## lx flags <tool>

Purpose:

Help users discover useful command options.

Example:

```bash
lx flags grep
```

Important:

The exact purpose of this command remains undefined.

An open question:

Should this teach:

```text
flags
```

or:

```text
common command patterns
```

?

Current concern:

A flag-focused feature risks becoming documentation rather than learning.

Further exploration is required before implementation.

---

## Challenge Mode

Example:

```bash
lx challenge grep
```

Purpose:

Allow users to practice and apply their knowledge.

Current status:

```text
Planned
```

---

## Explain Mode

Example:

```bash
lx explain 'grep -r "TODO" .'
```

Purpose:

Help users understand commands they encounter elsewhere.

Current status:

```text
Planned
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
curl https://jsonplaceholder.typicode.com/todos/1 | jq .title
```

without needing lx.

The objective is not dependency.

The objective is understanding.

---

# Current Development Focus

Current focus:

```text
Polish existing commands

Improve jq build experience

Evaluate command-combination learning

Continue improving educational value
```

Remember:

```text
Build first.

Learn from usage.

Extract abstractions later.
```
