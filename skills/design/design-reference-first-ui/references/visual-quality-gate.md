# Visual Quality Gate

Complete visual verification before calling a UI implementation finished.

## Contents

- [Render evidence](#render-evidence)
- [Compare](#compare)
- [Review checklist](#review-checklist)
- [Polish and convergence](#polish-and-convergence)

## Render evidence

Use the strongest available mechanism:

- SwiftUI previews, simulator/device screenshots, or macOS window captures;
- browser screenshots at explicit viewport sizes;
- component stories, snapshot tests, or project-specific visual harnesses.

Capture the component in isolation and inside its actual parent screen. Include enough surrounding UI and background to judge hierarchy, boundary, elevation, alignment, and product continuity.

Render the primary state plus the states most likely to expose layout weakness. Consider:

- light and dark appearance;
- narrow and wide widths or relevant size classes;
- short and long content;
- empty, loading, error, disabled, selected, and overflow states;
- larger text or zoom;
- hover, focus, pressed, expanded, and editing states when material.

## Compare

View the candidate beside:

- the nearest approved project screen and surrounding flow;
- one or more unrelated approved screens that express the broader product language;
- the project pattern or component guidance;
- the production reference set that informed the flow, archetype, component, data, and state decisions.

Compare relationships rather than pixel-copying unrelated products.

Use the reference set's extracted pattern studies. Compare flow continuity, data presentation, intended scan order, semantic text-emphasis levels, boundary count, icon treatment, alignment anchors, action placement, state behavior, and deliberate omissions. Correct unjustified deltas rather than accepting a merely similar mood.

Verify both directions: the candidate should benefit from mature external patterns while still belonging to the project. Reject borrowed signatures, trends, and source flaws that conflict with the project's character, components, platform behavior, accessibility, or surrounding screens.

## Review checklist

### Hierarchy and task

- Is the screen purpose clear at a glance?
- Does the intended scan order work at reduced scale?
- Is one action visually dominant where appropriate?
- Is secondary information actually subordinate?

### Project continuity

- Does the result look like the same product as adjacent screens?
- Are typography, icon, density, surface, and control-placement roles consistent?
- Did a framework default introduce an unintended tint, font, spacing, or component style?
- Does the component still feel coherent when viewed in the full screen rather than a close crop?

### Typography and legibility

- Do text styles match semantic roles?
- Are primary, secondary, tertiary, disabled, and semantic-status emphasis roles used intentionally?
- Is explanatory prose comfortably readable?
- Is any required information styled like optional metadata or disabled content?
- Are caption and micro styles limited to genuinely ignorable metadata?
- Does hierarchy remain clear at reduced scale and without accent color?
- Do long and localized strings survive?

### Layout and density

- Does proximity match semantic relationship?
- Are repeated rows and sibling cards aligned consistently?
- Can their container, icon, copy, baseline, and trailing-control anchors be named and traced?
- Is vertical rhythm neither cramped nor wasteful?
- Are surfaces used for meaningful containment rather than decoration?
- Does each repeated anatomy use one explicit grid or shared layout contract rather than unrelated spacer chains?
- Do outer spacing, width, z-order, and visual weight fit the surrounding composition?

### Surface and elevation

- Can every visible card, fill, border, divider, badge, icon tile, and rounded rectangle justify a semantic boundary?
- Were redundant boundaries and decorative icon surfaces removed during a subtraction pass?
- Does an informational icon use a bare glyph in a stable frame unless its role earns a tile, tint, or independent surface?
- Is every floating or layered surface clearly distinguishable from the background it can appear over?
- Does the project-approved surface, material, border, shadow, or backdrop treatment communicate the correct plane?
- Are borders, radii, fills, and shadows geometrically consistent and unclipped?
- Is elevation strong enough to explain layering without becoming theatrical?

### Interaction and platform

- Are controls placed where users expect them?
- Are persistent settings distinguished from transient commands?
- Do hover interactions have keyboard-focus equivalents?
- Are touch targets, focus rings, safe areas, resizing, menus, and navigation platform-appropriate?

### States and accessibility

- Are important states represented without layout collapse?
- Is meaning available without color alone?
- Are contrast, screen-reader labels, keyboard order, motion preferences, and text scaling addressed?

## Polish and convergence

Use [self-critique-protocol.md](self-critique-protocol.md). Treat the first complete render as a candidate, not the likely endpoint:

1. Run a structural and subtraction pass that fixes content organization, grouping, disclosure, action placement, and unnecessary containment.
2. Run a visual pass that fixes hierarchy, text emphasis, spacing, alignment, icon integration, surface treatment, environmental fit, and states.
3. Re-render the integrated context and compare it with the project language and extracted reference patterns.
4. Repeat when a material reference-backed improvement remains.

Do not manufacture endless churn. Stop when no blocker or major issue remains and the next change would be minor, subjective, or outside scope.

A successful build is not visual verification. If rendering is unavailable, state the exact limitation and do not imply that the interface was visually inspected.
