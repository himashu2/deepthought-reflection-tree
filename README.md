# DT Fellowship — R1 System Entry

## Daily Reflection Tree Agent

A deterministic system for structured end-of-day reflection, built as part of the DeepThought Fellowship assignment.

---

## Overview

Most reflection tools rely on free-form journaling or AI-generated suggestions. This project takes a different approach:

Reflection is not generated. It is designed.

The system guides users through a fixed decision tree where every path, question, and reflection is predefined. The outcome is consistent, explainable, and repeatable.

---

## What This Project Is

A command-line (CLI) application that:

* Guides users through a structured reflection flow
* Uses no AI or LLMs at runtime
* Produces deterministic outputs based on user choices

---

## Core Idea

The intelligence is not in the code. The intelligence is in the structure.

The Python agent is only a traversal engine. The actual system lives in:

```
reflection-tree.json
```

---

## System Axes

The reflection is structured across three dimensions:

1. Locus (Victim ↔ Victor)
   Where did control sit today?

2. Orientation (Entitlement ↔ Contribution)
   What were you optimizing for?

3. Radius (Self ↔ Others)
   Who was in your frame?

---

## System Flow

```
Start
  ↓
Locus
  ↓
Orientation
  ↓
Radius
  ↓
Summary
  ↓
End
```

---

## Architecture

```
User Input → Signal Generation → Decision Routing → Reflection → Summary
```

### Signal System

Each response contributes to a signal:

```
axis1: internal / external
axis2: contribution / entitlement
axis3: self / others
```

These signals determine branching, reflection type, and final summary.

### Deterministic Routing

Routing is rule-based:

```
IF axis1 = external → scenario A
IF axis1 = internal → scenario B
```

### Reflection Layer

* Pre-written reflections
* Context-aware
* Non-judgmental tone
* No hallucination

---

## Features

* Fully deterministic system
* No AI or LLM usage
* CLI-based interaction
* Signal-driven state handling
* Structured psychological modeling

---

## Project Structure

```
/tree/
  reflection-tree.json

/agent/
  agent.py

/transcripts/
  persona-1.md
  persona-2.md

README.md
write-up.md
```

---

## Running the Project

### Requirements

* Python 3.x

### Run

```
cd project
python agent.py
```

---

## Example Output

```
You said: "Waiting for clarity or direction"

You also said: "People were slowing things down"

Part of the day felt outside your control —
but part of it clearly wasn’t.

That gap is where agency lives.

---

Summary:

Locus: External
Orientation: Entitlement
Radius: Self

No score. No judgment.
Just a clearer picture.
```

---

## Psychological Foundations

* Locus of Control — Julian Rotter
* Growth Mindset — Carol Dweck
* Psychological Entitlement — W. Keith Campbell
* Self-Transcendence — Abraham Maslow

---

## Design Principles

* Structure over intelligence
* Determinism over probability
* Clarity over creativity

---

## What I Learned

Structure changes output more than intelligence.

---

## Constraints Followed

* No AI usage
* No randomness
* No free-text input
* Fully deterministic system

---

## Future Improvements

* Web-based interface
* Visualization of decision paths
* Deeper signal-based branching
* Reflection history tracking

---

## Final Note

This system is not designed to evaluate the user.

It is designed to help them see their own behavior more clearly.

---

DT Fellowship — R1 System Entry Submission






