# Production Reference Research

Use mature production interfaces as reviewed evidence when the project has no strong precedent.

## Source priority

1. User-provided screenshots and annotated collections
2. Project reference atlas and approved external examples
3. Live production applications the user can access
4. Targeted Mobbin screen or flow searches
5. Official product pages, documentation, or platform examples
6. Broad image search only when stronger sources are unavailable

Use current browsing or connected tools when a product interface may have changed. Inspect the actual image or live screen; do not infer design from search metadata.

First determine why a screenshot was supplied. A current-state screenshot is audit evidence, not a reference to emulate. Treat it as approved inspiration only when the user or project explicitly says so.

## Search narrowly

Describe one concrete problem:

- a two-line secondary navigation row with count metadata;
- a review screen with editable content and approve/reject actions;
- an agent activity group with collapsed technical evidence;
- a mobile empty state that transitions into a populated list.

Avoid vague searches such as “clean modern dashboard.”

## Prefer reviewed consensus

When practical, inspect two or three comparable mature applications. Identify:

- shared information hierarchy;
- scan order and action placement;
- typography relationships;
- density and grouping;
- icon alignment and color role;
- disclosure and state behavior;
- responsive or resizable behavior;
- accessibility-relevant interaction.

Convergence across products is a stronger default than one distinctive treatment.

## Extract a falsifiable pattern

Do not stop after collecting screenshots. Assign every reference a concrete design question, then record the evidence in a compact pattern study:

| Decision | Reference evidence | Working recipe | Deliberate omission | Project adaptation |
|---|---|---|---|---|
| Text hierarchy | Which content is darkest, muted, small, or grouped | Semantic roles and relationships, not copied values | What the reference does not emphasize | Project typography and contrast roles |
| Containment | Which groups receive a boundary and which rely on whitespace | Boundary count and nesting rule | Cards, fills, dividers, or badges intentionally absent | Project surface planes |
| Icon treatment | Bare glyph, stable frame, tile, tint, or status treatment | When each treatment is earned | Decorative icon surfaces intentionally absent | Project icon roles |
| Alignment | Shared leading, copy, baseline, and trailing anchors | Explicit row or card grid | Arbitrary spacer-driven positions absent | Shared layout primitive |
| Actions | Dominant, secondary, deferred, or disclosed | Placement and prominence relationship | Actions removed from the initial scan path | Platform-appropriate controls |

Extract what the reference **omits** as carefully as what it includes. Mature production design often feels clean because it declines unnecessary containers, accent colors, labels, repeated controls, and visible metadata.

A useful study produces a recipe another agent can test. “Clean,” “modern,” “Notion-like,” and “inspired by Apple” are not recipes.

## Adapt rather than copy

Extract the decision that makes the pattern work. Translate it into:

- the project's content model and visual language;
- the target platform's navigation and interaction conventions;
- existing semantic tokens and reusable components;
- the project's accessibility and localization requirements.

Do not copy brand assets, ornamental styling, proprietary content, or web behavior that weakens native Apple-platform interaction.

## Record influence precisely

State which aspect came from which reference:

> The reference uses neutral taxonomy icons, readable primary labels, quiet metadata, and generous row rhythm. Adapt those relationships to the project's typography and native selection behavior.

Do not justify a decision only by saying that another app uses it.

## Compare the candidate back to the pattern

After rendering, compare the candidate with the extracted recipe—not only with the screenshot's overall mood. Check:

- whether the same information is dominant and subordinate;
- whether the candidate introduced more text-emphasis levels or visible boundaries;
- whether icons gained decorative tiles, tints, or prominence absent from the reference;
- whether repeated content shares equally clear anchors;
- whether controls occupy the intended scan path;
- whether the candidate retained information the reference successfully combined, deferred, or removed.

Record material deltas privately and correct them when they weaken the intended pattern. A reference-informed design is not complete until the implementation has been compared back to the evidence that justified it.

## When research does not resolve the decision

Report a design gap. Explain:

- what was searched;
- why the references were insufficient or contradictory;
- the safest provisional direction;
- what project-level decision would close the gap.
