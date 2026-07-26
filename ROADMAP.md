# lx - ROADMAP

> Learn command-line tools by using real commands.

This roadmap intentionally prioritizes:

- learning
- simplicity
- incremental development
- real-world usage

The goal is not to build a framework.

The goal is to help developers gain confidence using real command-line tools through guided exploration, command construction, and hands-on practice.

---

# Current Status

✅ Phase 0: Project Definition

✅ Phase 1A: grep Vertical Slice

✅ Phase 1B: grep Experience Improvements

✅ Phase 1C: find Vertical Slice

✅ Phase 1D: Multi-Command Validation

🚧 Phase 1E: Polish And Refinement (Current)

---

# Guiding Principles

When making decisions, prefer:

- Simplicity over completeness
- Learning over abstraction
- Real commands over custom syntax
- Small releases over large releases
- Hands-on practice over documentation alone

Always ask:

> Does this help the user learn the underlying command?

If the answer is no, reconsider the feature.

---

# Phase 0: Project Definition

## Status

✅ Complete

## Completed Work

- Define project purpose
- Define philosophy
- Create README
- Create ROADMAP
- Create PROJECT_CONTEXT
- Create repository

## Exit Criteria

✅ Complete

---

# Phase 1A: grep Vertical Slice

## Status

✅ Complete

## Completed Work

### Learn Mode

Implemented:

```text
lx learn grep
```

### Build Mode

Implemented:

```text
lx build grep
```

### Lessons Learned

- Build before abstracting
- Educational value matters more than architecture
- Real command execution creates immediate feedback

## Exit Criteria

✅ Complete

---

# Phase 1B: grep Experience Improvements

## Status

✅ Complete

## Completed Work

- Improved formatting
- Improved command presentation
- Added educational command breakdowns
- Added "How To Read This Command"

## Lessons Learned

- Educational explanations outperform technical descriptions
- Learning-focused explanations improve retention

## Exit Criteria

✅ Complete

---

# Phase 1C: find Vertical Slice

## Status

✅ Complete

## Completed Work

Implemented:

```text
lx learn find
lx build find
```

### Lessons Learned

- Existing structure works well for additional commands
- Consistency improves learning
- Tool-specific workflows matter more than abstractions

## Exit Criteria

✅ Complete

---

# Phase 1D: Multi-Command Validation

## Status

✅ Complete

## Goal

Validate that lx can support fundamentally different command-line tools without needing significant architectural changes.

## Completed Work

### curl

Implemented:

```text
lx learn curl
lx build curl
```

Teaches:

```text
Retrieve data from the internet.
```

### jq

Implemented:

```text
lx learn jq
lx build jq
```

Teaches:

```text
Explore and extract JSON data.
```

### Educational Progression

The current commands now form a coherent learning path:

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

## Lessons Learned

The most surprising discovery:

```text
Very little shared architecture was needed.
```

The workflow remains:

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

while the educational content remains highly tool-specific.

## Exit Criteria

✅ Complete

---

# Phase 1E: Polish And Refinement

## Status

🚧 Current Phase

## Goal

Strengthen and refine the current learning experience before adding major new functionality.

## Current Areas

### jq Build Experience

Current implementation works well but is not yet considered fully polished.

Areas for future improvement:

- Better result presentation
- Better handling of different field types
- Stronger educational explanations
- More realistic JSON examples

### General Consistency

Continue improving:

- Output formatting
- Visual consistency
- Section hierarchy
- Command explanations
- Result explanations

## Exit Criteria

Current command set feels polished and internally consistent.

---

# Phase 2: Command Combinations

## Goal

Teach how real command-line tools work together.

Many powerful terminal workflows combine multiple commands.

Example:

```bash
curl https://jsonplaceholder.typicode.com/todos/1 | jq .title
```

### Potential Command

```bash
lx combine
```

or:

```bash
lx combine curl jq
```

### Educational Goals

Teach:

```text
pipes (|)
```

and:

```text
tool composition
```

Example:

```text
curl
→ retrieve JSON

|

→ pass output to another command

jq
→ extract a field
```

## Candidate Combinations

```bash
curl ... | jq .title
```

```bash
find . -name "*.py" | grep test
```

```bash
find . -name "*.log" | xargs grep ERROR
```

## Exit Criteria

Users understand that command-line power often comes from combining tools.

---

# Phase 3: Command Discovery

## Goal

Help users discover useful command patterns and flags.

## Potential Command

```bash
lx flags <tool>
```

Example:

```bash
lx flags grep
```

### Open Question

Should this focus on:

```text
Flags
```

or:

```text
Common command patterns
```

?

This still needs to be defined.

Current concern:

A flags-focused command may accidentally become documentation rather than learning.

Possible alternative:

```bash
lx recipes grep
```

or:

```bash
lx patterns grep
```

### Questions To Answer

What is more useful?

```text
-r
-i
-n
-c
```

or:

```text
Find TODO comments

Show line numbers

Ignore case
```

This remains intentionally undecided.

## Exit Criteria

Users can discover useful command variations without reading a man page.

---

# Phase 4: Challenge Mode

## Goal

Allow users to practice independently.

Example:

```bash
lx challenge grep
```

Output:

```text
Find every TODO comment
inside the current project.

What command would you use?
```

### Planned Features

- Challenges
- Hints
- Solutions
- Answer validation

## Exit Criteria

Users can practice commands through realistic scenarios.

---

# Phase 5: Explain Mode

## Goal

Help users understand commands they encounter elsewhere.

Example:

```bash
lx explain 'grep -r "TODO" .'
```

### Example Output

```text
grep
→ search text

-r
→ search all files underneath this directory

"TODO"
→ the text we want to find

.
→ start searching here
```

### Planned Features

- Explain flags
- Explain arguments
- Explain pipes
- Explain common command structures

## Exit Criteria

Users can paste commands and understand how to read them.

---

# Phase 6: Extended Commands

## Goal

Continue expanding the learning library.

## High Priority

```text
ssh
```

Reason:

Introduces remote systems and connectivity.

## Medium Priority

```text
tar
xargs
```

Reason:

Natural follow-ups to existing workflows.

## Future

```text
sed
awk
git
docker
```

## Exit Criteria

Additional commands support:

```text
lx learn <command>
lx build <command>
```

---

# Phase 7: Release Preparation

## Goal

Prepare lx for broader usage.

## Distribution

- Version command
- PyPI release

## Documentation

- Installation guide
- Screenshots
- Example sessions

## Polish

- Help output
- Error handling
- Consistent formatting

## Exit Criteria

A new developer can install lx and learn a command within minutes.

---

# Ideas Parking Lot

Interesting ideas intentionally deferred.

## Future Ideas

- Learning progress
- Learning streaks
- AI-generated challenges
- Shell scripting lessons
- Linux fundamentals lessons
- Curated learning paths

---

# Success Definition

lx succeeds when users gradually stop needing it.

A successful user should eventually feel comfortable typing:

```bash
grep -r "TODO" .
```

or:

```bash
curl https://jsonplaceholder.typicode.com/todos/1 | jq .title
```

instead of:

```bash
lx build grep
```

or:

```bash
lx build jq
```

The goal is not dependency.

The goal is confidence.

---

# Development Philosophy

Build first.

Learn from usage.

Extract abstractions later.
