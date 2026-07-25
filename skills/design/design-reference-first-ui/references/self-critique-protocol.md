# Self-Critique Protocol

Use this protocol to judge whether a rendered interface is genuinely production-ready rather than merely implemented.

## Contents

- [Critique stance](#critique-stance)
- [Required visual contexts](#required-visual-contexts)
- [Critique and convergence sequence](#critique-and-convergence-sequence)
- [Hierarchy, restraint, and alignment review](#hierarchy-restraint-and-alignment-review)
- [Attention-order audit](#attention-order-audit)
- [Sibling-geometry audit](#sibling-geometry-audit)
- [Environmental fit](#environmental-fit)
- [Composition relationship review](#composition-relationship-review)
- [Surface, boundary, and elevation review](#surface-boundary-and-elevation-review)
- [Production-readiness blockers](#production-readiness-blockers)
- [Fresh-eyes review](#fresh-eyes-review)

## Critique stance

Review adversarially. Do not ask only “Does this look good?” Ask:

- What looks accidental, generic, unfinished, or inherited from a framework default?
- What would a rigorous design review reject immediately?
- What becomes unclear when viewed quickly, from a distance, or at reduced scale?
- Which details fail to express the product's visual language?
- Does every element look intentionally placed, sized, aligned, and styled?
- What would the user likely have to point out if this were presented now?

Do not defend the first implementation. Treat the first render as evidence to improve.

## Required visual contexts

Inspect both:

1. **Isolated component context** — normal and important interaction or content states.
2. **Integrated application context** — actual parent screen, surrounding background, neighboring elements, navigation, window or viewport, and realistic content.

An isolated component can look polished while failing inside the application. Do not declare completion from a cropped component preview alone.

Inspect light and dark appearance, relevant widths or size classes, and the most demanding content/state combinations when they materially affect the result.

## Critique and convergence sequence

1. Render the first complete candidate.
2. Record a private critique of three to seven concrete observations.
3. Compare the intended first three attention destinations with the observed first three in the integrated render.
4. Classify each observation:
   - **blocker** — visibly unfinished, confusing, inaccessible, or inconsistent enough that it should not ship;
   - **major** — materially weakens hierarchy, cohesion, legibility, or interaction quality;
   - **minor** — optical polish that improves refinement without changing comprehension.
5. Run a **structural pass**: simplify the content model, grouping, disclosure, containment, and action placement; remove redundant surfaces and information.
6. Run a **visual pass**: correct text emphasis, spacing, density, icon treatment, alignment anchors, geometry, and environmental separation.
7. Re-render the integrated context as a **confirmation render**.
8. Compare it back to the project language and the extracted production-reference patterns.
9. Repeat while a reference-backed material improvement remains visible, even when the implementation technically works.

Stop only when:

- no blocker or major issue remains;
- the scan order, hierarchy, restraint, and alignment survive integrated review;
- the latest corrections work together and introduced no new defect;
- the next change would be minor, subjective, or outside the requested scope.

Do not expose the private critique unless it helps explain a design gap or unresolved limitation. Report material corrections concisely in the final handoff.

## Hierarchy, restraint, and alignment review

Judge these relationships explicitly rather than relying on a general impression:

- Write the intended scan order, then verify it at reduced scale.
- View the render in grayscale or mentally remove accent color. Primary, secondary, and tertiary importance must remain understandable.
- Confirm that required explanatory text is secondary and comfortably readable, not styled like optional metadata or disabled content.
- Count visible text-emphasis levels. More than three neutral levels, excluding disabled and semantic status, needs a clear reason.
- Count cards, fills, borders, dividers, badges, icon tiles, and rounded rectangles. Every visible boundary must explain grouping, interaction, state, or elevation.
- Remove one decorative treatment at a time and keep it removed when hierarchy remains clear.
- Treat a bare glyph in a stable frame as the default informational icon. Require a semantic reason for a tile, tint, or nested icon surface.
- Trace the leading container edge, icon frame, copy start, first baseline or top anchor, and trailing control edge across repeated rows or cards.
- Verify that controls align to the declared grid rather than to an arbitrary visual midpoint produced by spacer chains.

If the interface looks busy, do not begin by adjusting random spacing. First reduce competing emphasis, visible boundaries, duplicated labels, and unnecessary controls; then re-evaluate spacing.

## Attention-order audit

Use the first-read test and attention ledger in [visual-hierarchy-and-restraint.md](visual-hierarchy-and-restraint.md) for every important region.

1. Classify the visible blocks as peer sections, nested parts of one entity, or a parent entity with a decisive outcome and supporting evidence.
2. Write the intended first three attention destinations before inspecting the render.
3. At normal size, reduced scale, and in grayscale, record the observed first three without using source-code type names as evidence.
4. Compare parent and child prominence using size, weight, contrast, whitespace, position, surface emphasis, and wording—not size alone.
5. Inspect embedded Markdown, rich text, HTML, and native semantic headings for context-inappropriate document-level prominence.
6. Treat a mismatch, tie for first attention, or child-over-parent inversion as a blocker.
7. Fix the closest reusable owner: content model, semantic type recipe, contextual renderer style, or shared component.
8. Re-render and repeat the ledger.

Do not approve a single semantic entity when a nested generic label is louder than both its identity and useful value. Do not approve required explanation that becomes tertiary merely to make the hierarchy appear stronger.

## Sibling-geometry audit

Do not approve repeated anatomy by impression. Build a compact private matrix for every repeated component family visible in the integrated render, including instances that live in separate cards or sections:

| Family | Instances compared | Container edges | Icon frame | Copy start | Baseline or top | Trailing control | Result |
|---|---|---|---|---|---|---|---|
| Example: Settings rows | Model, Startup, Keyboard | shared | shared | shared | shared | shared | pass/fix |

Compare all instances when the set is small; otherwise compare at least the first, middle, last, shortest-content, longest-content, and state variants. Inspect the actual render with zoomed same-scale crops, temporary guides, layout geometry, or screenshot coordinates. Check:

- outer leading and trailing insets across separate containers;
- repeated control right edges and control-column starts;
- icon-frame edges and optical symbol placement;
- primary and supporting copy starts;
- first baselines or top anchors;
- control width, height, and internal label padding for the same control family;
- absent accessories, multiline copy, localization, and narrow/wide states.

A component name, shared token, or intended grid does not prove that the rendered instances align. Feature-local frames, padding, intrinsic control sizes, nested containers, and modifier order can still create visible drift.

Treat any unexplained delta larger than raster antialiasing as a production-readiness blocker. Fix the closest shared geometry owner when the relationship recurs. Re-run the same matrix on the confirmation render so the correction does not introduce a new mismatch.

## Environmental fit

Judge the component as part of a composition:

- Does it belong to the same product as the surrounding UI?
- Does it compete with or disappear behind neighboring elements?
- Are its outer spacing, alignment, width, and visual weight appropriate for its location?
- Does its hierarchy connect correctly to the parent screen's scan order?
- Does it preserve the intended background, scroll ownership, clipping, safe areas, and z-order?
- Do repeated siblings share optical alignment and treatment?
- Does the component remain legible against every background it can actually appear over?

Review the full screen or window, not only a close crop.

## Composition relationship review

Do not stop at verifying that every element uses an approved token. Ask:

- Can each gap be explained by semantic proximity, and are separate groups farther apart than paired content?
- Do sibling icons, copy blocks, first baselines, and trailing controls share stable anchors?
- Are dimensions content-derived or constrained by documented minimum, ideal, and maximum roles instead of arbitrary fixed geometry?
- Does every nested fill represent a higher semantic plane, or is it merely another grey or rounded rectangle?
- Does each type style match its role in the composition recipe, especially primary labels and explanatory copy?

A token-compliant screen with unresolved relationships is not production-ready.

## Surface, boundary, and elevation review

Every layered surface must communicate its plane deliberately.

- For a floating panel, popover, inspector, menu, or overlay, verify that users can distinguish its edges from the content behind it.
- Use the project-approved combination of surface contrast, material, border, shadow, backdrop, or elevation. Not every surface needs all of them, but a floating surface on a similar background needs a credible boundary.
- Check every edge and corner in light and dark appearance.
- Verify that shadows are not clipped and that border, radius, fill, and shadow geometry agree.
- Confirm that elevation strength matches the surface's role and does not overpower nearby content.
- Ensure the trigger-to-surface relationship, anchor, and placement feel intentional.

A floating surface with no perceivable separation from its environment is a production-readiness blocker.

## Production-readiness blockers

Treat these as failures until resolved:

- a floating or layered surface has no credible boundary from its background;
- the component was reviewed only in isolation;
- hierarchy, text contrast, or explanatory copy is not comfortably legible;
- the observed first-read order differs from the declared attention order;
- a nested heading, generic label, or supporting block unintentionally outranks its parent entity or decisive value;
- embedded content inherits document-level heading prominence that does not fit its component context;
- a framework default visibly conflicts with the product language;
- sibling alignment, padding, typography, icon treatment, or surface treatment is inconsistent;
- repeated geometry was approved without comparing actual sibling anchors across the integrated render;
- required prose is rendered with tertiary, disabled, or otherwise faint emphasis;
- nearly every text block uses the same dark emphasis, flattening the information hierarchy;
- cards, borders, icon tiles, badges, or nested surfaces lack a semantic containment reason;
- repeated rows or cards do not share explicit copy and trailing-control anchors;
- production references were collected without extracting their hierarchy, restraint, alignment, and omission patterns;
- a material or novel design was justified by one isolated screenshot without checking relevant flows, component families, data shapes, states, or whole-product patterns;
- a borrowed product signature, temporary trend, accessibility weakness, or source inconsistency was treated as a durable convention;
- the candidate matches an external reference but feels inconsistent with the project's surrounding screens, components, or full flow;
- intended interactive states are absent, ambiguous, or visually broken;
- shadows, outlines, focus rings, or content are clipped;
- empty, loading, error, disabled, overflow, or long-content states collapse the layout;
- the component looks decorative or heavy relative to its importance;
- the candidate was not re-rendered after material critique corrections;
- the result relies on rationale to excuse a defect visible in the render.

## Fresh-eyes review

For visually consequential, novel, or high-exposure surfaces, use an independent read-only reviewer when available after the implementing agent has completed its own deterministic geometry, state, and accessibility checks. Give the reviewer the rendered artifact, relevant project references, and user goal—not the intended answer or the author's diagnosis.

Use independent review as additional evidence for hierarchy, restraint, taste, pattern transfer, and fresh-eyes defects. A second model is not proof of alignment, sizing, overflow, contrast, or state correctness and does not replace the implementing agent's own critique.
