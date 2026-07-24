# Repository Guidelines

## Structure

- Keep each reusable skill in its own top-level directory.
- Keep project-specific design decisions and screenshots out of reusable skills.
- Do not add auxiliary files such as `README.md` or changelogs inside a skill directory.
- Use the repository-level `README.md` for human-facing discovery and installation guidance.

## Updating a skill

- Read the complete `skill-creator` guidance before materially changing a skill.
- Keep `SKILL.md` concise and use `references/` for detailed conditional guidance.
- Keep every reference directly discoverable from `SKILL.md`.
- Update `agents/openai.yaml` when the skill's purpose or default invocation changes.
- Validate the skill with Codex's `quick_validate.py` before committing.
- Forward-test substantial workflow changes when a clean test environment is available.

## Git

- Keep commits focused and use short, present-tense messages.
- Do not commit credentials, generated caches, or project-specific private references.
