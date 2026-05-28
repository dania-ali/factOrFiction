# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fact or Fiction is a Flask web app that helps students evaluate the credibility of online claims, headlines, and social media posts. Users submit a claim and receive a credibility analysis based on factors like emotional language, evidence, source quality, and bias indicators. It is a lightweight educational tool for media literacy.

## Stack

- Python 3.10+, Flask 3.x, Jinja2 templates
- Vanilla HTML/CSS, optional lightweight JavaScript
- pytest for testing

## Commands

```bash
# Run the app
python app.py
# → http://localhost:5000

# Run all tests
pytest

# Run tests for a single task
pytest tests/test_task_01.py
```

## Architecture

- Each task maps to a `tests/test_task_NN.py` file — treat tests as the specification.
- Flask routes should stay thin; move reusable logic into helper functions.
- Credibility analysis logic (emotional language, evidence, source quality, bias indicators) lives in helper functions, not inside route handlers.
- HTML lives in Jinja2 templates; keep them clean and organized.

## Conventions

- Read the task test file before implementing anything.
- Run `pytest` after each meaningful code change.
- Use small, focused functions with descriptive names.
- Prefer readable, beginner-friendly code over clever implementations.
- Handle invalid user input gracefully.

## Constraints

- Do not edit files inside `tests/`.
- Do not add new dependencies without asking first.
- Do not introduce databases, authentication, or a different framework.
- Do not refactor unrelated code during a task.
- Do not overengineer — this is an MVP.

## Definition of Done

The MVP is complete when a user can submit a claim, receive a credibility score with explanation, view basic responsive styling, and all pytest tests pass.
