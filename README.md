# lx

> Learn command-line tools by using real commands.

lx is an interactive CLI that helps developers learn command-line tools through guided usage.

Unlike traditional wrappers, lx does not hide the underlying command.

Instead, it reveals it.

The goal is not to make developers dependent on lx.

The goal is for developers to eventually stop needing lx because they have internalized the commands themselves.

---

## Why?

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

## Philosophy

### Don't hide the command.

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

### Learn by doing.

Reading documentation is useful.

Running commands is better.

lx encourages hands-on learning with real commands on a real system.

---

### Build confidence gradually.

Most command-line tools expose a huge number of options.

That can feel overwhelming.

lx introduces concepts incrementally through practical examples.

---

### The ultimate goal is to stop using lx.

Success is when a user naturally types:

```bash
grep -r "TODO" .
```

instead of:

```bash
lx build grep
```

---

## Current Status

Current phase:

✅ Vertical Slice Complete

Implemented:

- `lx learn grep`
- `lx build grep`
- Real grep command generation
- Real grep command execution
- Command explanation

Not yet implemented:

- `find`
- `curl`
- `jq`
- Challenge Mode
- Explain Mode

---

## Features

### Learn

Learn what a command does and why it matters.

```bash
lx learn grep
```

Example output:

```text
GREP - SEARCH TEXT FOR PATTERNS.

Why Learn grep?

✓ Search source code
✓ Find TODO comments
✓ Investigate log files
✓ Locate configuration values
✓ Find references in projects

Common Use Cases

• Find TODO comments
• Search for error messages
• Search log files
• Locate code references
```

The goal is to provide practical context before introducing command syntax.

---

### Build

Build a real command interactively.

```bash
lx build grep
```

Example:

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

Explanation:

```text
grep        → search text

-r          → search recursively

"TODO"      → text to search for

.           → target file or directory
```

The generated command can optionally be executed immediately.

---

## Example Session

```bash
lx build grep
```

```text
Build a real grep command step by step.
```

```text
What text are you looking for?

> TODO
```

```text
Which file or directory should be searched?

> .
```

```text
Search recursively?

> y
```

```text
Generated grep command

👉 grep -r "TODO" .
```

```text
Run generated command?

> y
```

The command is executed and the results are shown directly in the terminal.

---

## Supported Commands

### Current

- grep

### Planned

- find
- curl
- jq

---

## Planned Modes

The long-term vision for lx includes four primary modes.

### Learn

Learn what a command does.

```bash
lx learn grep
```

### Build

Construct commands interactively.

```bash
lx build grep
```

### Challenge

Practice solving real command-line tasks.

```bash
lx challenge grep
```

### Explain

Understand existing commands.

```bash
lx explain 'grep -r "TODO" .'
```

These modes are not all implemented yet.

The current focus is improving Learn and Build workflows.

---

## Project Goals

- Make command-line tools approachable
- Remove fear around terminal usage
- Teach through real commands
- Encourage experimentation
- Help developers become independent terminal users

---

## Non-Goals

- Replacing existing tools
- Hiding complexity
- Creating proprietary syntax
- Abstracting away commands

---

## Inspiration

lx was inspired by the idea that the best learning happens through use.

The project takes inspiration from interactive tools that teach by generating real commands instead of hiding them.

Users should gradually become comfortable writing commands themselves.

A successful lx user should eventually no longer need lx.

---

## Current Focus

The immediate focus of the project is:

- Improving the grep learning experience
- Improving the grep command builder
- Discovering what common patterns emerge
- Building a solid foundation before adding additional commands

Only after the grep workflow feels genuinely useful will support for:

- find
- curl
- jq

be added.
