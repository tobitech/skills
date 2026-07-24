# Self-Critique Protocol

Use this protocol to judge whether a rendered interface is genuinely production-ready rather than merely implemented.

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

## Critique sequence

1. Render the first complete candidate.
2. Record a private critique of three to seven concrete observations.
3. Classify each observation:
   - **blocker** — visibly unfinished, confusing, inaccessible, or inconsistent enough that it should not ship;
   - **major** — materially weakens hierarchy, cohesion, legibility, or interaction quality;
   - **minor** — optical polish that improves refinement without changing comprehension.
4. Fix every blocker and major issue within scope.
5. Re-render the integrated context.
6. Confirm that the fixes work together and did not create new defects.
7. Repeat when a blocker or major issue remains.

Do not expose the private critique unless it helps explain a design gap or unresolved limitation. Report material corrections concisely in the final handoff.

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
- a framework default visibly conflicts with the product language;
- sibling alignment, padding, typography, icon treatment, or surface treatment is inconsistent;
- intended interactive states are absent, ambiguous, or visually broken;
- shadows, outlines, focus rings, or content are clipped;
- empty, loading, error, disabled, overflow, or long-content states collapse the layout;
- the component looks decorative or heavy relative to its importance;
- the result relies on rationale to excuse a defect visible in the render.

## Fresh-eyes review

For visually consequential, novel, or high-exposure surfaces, use an independent read-only reviewer when available after the first render. Give the reviewer the rendered artifact, relevant project references, and user goal—not the intended answer or the author's diagnosis.

Use independent review as additional evidence, not as a replacement for the implementing agent's own critique.
