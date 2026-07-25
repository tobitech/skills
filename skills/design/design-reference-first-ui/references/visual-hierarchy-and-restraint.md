# Visual Hierarchy and Restraint

Use this protocol for every new or materially redesigned interface. It converts mature production references into explicit hierarchy, grouping, icon, and alignment decisions, then makes the agent test those decisions against its own render.

## Contents

- [1. Study references as systems](#1-study-references-as-systems)
- [2. Rank information before styling](#2-rank-information-before-styling)
- [3. Build a bounded text-emphasis ladder](#3-build-a-bounded-text-emphasis-ladder)
- [4. Control containment and visual density](#4-control-containment-and-visual-density)
- [5. Integrate icons without surface clutter](#5-integrate-icons-without-surface-clutter)
- [6. Prove alignment with a layout ledger](#6-prove-alignment-with-a-layout-ledger)
- [7. Run a design-convergence loop](#7-run-a-design-convergence-loop)
- [8. Treat recurring failures as blockers](#8-treat-recurring-failures-as-blockers)

## 1. Study references as systems

Do not collect references only for mood. Use [production-reference-research.md](production-reference-research.md) to build a compact multi-example coverage set across the relevant product system, flow, screen archetype, component family, data shape, states, platform, and internal project contexts. Assign each reference a concrete question, then extract an implementable pattern.

Inspect these dimensions:

| Dimension | Extract |
|---|---|
| Information architecture | What is shown, combined, delayed, disclosed, or omitted |
| Scan order | First, second, and third visual destinations |
| Text emphasis | Which roles are darkest, muted, smaller, heavier, or intentionally quiet |
| Grouping | What uses proximity, whitespace, dividers, one shared surface, or separate cards |
| Boundaries | Number and purpose of fills, borders, radii, badges, and nested surfaces |
| Icons | Bare glyph, semantic color, tile, avatar, brand mark, status, or action affordance |
| Alignment | Container edges, icon column, copy column, baselines, and trailing-control edge |
| Actions | Primary, secondary, destructive, persistent, and contextual placement |
| States | Hover, focus, selected, disabled, loading, empty, error, and overflow treatment |
| Restraint | What the reference deliberately does not decorate, repeat, or keep visible |

Record a falsifiable recipe, not an adjective. “Clean” is not a recipe. “One unbounded section, bare neutral icons in a fixed column, readable secondary copy, and trailing controls sharing one edge” is.

Use different references for different decisions when appropriate. A platform-native app may supply interaction behavior while a mature web product supplies information grouping. Do not let one screen become blanket approval.

Classify each observation as a durable convention, category pattern, product signature, current trend, or possible source flaw. Production references are reviewed evidence, not unquestionable truth.

If the agent cannot explain what the references collectively establish, where they disagree, what each source omits, how many neutral text levels it uses, why each boundary exists, which edges align, and which treatments should not transfer, it has not studied the evidence deeply enough.

## 2. Rank information before styling

Do not restyle the source view tree one block at a time. First classify every visible item:

1. **Orienting** — tells the user where they are and what the surface is for.
2. **Actionable or decisive** — the main result, value, state, or action.
3. **Required explanatory** — must be read to understand or safely use the interface.
4. **Supporting** — useful context that may be scanned after the primary content.
5. **Optional metadata** — paths, timestamps, provenance, counts, or technical detail that can be ignored.

Then decide what to:

- keep visible;
- combine into one sentence, row, or group;
- move closer to the item it explains;
- convert to label/value anatomy;
- reveal on demand;
- remove because it repeats the same meaning.

Choose one dominant message or task per region. When several elements compete for first attention, change the structure before changing colors.

For redesigns, preserve required behavior and content—not the accidental hierarchy of the old layout.

## 3. Build a bounded text-emphasis ladder

Use semantic emphasis roles rather than isolated foreground colors or opacity values.

### Primary emphasis

Use for the page identity, decisive values, primary row labels, and content that must be read. It should remain clearly legible without relying on heavy weight.

### Secondary emphasis

Use for supporting explanations, section orientation, and content that remains useful to the task. Secondary does not mean faint. It must remain comfortably readable at normal viewing distance and meet applicable contrast requirements.

### Tertiary emphasis

Reserve for genuinely optional metadata such as timestamps, file paths, provenance, or redundant detail. Do not use tertiary color for instructions, errors, current state, or explanatory text needed to make a decision.

### Disabled emphasis

Use only for unavailable interaction or content whose disabled state is intentional. Do not use disabled styling merely to create another hierarchy tier.

Limit one composition to roughly three neutral text-emphasis levels, excluding disabled and semantic status colors. Too many near-grey values create visual fog rather than hierarchy.

Combine color with role-appropriate size, weight, spacing, and placement. Do not:

- make every heading, value, and paragraph equally dark;
- mute an entire card because one state is unavailable;
- bold a sentence to compensate for missing structure;
- render required prose like ignorable metadata;
- introduce a raw opacity because the semantic role is unclear.

Test the hierarchy at reduced scale and in grayscale when possible. The dominant message, required explanation, and optional metadata should remain distinguishable by luminance and structure. If everything becomes one dark block or one pale haze, revise the recipe.

## 4. Control containment and visual density

Visual clutter comes from competing boundaries and emphasis, not only from the amount of content.

Require a semantic reason for every card, fill, border, divider, badge, and rounded rectangle. Valid reasons include:

- selecting or manipulating one bounded object;
- separating a distinct action region;
- expressing a real surface plane or floating layer;
- grouping content that must move, focus, or respond as one unit.

Prefer whitespace, alignment, and one shared grouped surface before separate cards. A card is not the default way to group every paragraph or setting.

Use a containment budget:

- default to one visible boundary per semantic group;
- avoid card-inside-card unless the child is a distinct interactive object or higher plane;
- avoid repeating the same fill and radius on a parent, icon tile, badge, and button;
- challenge sibling cards that could become rows in one group;
- avoid keeping every possible action visible when a menu or progressive disclosure is clearer.

Run a subtraction pass after the first render. Remove or simplify one boundary, fill, icon tile, label, or persistent action at a time. Keep it removed when hierarchy and interaction remain clear.

Compare boundary count with the selected production references. If the candidate uses more cards, pills, tiles, dividers, or emphasized labels, justify each extra one.

## 5. Integrate icons without surface clutter

Default neutral informational icons to a bare glyph in a stable semantic frame. Let alignment, weight, and color integrate the symbol with the card or row.

Add an icon background only when it has a documented role:

- avatar or identity;
- brand mark;
- semantic status that benefits from a badge;
- primary action affordance;
- distinct selectable object;
- required contrast against a variable background.

Do not place a quiet icon on a decorative tile merely because the parent is a card. Avoid identical or near-identical surface fills nested behind the icon.

Ensure the icon remains subordinate to the primary label unless the icon itself is the object or action. Check mixed glyph shapes inside the same frame and align multiline rows by the copy, not by raw symbol bounds.

## 6. Prove alignment with a layout ledger

A generic grid intention is insufficient. Before implementation, name the repeated anchors:

- outer container leading and trailing edges;
- icon or avatar frame;
- primary copy start;
- first baseline or top edge;
- trailing state, action, or control edge;
- optional secondary column and its ownership.

For repeated rows or cards, write a compact ledger such as:

```text
container | icon 24 | gap | flexible copy | gap | trailing control
alignment | top     |     | first baseline |     | trailing/top
```

Use the same declared columns across siblings. Do not place a control at an arbitrary midpoint because one row has shorter copy. Do not let one helper sentence begin under a control while a sibling helper begins under the label unless those are named, recurring variants.

Prefer a real layout primitive—SwiftUI `Grid`, CSS Grid, a shared row component, or equivalent—when repeated columns must align. A chain of spacers and local frames is not a grid contract.

On the integrated render, trace or measure vertical lines through copy starts and trailing edges. Compare repeated anatomy across separate cards and sections as well as inside one container. Check the first, middle, and last item, shortest and longest content, multiline content, absent accessories, and narrow/wide widths. Use same-scale crops, temporary guides, layout geometry, or screenshot coordinates when available; a declared component or grid is not proof that modifier order and intrinsic control sizing preserved it.

## 7. Run a design-convergence loop

Do not stop when the first render is merely acceptable.

For new or materially redesigned UI:

1. Render the complete integrated candidate with realistic content.
2. Review at normal size, reduced scale, and grayscale when available.
3. Run the structural pass: priority, grouping, containment, omission, and action placement.
4. Compare those decisions with the reference recipes.
5. Revise and re-render.
6. Run the visual pass: text emphasis, alignment, proportion, icon integration, contrast, and optical polish.
7. Revise and re-render.
8. Confirm important states, widths, appearance modes, and accessibility.
9. Repeat whenever a reference-backed change would materially improve the result.

Stop when no blocker or major issue remains and the next change would be minor, subjective, or outside scope. Record unresolved recurring decisions as design gaps.

## 8. Treat recurring failures as blockers

Do not call the design complete when any of these remain:

- required reading is styled like metadata or disabled content;
- every text block has nearly equal darkness and visual weight;
- several elements compete for first attention;
- the candidate preserves all source blocks without reconsidering organization;
- a surface or icon tile has no semantic containment role;
- cards, pills, borders, or fills outnumber comparable reference patterns without justification;
- repeated rows do not share a copy start or trailing-control edge;
- controls float in available space instead of belonging to a declared column;
- a material or novel design relies on one isolated source screen despite broader relevant examples being available;
- the agent cannot state what it learned from references per decision;
- the agent cannot state which source treatments it deliberately rejected and why;
- the integrated candidate has not been re-rendered after hierarchy and restraint critique.
