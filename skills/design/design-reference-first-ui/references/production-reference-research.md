# Production Reference Research

Use mature production interfaces as reviewed evidence when the project has no strong precedent.

## Contents

- [Source priority](#source-priority)
- [Search narrowly](#search-narrowly)
- [Build a reference coverage set](#build-a-reference-coverage-set)
- [Inspect flows, systems, and data](#inspect-flows-systems-and-data)
- [Know when the evidence is sufficient](#know-when-the-evidence-is-sufficient)
- [Prefer reviewed consensus](#prefer-reviewed-consensus)
- [Extract a falsifiable pattern](#extract-a-falsifiable-pattern)
- [Separate convention, signature, trend, and flaw](#separate-convention-signature-trend-and-flaw)
- [Adapt rather than copy](#adapt-rather-than-copy)
- [Record influence precisely](#record-influence-precisely)
- [Compare the candidate back to the pattern](#compare-the-candidate-back-to-the-pattern)
- [When research does not resolve the decision](#when-research-does-not-resolve-the-decision)

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

## Build a reference coverage set

Do not treat one visually similar screen as sufficient evidence for a material or novel interface. Build a compact set that answers the design from several lenses:

| Lens | Question |
|---|---|
| Whole-product system | How does the source handle hierarchy, density, navigation, surfaces, actions, and states across unrelated areas? |
| End-to-end flow | What happens before, during, and after the target task? What remains persistent or becomes progressive disclosure? |
| Screen archetype or category | How do mature products structure this kind of settings, review, list-detail, dashboard, editor, or activity surface? |
| Component family | How do rows, cards, fields, menus, toolbars, inspectors, and empty states behave across variants? |
| Data shape | How is this exact kind of narrative, metadata, status, metric, record, history, comparison, or editable value presented? |
| State and scale | What changes with loading, empty, error, disabled, selected, overflow, long content, resizing, or responsive layout? |
| Platform convention | Which interaction and accessibility behaviors belong to iOS, macOS, or web rather than to the source brand? |
| Project continuity | Which internal screens, components, and golden examples must the result still look related to? |

For substantial work, normally inspect four to eight relevant examples across at least four lenses, using two or more products when available, plus the nearest internal contexts. These are coverage defaults, not a quota: use fewer for a tightly scoped component with strong precedent, and more when the information architecture is novel or references disagree.

Use multiple examples from the same inspiration product. A product's settings, search, editor, empty state, and detail screen often reveal its real system more reliably than one isolated screenshot.

## Inspect flows, systems, and data

For a flow, inspect:

- entry point and initial promise;
- task stages and decision points;
- what remains persistent versus contextual;
- loading, empty, error, success, and recovery;
- completion, return path, and downstream consequences.

For a component family, inspect:

- stable anatomy and alignment;
- density and content-dependent sizing;
- normal, hover, focus, selected, disabled, editing, and overflow variants;
- which parts are shared versus contextual;
- how the component behaves inside different parent surfaces.

For the data itself, identify:

- type, volume, variability, and scan frequency;
- whether users compare, edit, verify, act, or merely read;
- importance, confidence, status, provenance, and recency;
- which fields are required, supporting, optional, or better disclosed later.

Do not borrow a visual treatment designed for a different data task. A compact metric, narrative report, editable setting, and audit history may contain similar text but need different hierarchy and interaction.

## Know when the evidence is sufficient

Continue sampling while another example could still answer an unresolved question or expose a conflicting pattern. Stop when:

- the important lenses have credible evidence;
- additional examples repeat the same relationships;
- disagreements are understood as platform, category, product-signature, or state differences;
- each material design decision has an internal precedent, production pattern, platform convention, or explicit provisional rationale.

More references are useful only when they improve coverage or challenge a conclusion. Do not browse indefinitely or collect decorative mood boards with no decision attached.

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

## Separate convention, signature, trend, and flaw

Classify observations before adopting them:

- **durable convention** — repeatedly solves the same usability or comprehension problem across products;
- **category pattern** — fits the task and data common to this product category;
- **product signature** — distinctive expression that may be useful only after translation into the project's language;
- **current trend** — popular treatment whose utility, accessibility, or longevity still needs evidence;
- **source flaw or compromise** — inconsistency, accessibility weakness, awkward platform transfer, legacy debt, growth experiment, or design optimized for constraints this project does not share.

Production status is evidence of review, not proof that every decision is good. Critique the reference with the same rigor as the candidate. For every borrowed pattern, ask:

- What problem does it solve?
- What cost or complexity does it introduce?
- Does it fit this data, task, platform, and project character?
- Does it conflict with stronger internal or platform guidance?
- What aspect should be rejected even if another aspect is adopted?

Prefer cross-source convergence over a distinctive treatment. When sources disagree, determine whether the difference comes from the flow stage, data type, platform, audience, product strategy, or an actual design flaw.

## Adapt rather than copy

Extract the decision that makes the pattern work. Translate it into:

- the project's content model and visual language;
- the target platform's navigation and interaction conventions;
- existing semantic tokens and reusable components;
- the project's accessibility and localization requirements.

Do not copy brand assets, ornamental styling, proprietary content, or web behavior that weakens native Apple-platform interaction.

Preserve the project's established identity. External references may improve structure, information handling, component behavior, or visual relationships; they do not override approved project typography, surface hierarchy, density, icon roles, navigation, or reusable components without a deliberate system-level decision.

## Record influence precisely

State which aspect came from which reference:

> The reference uses neutral taxonomy icons, readable primary labels, quiet metadata, and generous row rhythm. Adapt those relationships to the project's typography and native selection behavior.

Do not justify a decision only by saying that another app uses it.

Record rejected influence too:

> Adopt the source's progressive disclosure and trailing action alignment. Reject its faint instructional text and decorative icon tiles because they weaken this project's legibility and surface restraint.

## Compare the candidate back to the pattern

After rendering, compare the candidate with the extracted recipe—not only with the screenshot's overall mood. Check:

- whether the same information is dominant and subordinate;
- whether the candidate introduced more text-emphasis levels or visible boundaries;
- whether icons gained decorative tiles, tints, or prominence absent from the reference;
- whether repeated content shares equally clear anchors;
- whether controls occupy the intended scan path;
- whether the candidate retained information the reference successfully combined, deferred, or removed;
- whether the candidate still belongs to the project's surrounding screens and complete flow;
- whether a borrowed product signature, trend, or source flaw slipped through as if it were a durable pattern.

Record material deltas privately and correct them when they weaken the intended pattern. A reference-informed design is not complete until the implementation has been compared back to the evidence that justified it.

## When research does not resolve the decision

Report a design gap. Explain:

- what was searched;
- why the references were insufficient or contradictory;
- the safest provisional direction;
- what project-level decision would close the gap.
