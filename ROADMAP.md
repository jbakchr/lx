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

# Current Phase

✅ Phase 0: Project Definition

✅ Phase 1A: grep Vertical Slice

✅ Phase 1B: grep Experience Improvements

✅ Phase 1C: find Vertical Slice

🚧 Phase 1D: Multi-Command Validation (Current)

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

## Goal

Validate the core lx learning experience with a single command.

The focus was not architecture.

The focus was proving that:

```bash
lx learn grep
```

and

```bash
lx build grep
```

feel useful.

## Completed Work

### Core CLI

- Create Typer application
- Add Rich output
- Add command routing

### Learn Mode

- Implement `lx learn grep`
- Add purpose section
- Add common use cases
- Add examples
- Add try-it exercise

### Build Mode

- Implement `lx build grep`
- Interactive prompts
- Generate grep command
- Explain generated command
- Execute generated command

## Lessons Learned

- Build before abstracting
- Learning experience matters more than architecture
- Real command execution creates immediate feedback
- Generated commands should be visible

## Exit Criteria

✅ Complete

---

# Phase 1B: grep Experience Improvements

## Status

✅ Complete

## Completed Work

### Formatting

- Improve output readability
- Improve section hierarchy
- Improve command presentation

### Learning Experience

- Replace technical explanations with:
  - "How To Read This Command"
- Emphasize understanding over syntax
- Improve generated command explanations

### Project Structure

- Extract command-specific logic
- Split grep into:
  - `learn.py`
  - `build.py`

## Lessons Learned

- Educational explanations outperform technical descriptions
- Command breakdowns help users remember commands
- Structure should mirror user workflows

## Exit Criteria

✅ Complete

---

# Phase 1C: find Vertical Slice

## Status

✅ Complete

## Goal

Validate that the lx architecture works for a second command.

## Completed Work

### Learn Mode

Implemented:

```bash
lx learn find
```

Includes:

- Why Learn?
- Common Use Cases
- Examples
- Try It

### Build Mode

Implemented:

```bash
lx build find
```

Includes:

- Interactive prompts
- Command generation
- Command breakdown
- Command execution

### Generated Command Example

```bash
find . -name "*.py"
```

### Command Breakdown Example

```text
find
→ the tool we are using

.
→ start searching from this location

-name
→ search by file name

"*.py"
→ file name pattern
```

## Lessons Learned

- The existing architecture works well for additional tools
- Tool-specific workflows are more important than shared abstractions
- Consistency improves learning

## Exit Criteria

✅ Complete

---

# Phase 1D: Multi-Command Validation

## Status

🚧 Current Phase

## Goal

Implement a third command and observe what architecture naturally emerges.

The purpose is not to build abstractions.

The purpose is to discover patterns.

## Candidate Commands

### curl

Preferred next command.

Potential learn mode:

```bash
lx learn curl
```

Potential build mode:

```bash
lx build curl
```

Example generated command:

```bash
curl https://api.github.com
```

### jq

Potential follow-up after curl.

### ssh

Candidate after curl and jq.

## Questions To Answer

What functionality is genuinely shared?

Examples:

- command rendering
- command execution
- command breakdown formatting
- lesson structure

What functionality remains tool-specific?

Examples:

- prompts
- generated commands
- explanations
- learning content

## Exit Criteria

A third command exists and architectural patterns become obvious.

---

# Phase 2: Learn Mode Expansion

## Goal

Create richer learning experiences.

## Improvements

- Common mistakes
- Related commands
- Expanded examples
- Real-world workflows
- Suggested next command

## Example

For grep:

```text
Common mistakes

grep TODO .

Why doesn't this work?

Because . is a directory.

Try:

grep -r TODO .
```

## Exit Criteria

Every supported command teaches:

- Purpose
- Use cases
- Examples
- Try It
- Common mistakes
- Related commands

---

# Phase 3: Challenge Mode

## Goal

Allow users to practice independently.

## Example

```bash
lx challenge grep
```

Output:

```text
Find every TODO comment in the current project.

What command would you use?
```

## Planned Features

- Challenges
- Hints
- Solutions
- Answer validation

## Exit Criteria

Users can practice commands through realistic scenarios.

---

# Phase 4: Explain Mode

## Goal

Help users understand commands they encounter elsewhere.

Example:

```bash
lx explain 'grep -r "TODO" .'
```

Potential output:

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

## Planned Features

- Parse commands
- Explain flags
- Explain arguments
- Explain common options

## Exit Criteria

Users can understand commands copied from tutorials or documentation.

---

# Phase 5: Extended Commands

## Goal

Expand beyond the initial learning set.

## High Priority

- curl
- jq
- ssh

## Medium Priority

- tar
- xargs

## Future

- sed
- awk
- git
- docker

## Exit Criteria

Additional commands support:

```bash
lx learn <command>
```

and

```bash
lx build <command>
```

---

# Phase 6: Release Preparation

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

Interesting ideas that are intentionally deferred.

## Future Ideas

- Command history
- Learning progress
- Learning streaks
- AI-generated challenges
- Interactive tutorials
- Shell scripting lessons
- Linux fundamentals lessons

---

# Success Definition

lx succeeds when users gradually stop needing it.

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

The goal is not dependency.

The goal is confidence.

---

# Development Philosophy

Build first.

Learn from usage.

Extract abstractions later.
