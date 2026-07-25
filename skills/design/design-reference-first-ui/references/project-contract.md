# Project Design Contract

Use this reference to discover the design evidence available in a repository and to recognize what is missing.

## Discovery order

1. Read repository instructions such as `AGENTS.md`.
2. Find the design entry point and documentation index.
3. Find the project visual language or brand/product principles.
4. Find the reference source map, approved inspiration, and recorded no-transfer decisions.
5. Find UI patterns, screen archetypes, flow guidance, and component usage guidance.
6. Find design tokens and reusable component source.
7. Find golden screenshots, previews, snapshot tests, demos, and story catalogs.
8. Inspect the nearest surfaces, complete flow, sibling components, and unrelated product-defining screens.
9. Find prior design decisions and unresolved gaps.

Use fast repository search and adapt to local naming. Do not require a `docs/design` directory or any exact filename.

## Evidence strength

Treat project evidence in this order:

1. Explicitly approved golden screens and documented patterns
2. Current visual-language and component guidance
3. Repeated, consistent production implementations
4. Isolated current implementation
5. Unreviewed experiments, previews, plans, or old screenshots

Existing code may contain accidental framework defaults or unresolved inconsistencies. Do not copy it merely because it exists.

Evaluate evidence per visual decision. A screen can be approved for its information architecture but not for its typography, density, icon roles, surfaces, or control placement. Do not use structural similarity as blanket approval.

A feature plan normally resolves user flow, scope, and behavior. Unless it explicitly includes reviewed visual direction, it does not establish the project's visual language.

Classify rendered artifacts explicitly:

- A golden screen is approved only when the user or project marks it as such.
- A current-state screenshot is an audit target, even when supplied by the user.
- An external reference is evidence only for the decisions extracted from it.

Never assume that a current screenshot expresses the user's preference.

## Minimum project-specific context

Look for guidance covering:

- product character and emotional tone;
- platform posture and native-versus-custom boundary;
- typography roles and minimum readable sizes;
- color and icon roles;
- density, spacing, row, and container conventions;
- surface, border, radius, and elevation philosophy;
- control placement and action hierarchy;
- common screen archetypes and navigation structures;
- reference coverage across flows, component families, data shapes, states, product systems, platforms, and internal continuity;
- motion, feedback, hover, focus, and accessibility behavior;
- approved production references, examples inspected, what to borrow, and what not to transfer;
- explicit anti-patterns;
- golden screens and their intended lessons.

## When context is incomplete

Do not stop ordinary implementation solely because the repository lacks one of these documents.

- Inspect the strongest internal examples.
- Research comparable mature production patterns.
- report a non-blocking design gap;
- implement a reversible provisional direction;
- propose the smallest project artifact needed to close the gap.

Do not create a global rule or rewrite the design system unless the task authorizes that scope.

## Sufficiency check

Before declaring that the project already covers a recurring pattern, locate at least one of:

- explicit documented visual guidance for the decision;
- an approved golden rendering that demonstrates it;
- two or more consistent reviewed production renderings;
- a reusable component whose documented API intentionally owns the treatment.

A bare framework default, one unreviewed screen, or a plan that names the feature is not sufficient evidence.

## Component discovery

Before creating a new control:

- search for semantic equivalents, not only matching names;
- inspect component states and visual previews;
- confirm whether the framework-native control can adopt the project presentation;
- evolve an existing reusable API when the need is general;
- avoid feature-specific workarounds that duplicate an established abstraction.
