# Visual Quality Gate

Complete visual verification before calling a UI implementation finished.

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

- the nearest approved project screen;
- the project pattern or component guidance;
- the production references that informed the design.

Compare relationships rather than pixel-copying unrelated products.

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
- Is explanatory prose comfortably readable?
- Are caption and micro styles limited to genuinely ignorable metadata?
- Do long and localized strings survive?

### Layout and density

- Does proximity match semantic relationship?
- Are repeated rows and sibling cards aligned consistently?
- Is vertical rhythm neither cramped nor wasteful?
- Are surfaces used for meaningful containment rather than decoration?
- Do outer spacing, width, z-order, and visual weight fit the surrounding composition?

### Surface and elevation

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

## Polish pass

Use [self-critique-protocol.md](self-critique-protocol.md). After the first visual review, make at least one autonomous pass that fixes every blocker and the highest-impact hierarchy, spacing, typography, alignment, surface, environmental-fit, and state issues. Re-render the integrated context and confirm the fixes.

A successful build is not visual verification. If rendering is unavailable, state the exact limitation and do not imply that the interface was visually inspected.
