# ROADMAP.md

# lx Roadmap

> Learn command-line tools by using real commands.

This roadmap intentionally prioritizes learning, simplicity, and iterative development.

The goal is not to build a large framework.

The goal is to help developers gain confidence using real command-line tools through guided exploration, command construction, and hands-on practice.

---

# Current Phase

✅ Phase 0: Project Definition

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

## Goals

- [x] Define project purpose
- [x] Define philosophy
- [x] Create README
- [x] Create roadmap
- [x] Create PROJECT_CONTEXT.md
- [x] Create repository

## Exit Criteria

- Clear vision exists
- Project documentation exists
- First development phase identified

---

# Phase 1: Foundation (MVP)

Goal:

Build the smallest possible version of lx.

Focus on architecture and one complete command-learning workflow.

## Core CLI

- [ ] Create Typer application
- [ ] Add Rich output
- [ ] Add command groups
- [ ] Add help screens
- [ ] Add version command

## Initial Commands

### grep

- [ ] learn grep
- [ ] build grep
- [ ] execute generated grep command

### find

- [ ] learn find
- [ ] build find
- [ ] execute generated find command

### curl

- [ ] learn curl
- [ ] build curl
- [ ] execute generated curl command

### jq

- [ ] learn jq
- [ ] build jq
- [ ] execute generated jq command

## Supporting Infrastructure

- [ ] Command definition model
- [ ] Command explanation model
- [ ] Example system
- [ ] Shared formatter utilities

## Exit Criteria

User can:

```bash
lx learn grep
```

and

```bash
lx build grep
```

and run a real generated command.

---

# Phase 2: Learn Mode

Goal:

Create a high-quality learning experience.

Focus on explanations rather than execution.

## Learn Command

- [ ] Consistent layouts
- [ ] Purpose section
- [ ] Common use cases
- [ ] Examples section
- [ ] Related commands section

## Supported Tools

- [ ] grep
- [ ] find
- [ ] curl
- [ ] jq

## Improvements

- [ ] Better formatting
- [ ] Syntax highlighting
- [ ] Example command walkthroughs

## Exit Criteria

Every supported tool has:

- Purpose
- Examples
- Common use cases
- Common mistakes

---

# Phase 3: Build Mode

Goal:

Turn command construction into an interactive learning experience.

## Interactive Builders

### grep

- [ ] Search text
- [ ] Recursive search
- [ ] Ignore case
- [ ] File targeting

### find

- [ ] File names
- [ ] File extensions
- [ ] Directory targeting

### curl

- [ ] GET requests
- [ ] Headers
- [ ] Query parameters

### jq

- [ ] Property selection
- [ ] Nested properties
- [ ] Array access

## Improvements

- [ ] Preview generated command
- [ ] Explain generated command
- [ ] Optional execution

## Exit Criteria

Users can construct useful commands without reading documentation.

---

# Phase 4: Challenge Mode

Goal:

Help users practice independently.

## Challenge Engine

- [ ] Generate challenge
- [ ] Validate answer
- [ ] Give hints
- [ ] Show solution

## grep Challenges

- [ ] Beginner
- [ ] Intermediate
- [ ] Advanced

## find Challenges

- [ ] Beginner
- [ ] Intermediate
- [ ] Advanced

## curl Challenges

- [ ] Beginner
- [ ] Intermediate
- [ ] Advanced

## jq Challenges

- [ ] Beginner
- [ ] Intermediate
- [ ] Advanced

## Exit Criteria

Users can practice commands repeatedly without external resources.

---

# Phase 5: Explain Mode

Goal:

Explain existing commands.

Example:

```bash
lx explain 'grep -r "TODO" src/'
```

Output:

```text
grep      → search text
-r         → recursive search
"TODO"     → search pattern
src/       → target directory
```

## Features

- [ ] Parse command
- [ ] Explain arguments
- [ ] Explain flags
- [ ] Explain common options

## Supported Tools

- [ ] grep
- [ ] find
- [ ] curl
- [ ] jq

## Exit Criteria

Users can understand commands they encounter online.

---

# Phase 6: Extended Commands

Goal:

Expand beyond the initial learning set.

## Candidate Commands

### High Priority

- [ ] ssh
- [ ] tar
- [ ] xargs

### Medium Priority

- [ ] sed
- [ ] awk

### Future

- [ ] git
- [ ] docker

## Exit Criteria

Additional commands follow the same learn/build/challenge/explain model.

---

# Phase 7: Content Expansion

Goal:

Increase educational value.

## Examples

- [ ] More examples
- [ ] Real-world scenarios
- [ ] Common workflows

## Teaching

- [ ] Beginner paths
- [ ] Suggested learning order
- [ ] Related command recommendations

## Exit Criteria

Users have a clear progression path through lx.

---

# Phase 8: Release Preparation

Goal:

Prepare lx for broader usage.

## Polish

- [ ] Improve help output
- [ ] Improve documentation
- [ ] Improve onboarding

## Packaging

- [ ] PyPI release
- [ ] Installation instructions
- [ ] Versioning strategy

## Repository

- [ ] Screenshots
- [ ] GIF demonstrations
- [ ] Example workflows

## Exit Criteria

A new user can install lx and learn their first command within minutes.

---

# Ideas Parking Lot

Ideas that sound interesting but are intentionally deferred.

## Possible Future Features

- [ ] Command history
- [ ] Progress tracking
- [ ] Learning streaks
- [ ] AI-generated challenges
- [ ] Interactive tutorials
- [ ] Command comparison mode
- [ ] Shell scripting lessons
- [ ] Linux fundamentals lessons

---

# Success Definition

lx succeeds when users gradually stop needing it.

A successful user should eventually feel comfortable typing:

```bash
grep -r "TODO" src/
```

instead of:

```bash
lx build grep
```

The goal is not dependency.

The goal is confidence.
