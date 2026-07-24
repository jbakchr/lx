# lx - ROADMAP

> Learn command-line tools by using real commands.

This roadmap intentionally prioritizes learning, simplicity, and iterative development.

The goal is not to build a large framework.

The goal is to help developers gain confidence using real command-line tools through guided exploration, command construction, and hands-on practice.

---

## Current Phase

✅ Phase 0: Project Definition

✅ Phase 1A: grep Vertical Slice

🚧 Phase 1B: Improve grep Experience (Current)

---

## Guiding Principles

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

## Phase 0: Project Definition

### Status

✅ Completed

### Completed Work

- [x] Define project purpose
- [x] Define philosophy
- [x] Create README
- [x] Create ROADMAP
- [x] Create PROJECT_CONTEXT
- [x] Create repository

### Exit Criteria

✅ Complete

---

## Phase 1A: grep Vertical Slice

### Goal

Validate the core lx learning experience with a single command.

The focus is not architecture.

The focus is proving that:

```bash
lx learn grep
```

and

```bash
lx build grep
```

feel useful.

### Completed Work

#### Core CLI

- [x] Create Typer application
- [x] Add Rich output
- [x] Add command groups

#### Learn Mode

- [x] Implement `lx learn grep`
- [x] Add purpose section
- [x] Add examples
- [x] Add common use cases
- [x] Add practical exercise

#### Build Mode

- [x] Implement `lx build grep`
- [x] Interactive prompts
- [x] Generate grep command
- [x] Explain generated command
- [x] Execute generated command

#### Lessons Learned

- Build before abstracting
- Let duplication reveal architecture
- Learning experience matters more than framework design
- Real command execution provides immediate feedback

### Exit Criteria

✅ Complete

Users can run:

```bash
lx learn grep
```

and

```bash
lx build grep
```

and execute a real generated grep command.

---

## Phase 1B: Improve grep Experience

### Status

🚧 Current Phase

### Goal

Refine the grep workflow through real usage.

Focus on usability and learning value.

Do not add new commands until grep feels genuinely useful.

### Learn Improvements

- [ ] Improve visual formatting
- [ ] Improve section hierarchy
- [ ] Improve command highlighting
- [ ] Add common mistakes section
- [ ] Add related commands section

### Build Improvements

- [ ] Improve explanation formatting
- [ ] Improve command preview formatting
- [ ] Improve execution output formatting
- [ ] Better handling of large grep results
- [ ] Better handling of binary files
- [ ] Better defaults for search targets

### grep Options

- [ ] Ignore case (`-i`)
- [ ] Whole word match (`-w`)
- [ ] Show line numbers (`-n`)
- [ ] Invert matches (`-v`)

### Exit Criteria

The grep workflow feels genuinely useful during daily usage.

---

## Phase 1C: Extract Emerging Patterns

### Goal

Extract shared functionality only after grep has matured.

Avoid premature abstractions.

### Possible Infrastructure

- [ ] Shared formatter utilities
- [ ] Shared command display helper
- [ ] Shared explanation helper
- [ ] Shared section rendering
- [ ] Example rendering helper

### Important

Only build abstractions that have emerged from actual duplication.

### Exit Criteria

The codebase becomes easier to maintain without becoming more complex.

---

## Phase 2: Additional Commands

### Goal

Apply lessons learned from grep to other commands.

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

### Exit Criteria

Each command supports both:

```bash
lx learn <command>
```

and

```bash
lx build <command>
```

---

## Phase 3: Learn Mode Expansion

### Goal

Create a richer learning experience.

### Improvements

- [ ] Common mistakes
- [ ] Related commands
- [ ] Expanded examples
- [ ] Real-world workflows
- [ ] Suggested next command to learn

### Exit Criteria

Every supported command teaches:

- Purpose
- Use cases
- Examples
- Common mistakes
- Related commands

---

## Phase 4: Challenge Mode

### Goal

Allow developers to practice independently.

### Challenge Engine

- [ ] Generate challenges
- [ ] Provide hints
- [ ] Validate answers
- [ ] Reveal solutions

### Supported Commands

- [ ] grep
- [ ] find
- [ ] curl
- [ ] jq

### Exit Criteria

Users can learn by solving realistic command-line tasks.

---

## Phase 5: Explain Mode

### Goal

Help users understand commands they encounter elsewhere.

Example:

```bash
lx explain 'grep -r "TODO" .'
```

Output:

```text
grep      → search text

-r        → search recursively

"TODO"    → search pattern

.         → target directory
```

### Features

- [ ] Parse commands
- [ ] Explain flags
- [ ] Explain arguments
- [ ] Explain common options

### Exit Criteria

Users can understand commands copied from tutorials or documentation.

---

## Phase 6: Extended Commands

### Goal

Expand beyond the initial learning set.

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

### Exit Criteria

Additional commands follow the same learn / build / challenge / explain model.

---

## Phase 7: Release Preparation

### Goal

Prepare lx for broader use.

### Distribution

- [ ] Add pyproject.toml
- [ ] Add version command
- [ ] Install via pip
- [ ] PyPI release

### Documentation

- [ ] Installation guide
- [ ] Screenshots
- [ ] Example sessions

### Polish

- [ ] Help output
- [ ] Error handling
- [ ] Consistent formatting

### Exit Criteria

A new developer can install lx and learn their first command within minutes.

---

## Ideas Parking Lot

Ideas that sound interesting but are intentionally deferred.

### Future Ideas

- [ ] Command history
- [ ] Learning progress
- [ ] Learning streaks
- [ ] AI-generated challenges
- [ ] Interactive tutorials
- [ ] Shell scripting lessons
- [ ] Linux fundamentals lessons

---

## Success Definition

lx succeeds when users gradually stop needing it.

A successful user should eventually feel comfortable typing:

```bash
grep -r "TODO" .
```

instead of:

```bash
lx build grep
```

The goal is not dependency.

The goal is confidence.