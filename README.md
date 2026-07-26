# lx

> _**Learn command-line tools by using real commands.**_

`lx` is an interactive CLI that helps developers learn command-line tools through guided usage.

Unlike traditional wrappers, `lx` does not hide the underlying command.

Instead, it intentionally exposes, explains, and executes real commands so users gradually become comfortable using them directly.

The goal is not dependency.

The goal is **understanding**.

A successful lx user eventually stops needing `lx` because they have internalized the commands themselves.

---

## Why?

Many developers feel comfortable with basic terminal navigation:

```bash
cd
ls
pwd
```

but less comfortable using tools such as:

```bash
grep
find
curl
jq
ssh
sed
awk
```

These tools are incredibly powerful, but learning them often involves reading documentation that is:

- syntax-heavy
- reference-oriented
- disconnected from real-world workflows

`lx` bridges that gap.

Instead of teaching commands through documentation alone, `lx` teaches them through:

- guided lessons
- practical examples
- interactive command builders
- real command execution

---

## Philosophy

### Don't Hide The Command

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

### Learn By Doing

Reading documentation is useful.

Running commands is better.

`lx` focuses on:

```text
Learn
→ Build
→ Understand
→ Run
```

The goal is active learning rather than passive reading.

---

### Build Confidence Gradually

Most command-line tools expose dozens or hundreds of options.

That can feel overwhelming.

`lx` introduces concepts incrementally through practical examples and guided workflows.

---

### Independence Over Dependency

Most software aims for long-term usage.

`lx` aims for the opposite.

Success is when a user naturally types:

```bash
grep -r "TODO" .
```

instead of:

```bash
lx build grep
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd lx
```

Install in editable mode:

```bash
pip install -e .
```

After installation:

```bash
lx
```

becomes available as a terminal command.

---

## Current Status

Current phase:

✅ grep complete

✅ find complete

✅ curl complete

✅ jq complete

Implemented:

- Learn mode
- Build mode
- Interactive command builders
- Real command generation
- Real command execution
- Command explanations
- Result explanations

Not yet implemented:

- Challenge mode
- Explain mode
- Command combinations
- Additional tools (ssh, sed, awk, etc.)

---

## Supported Commands

### grep

Search text.

Examples:

```bash
grep "TODO" file.py
```

```bash
grep -r "TODO" .
```

---

### find

Locate files and directories.

Examples:

```bash
find . -name "*.py"
```

```bash
find . -name "*.json"
```

---

### curl

Retrieve data from the internet.

Examples:

```bash
curl https://jsonplaceholder.typicode.com/todos/1
```

```bash
curl https://api.github.com
```

---

### jq

Explore and extract JSON data.

Examples:

```bash
jq .title
```

```bash
jq .completed
```

```bash
jq .
```

---

## Learn Mode

Learn what a command does.

Examples:

```bash
lx learn grep
```

```bash
lx learn find
```

```bash
lx learn curl
```

```bash
lx learn jq
```

Learn mode includes:

- Why Learn?
- Common Use Cases
- Examples
- Try It

Example:

```text
CURL - RETRIEVE DATA FROM THE INTERNET.

Why Learn?

  curl helps you retrieve data directly from your terminal.

Common Use Cases

  • Check what data an API returns
  • Download files

Examples

  curl https://api.github.com
```

---

## Build Mode

Build real commands interactively.

Examples:

```bash
lx build grep
```

```bash
lx build find
```

```bash
lx build curl
```

```bash
lx build jq
```

Example:

```text
Generated curl command

👉 curl "https://jsonplaceholder.typicode.com/todos/1"
```

---

### How Command Building Works

A build workflow typically follows this pattern:

```text
1. Ask simple questions

2. Generate a real command

3. Explain how to read the command

4. Optionally execute it

5. Explain the result
```

Example:

```text
Generated jq command

👉 jq .title
```

Followed by:

```text
How To Read This Command

jq
→ the tool we are using

.title
→ extract the title field from JSON data
```

Then:

```text
What came back?

delectus aut autem
```

And:

```text
What happened?

jq looked at the JSON data.

It extracted the 'title' field.

Only that value was returned.
```

---

## Example Learning Path

The current commands intentionally build on one another:

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

A user might naturally progress:

```text
curl
→ retrieve JSON

jq
→ extract values from JSON
```

For example:

```bash
curl https://jsonplaceholder.typicode.com/todos/1
```

followed by:

```bash
jq .title
```

---

## Planned Features

Potential future additions:

### Challenge Mode

Practice solving realistic problems.

Example:

```bash
lx challenge grep
```

Scenario:

```text
Find every TODO comment
inside the current project.
```

---

### Explain Mode

Understand commands you encounter elsewhere.

Example:

```bash
lx explain 'grep -r "TODO" .'
```

Output:

```text
grep
→ search text

-r
→ search all files underneath this directory

"TODO"
→ text we want to find

.
→ start searching here
```

---

### Command Combinations

Explore how tools work together.

Potential examples:

```bash
curl https://jsonplaceholder.typicode.com/todos/1 | jq .title
```

```bash
find . -name "*.py" | grep test
```

This would also introduce another important command-line concept:

```text
pipes*(|)
```

---

## Project Structure

```text
src/lx/
├── commands/
│
├─_ tools/
│ ├── grep/
│ │ ├── *earn.py
│ │ └── build.py
│ │*│ ├── find/
│ │ ├── learn.py*│ │ └── build.py
│ │
│ ├──*curl/
│ │ ├── learn.py
│ │ _└── build.py
│ │
│ └── jq/
│ _ ├── learn.py
│ └── build\*py
│
├── ui/
└── cli.py

```

The s*ructure intentionally mirrors the *ser experience:

```text
lx learn grep
        ↓
tools/grep/learn.py

lx build grep
        ↓
tools/grep*build.py
```

This approach prioritizes clarity and discoverability over abstraction.

---

## Goals

- M\*ke command-line tools approachable
- Reduce fear around terminal usage
- Teach through real commands
- Encourage experimentation
- Build user confidence
- Help developers become independent terminal users

---

## Non-Goals

- Replacing existing tools
- Hiding complexity
- Creating proprietary syntax
- Abstracting away commands
- Building a wrapper users depend on forever

---

## Inspiration

lx is inspired by the idea that the best learning happens through use.

The project teaches by generating and explaining real commands rather than hiding them.

A successful lx user eventually becomes comfortable using the underlying tools directly.

---

## Development Philosophy

Build first.

Learn from usage.

Extract abstractions later.
