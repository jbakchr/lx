# lx

> Learn command-line tools by using real commands.

lx is an interactive CLI that helps developers learn command-line tools through guided usage.

Unlike traditional wrappers, lx does not hide the underlying command.

Instead, it reveals it.

The goal is not to make developers dependent on lx.

The goal is for developers to eventually stop needing lx because they have internalized the commands themselves.

---

# Why?

Many developers know the basics of terminal navigation:

```bash
cd
ls
pwd
```

but feel less comfortable using commands such as:

```bash
grep
find
curl
jq
ssh
sed
awk
```

These tools are incredibly useful, but learning them often means reading documentation that focuses on syntax rather than practical usage.

lx aims to bridge that gap.

Instead of teaching commands through documentation alone, lx teaches them through:

- explanations
- examples
- guided command building
- real command execution

---

# Philosophy

## Don't Hide The Command

Many tools abstract complexity away.

lx does the opposite.

Every interaction should help the user understand the command being generated.

Example:

```text
Generated grep command

👉 grep -r "TODO" .
```

The command is not an implementation detail.

The command is the lesson.

---

## Learn By Doing

Reading documentation is useful.

Running commands is better.

lx encourages hands-on learning with real commands on a real system.

---

## Build Confidence Gradually

Most command-line tools expose a huge number of options.

That can feel overwhelming.

lx introduces concepts incrementally through practical examples.

---

## Independence Over Dependency

The ultimate goal is not long-term usage.

Success is when a user naturally types:

```bash
grep -r "TODO" .
```

instead of:

```bash
lx build grep
```

---

# Installation

Clone the repository and install in editable mode:

```bash
pip install -e .
```

After installation:

```bash
lx
```

becomes available as a terminal command.

---

# Current Status

Current phase:

✅ grep learning workflow complete

✅ find learning workflow complete

✅ second command workflow validated

Implemented:

- `lx learn grep`
- `lx build grep`
- `lx learn find`
- `lx build find`
- Real command generation
- Real command execution
- Interactive command builders
- Command breakdowns using "How To Read This Command"

Not yet implemented:

- curl
- jq
- ssh
- Challenge Mode
- Explain Mode

---

# Features

## Learn

Learn what a command does and why it matters.

Examples:

```bash
lx learn grep
```

```bash
lx learn find
```

Learn mode includes:

- Why Learn?
- Common Use Cases
- Examples
- Try It exercises

Example:

```text
FIND - LOCATE FILES AND DIRECTORIES.

Why Learn find?

✓ Find files by name
✓ Locate configuration files
✓ Search project directories
✓ Find specific file types

Common Use Cases

• Find Python files
• Locate config files
• Search large projects
```

---

## Build

Build real commands interactively.

Example:

```bash
lx build grep
```

```text
What text are you looking for?

> TODO

Which file or directory should be searched?

> .

Search recursively?

> y
```

Generated command:

```text
👉 grep -r "TODO" .
```

---

Example:

```bash
lx build find
```

```text
What file are you looking for?

> *.py

Which directory should be searched?

> .
```

Generated command:

```text
👉 find . -name "*.py"
```

---

## Command Breakdown

Before execution, lx explains how to read the command.

Example:

```text
How To Read This Command

find
→ the tool we are using

.
→ start searching from this location

-name
→ search by file name

"*.py"
→ file name pattern
```

The goal is not just command execution.

The goal is understanding.

---

# Example Session

```bash
lx build grep
```

Output:

```text
Build a real grep command step by step.

What text are you looking for?

> TODO

Which file or directory should be searched?

> .

Search recursively?

> y

Generated grep command

👉 grep -r "TODO" .

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

The generated command can then be executed directly from lx.

---

# Supported Commands

## Current

- grep
- find

## Planned

- curl
- jq
- ssh

---

# Planned Modes

The long-term vision for lx includes four primary modes.

## Learn

Learn what a command does.

```bash
lx learn grep
```

---

## Build

Construct commands interactively.

```bash
lx build grep
```

---

## Challenge

Practice solving realistic command-line problems.

```bash
lx challenge grep
```

Example:

```text
Find every TODO comment in the current project.

What command would you use?
```

---

## Explain

Understand commands you encounter elsewhere.

```bash
lx explain 'grep -r "TODO" .'
```

These modes are not all implemented yet.

The current focus remains Learn and Build.

---

# Project Structure

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

The structure intentionally mirrors the user experience:

```text
lx learn grep
lx build grep

lx learn find
lx build find
```

The project favors clarity and explicitness over abstractions.

---

# Project Goals

- Make command-line tools approachable
- Reduce fear around terminal usage
- Teach through real commands
- Encourage experimentation
- Help developers become independent terminal users

---

# Non-Goals

- Replacing existing tools
- Hiding complexity
- Creating proprietary syntax
- Abstracting away commands
- Building a command wrapper that users depend on forever

---

# Inspiration

lx is inspired by the idea that the best learning happens through use.

The project takes inspiration from interactive tools that teach by generating real commands instead of hiding them.

Users should gradually become comfortable writing commands themselves.

A successful lx user should eventually no longer need lx.

---

# Current Focus

The immediate focus of the project is:

- Learn from implementing multiple tools
- Compare grep and find workflows
- Discover patterns through usage
- Avoid premature abstractions
- Continue improving educational value

Future work may include:

- curl
- jq
- ssh
- Challenge Mode
- Explain Mode

The project follows a simple principle:

> Build first.
>
> Learn from usage.
>
> Extract abstractions later.