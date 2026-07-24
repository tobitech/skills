# Composition Foundations

Use this guide when a project has tokens but still produces inconsistent spacing, alignment, proportions, surface layering, or typography. The goal is a small visual grammar that tells agents how valid values relate.

## Tokens are necessary but insufficient

A token inventory constrains values. It does not decide:

- which gap expresses paired content versus separate sections;
- which edges and baselines must align across siblings;
- how wide a readable content region should become;
- which surface may sit on which background;
- which type role belongs to a page header, catalog row, setting, or metadata line.

Encode these decisions as semantic relationships, named metrics, reusable anatomy, and reviewed renders. Do not expect an agent to infer them repeatedly from raw constants.

## Establish a spacing relationship ladder

Choose a compact base rhythm appropriate to the platform, commonly 4 or 8 points, then map available tokens to semantic degrees of relatedness:

1. paired text inside one copy block;
2. icon to copy or compact control gap;
3. related groups in one container;
4. container padding;
5. separate sections;
6. major page or region inset.

The exact values are project-specific. The invariant is that looser semantic relationships receive visibly more space than tighter ones.

Allow optical exceptions only when they are named and owned by a component or token. A 2-point symbol correction can be legitimate; an unexplained local 13-point gap is design-system debt.

## Define alignment anchors

For every repeated row or card anatomy, name the stable anchors:

- container edge;
- leading icon or avatar column;
- primary copy column;
- first text baseline;
- trailing metadata, state, action, or control column.

Decide how single-line and multiline content align. Multiline copy commonly needs top-aligned leading imagery, while single-line controls may use optical centering. Siblings must not alternate arbitrarily between these treatments.

Use a semantic frame for icons instead of aligning raw glyph bounds. Validate first and last rows, multiline content, missing accessories, and mixed symbol shapes.

## Encode sizing and proportion rules

Prefer:

- content-derived row heights with semantic vertical padding;
- stable icon, avatar, and control frames;
- minimum, ideal, and maximum column widths;
- readable maximum widths for prose and settings;
- native resizing behavior and accessibility before fixed geometry.

Grid systems can create rhythm, and modular or golden-ratio studies can inspire large-scale proportions. They are evaluation aids, not universal constraints. Do not force content, native controls, or adaptive layouts into a ratio that weakens scanning or accessibility.

## Define a surface plane ladder

Name the project’s visual planes, for example:

0. base canvas or workspace;
1. grouped or quiet subsection;
2. bounded content object or action region;
3. floating, overlay, menu, or popover.

For every plane, define:

- semantic purpose;
- fill or material role;
- border expectation;
- corner treatment;
- elevation expectation;
- legal parents and nesting limits;
- light and dark appearance behavior.

Use whitespace and dividers before adding another plane. Do not nest identical surface tokens, add a grey solely because an element sits on another grey, or stack rounded rectangles without a distinct containment reason.

A floating surface must remain distinguishable over every background it can cover. Its fill, border, radius, shadow, backdrop, and host clipping must describe one geometry.

## Define typography recipes

A type scale lists available roles. Recipes specify how those roles combine in recurring compositions, such as:

- page title plus supporting sentence;
- catalog row title plus metadata;
- settings row label plus explanation and control;
- card title, supporting copy, and ignorable metadata;
- dense status or timestamp line.

State the type role, weight, contrast role, and maximum number of levels for each recipe. Primary labels should not become captions simply because a column is narrow. Explanatory copy should not use a metadata style when comprehension depends on it.

## Turn rules into implementation

Choose the narrowest durable system home:

- foundation token for an app-wide semantic value;
- named metric for recurring geometry;
- shared component for recurring anatomy;
- contextual variant for a legitimate repeated exception;
- local composition for unique content arrangement;
- golden render for a relationship that is easier to show than describe.

Add source-policy or rendering tests for high-cost regressions, but do not treat tests as visual review. The render remains the evidence for whether the relationships work together.

## Failure-seeking composition critique

On the first integrated render, ask:

- Which gap cannot be explained by the relationship ladder?
- Which sibling edge, baseline, icon, or accessory fails to share an anchor?
- Which dimension feels arbitrarily fixed, cramped, or stretched?
- Which surface has no distinct semantic plane, nests unnecessarily, or disappears into its environment?
- Which text role is technically valid but semantically too small, heavy, faint, or prominent?
- Does the component fit the background, neighboring controls, viewport, and platform chrome around it?
- What would a rigorous design review reject before discussing subjective taste?

Fix blockers and major issues, then re-render the integrated context. If a recurring relationship has no rule, report a non-blocking design gap and propose the token, metric, component, recipe, or golden example that should close it.
