---
name: design-reference-first-ui
description: Design, implement, and critically review polished product interfaces across iOS, macOS, and web by grounding decisions in the project's visual language, approved internal patterns, and mature production references. Use when starting a fresh project without a design system or design documentation and needing a minimum visual foundation for its first screen; when creating or materially redesigning screens, flows, navigation, layouts, controls, components, or UI states; when modifying an existing design and deciding whether the change belongs in a foundation, shared component, contextual variant, or one-off composition; when implementing UI from a plan without a supplied mockup; when an existing interface feels generic, unfinished, or inconsistent; when Codex should critique its own rendered design in application context before claiming completion; or when a missing design-system pattern should be identified, handled provisionally, and proposed for closure without unnecessarily stopping implementation.
---

# Reference-First UI Design

Use reviewed product evidence before invention. Preserve platform-native behavior while expressing the project's own visual language.

## Core contract

- Treat an approved implementation plan as authorization to continue through design, implementation, rendering, self-review, and iterative polish. Do not add a user-approval pause merely because no mockup exists.
- When a project has no visual language or design system, bootstrap a minimum viable design contract and implement the first screen in the same workflow. Do not require pre-existing `design.md` files or delay the first interface for a speculative comprehensive system.
- Treat a feature plan as product and implementation direction, not blanket approval of visual treatment. Require visual evidence for typography, icon, density, alignment, surface, and control-placement decisions.
- Prefer, in order: an approved project pattern, a comparable mature production pattern, platform conventions for behavior, then a new composition.
- For material or novel UI, build a compact multi-example reference set across relevant flows, screen archetypes, component families, data shapes, states, and whole-product systems. Do not make one similar screenshot carry every design decision.
- Treat existing code as evidence, not automatically as an approved design. Prefer documented patterns and golden screens.
- Require a composition grammar as well as a token inventory. A valid font, color, or spacing value can still produce a weak hierarchy when its relationship, alignment, proportion, or surface plane is wrong.
- Begin visual design from ranked information and task priority rather than styling the source view tree. Require a bounded text-emphasis system, justified containment, deliberate icon treatment, and explicit alignment anchors.
- Use native interaction semantics and accessibility while applying project-specific presentation. Follow: **native behavior, project presentation**.
- Classify requested visual changes by ownership before implementation. Inspect consumers before changing foundations or shared components; prefer named semantic variants over repeated local overrides.
- Report reusable or conflicting design-system gaps while continuing with a reversible provisional choice. Pause only for decisions that materially change product behavior, information architecture, or scope.
- Require a rendered, in-context self-critique before declaring a visual implementation complete. Do not confuse functional correctness, token usage, or an isolated component preview with production readiness.
- Invoke relevant platform implementation skills when available; this skill governs design reasoning and visual verification rather than replacing framework expertise.

## Workflow

### 1. Establish task mode

Determine whether the user requested implementation, design exploration, project bootstrap, or review.

- For implementation, make safe design decisions autonomously and keep working.
- For a fresh-project bootstrap, establish the minimum project foundation and build the requested first screen without adding an approval gate.
- For design exploration, present alternatives only when they represent meaningfully different structures or user journeys.
- For review, remain read-only unless the user also requested changes.

### 2. Load project-specific context

Read repository instructions first. Discover the project's visual language, design-system implementation, UI patterns, component catalog, reference atlas, golden screens, and nearby relevant interfaces.

Read [project-contract.md](references/project-contract.md) when discovering a project or when its design context is incomplete. Do not require exact filenames.

Read [composition-foundations.md](references/composition-foundations.md) when establishing a visual language or when recurring problems involve spacing, alignment, sizing, proportion, surface hierarchy, or typography hierarchy.

Read [visual-hierarchy-and-restraint.md](references/visual-hierarchy-and-restraint.md) for every new or materially redesigned interface. Use it to study references, rank content, control text emphasis, prevent container clutter, decide icon treatment, and prove repeated alignment.

Read the relevant platform guidance:

- Apple platforms: [apple-platforms.md](references/apple-platforms.md)
- Web: [web-platform.md](references/web-platform.md)
- Cross-platform work: read both and keep shared product identity separate from platform adaptation.

### 3. Bootstrap a fresh project when needed

If the project lacks sufficient visual guidance or reusable foundations, read [fresh-project-bootstrap.md](references/fresh-project-bootstrap.md) and run its just-in-time bootstrap before or alongside the first interface.

Create filled, evidence-backed project artifacts rather than empty templates. Establish:

- a discoverable design entry point and concise repository instruction bridge;
- product character, platform posture, and explicit anti-patterns;
- a reference source map that records what each source may and may not influence;
- semantic composition foundations and the smallest reusable implementation needed by the first screen;
- deterministic component and integrated previews;
- an open design-gap register and a candidate golden rendering.

Use [project-visual-language-template.md](references/project-visual-language-template.md) as the content checklist. Adapt to the repository's existing documentation conventions and avoid unnecessary file proliferation.

### 4. Inspect the nearest precedents

Inspect the actual UI or rendered previews when available, not only source code. Select precedents by interaction, information structure, flow stage, component family, and data shape—not superficial visual similarity.

Inspect the project laterally as well as locally. Review the nearest screen, the complete surrounding flow, sibling components, unrelated golden screens that express the product language, and the same data or action pattern elsewhere. The result must solve the local problem without becoming a visual dialect that appears only on one screen.

Evaluate a precedent per decision. A screen may be a valid reference for navigation structure while remaining unapproved for row density, icon tint, typography, card treatment, or toolbar composition. Do not treat one structurally similar screen as blanket visual approval.

Classify every screenshot or rendered screen as one of:

- **approved reference or golden** — explicitly endorsed by the user or project;
- **current-state audit evidence** — demonstrates what exists but not necessarily what should be copied;
- **external inspiration** — supplies reviewed production evidence for selected decisions.

When intent is not explicit, treat a current project screenshot as audit evidence rather than approval. Do not infer the user's taste from the current implementation.

Identify:

- screen archetype and user goal;
- scan order and primary action;
- ranked information and what remains visible, combines, moves, or becomes progressive disclosure;
- typography and text-emphasis relationships, icon integration, density, alignment grid, surface strategy, and control-placement rules;
- what the reference deliberately leaves unbounded, unaccented, or absent;
- reusable components and their states;
- nearby inconsistencies that should not be copied.

Before concluding that no reusable design gap exists, identify explicit documented guidance, an approved golden example, or consistent reviewed renderings for the recurring decisions the feature requires. Framework defaults and isolated implementations are insufficient by themselves.

Inspect all critical recurring dimensions before reporting gaps. Group related gaps into one concise notice when that reduces noise, but do not stop analysis after finding the first obvious problem.

### 5. Research production references when needed

If no strong internal precedent exists, read [production-reference-research.md](references/production-reference-research.md). Search narrowly for the same design problem in mature production applications. Inspect actual screenshots or live UI and synthesize the reviewed pattern instead of copying an app wholesale.

For material or novel UI, inspect a compact evidence set across the applicable lenses: whole-product system, end-to-end flow, screen archetype or category, component family, data shape, states and scale, platform convention, and project continuity. Normally use several examples from the user's preferred sources, including multiple areas of the same product, and compare two or more products when available.

Extract shared decisions and omissions, explain platform adaptation, and record which reference influenced each hierarchy, grouping, surface, icon, alignment, data-presentation, or interaction choice. Classify observations as durable conventions, category patterns, product signatures, current trends, or source flaws. Adopt selectively; production quality does not make every source decision transferable.

### 6. Perform a private design preflight

Before coding, resolve:

- intended outcome and dominant scan path;
- ranked content map: orienting, actionable, required explanatory, supporting, and optional metadata;
- screen archetype and content hierarchy;
- primary, secondary, and destructive actions;
- component reuse versus new component needs;
- text-emphasis ladder and recurring label/value or title/supporting-copy recipes;
- spacing relationships, an alignment ledger for repeated anatomy, content-width and sizing rules, and surface planes;
- containment budget, subtraction opportunities, and justification for every icon tile or nested surface;
- change ownership: foundation, shared component, contextual semantic variant, or local composition;
- important normal, empty, loading, error, disabled, selected, and overflow states;
- responsive or resizable behavior;
- accessibility and platform-native interaction requirements;
- reference coverage across flow, archetype, components, data, states, product system, platform, and internal continuity;
- patterns adopted, patterns deliberately rejected, and open design-system gaps.

Keep this preflight internal unless sharing it helps the user evaluate a meaningful decision.

### 7. Report design gaps without unnecessary blocking

Read [design-gap-protocol.md](references/design-gap-protocol.md) whenever guidance is missing, contradictory, or likely to recur.

Send a concise **Design gap — non-blocking** commentary update, cite the evidence inspected, state the provisional reference-backed direction, and continue implementation.

Do not silently promote a provisional local decision into the global visual language. Propose how to close the gap with a documented rule, semantic token, reusable component, pattern, or golden example.

When the scope of a requested change is unclear, use the ownership procedure in the protocol. Ask only when local and shared interpretations are both plausible and the shared blast radius is meaningful.

### 8. Implement preview-first

Create deterministic preview or fixture data before wiring live dependencies when the framework supports it. Reuse existing components and design-system roles. When a new reusable primitive is required, keep its API product-agnostic and document its intended visual role.

Avoid locally valid defaults that conflict with the project character. Explicitly control presentation where framework defaults introduce the wrong typography, tint, density, alignment, surface, or control placement.

Prepare both:

- an isolated render that exposes component states and edge cases;
- an integrated render inside the real screen, window, background, navigation, and neighboring content.

### 9. Render, self-critique, compare, and polish

Read [self-critique-protocol.md](references/self-critique-protocol.md) and [visual-quality-gate.md](references/visual-quality-gate.md). Render the actual interface using the best available platform tooling.

Perform a private failure-seeking critique of the first render. Judge the component in isolation and within its surrounding application environment. Identify what looks accidental, generic, visually unresolved, poorly separated, misaligned, illegible, inconsistent, or unshippable. Fix every production-readiness blocker and major issue, then re-render and perform a confirmation pass.

Compare the result with the selected internal and production reference set. Compare relationships—not merely token names or individual measurements—including flow continuity, data presentation, scan order, text-emphasis contrast, proximity, baseline and edge alignment, proportions, boundary count, surface nesting, icon integration, state behavior, and environmental contrast.

Review the candidate at reduced scale and, when tooling permits, in grayscale. Run a mandatory sibling-geometry audit before relying on general visual judgment. For every repeated component family visible in the integrated render—including instances separated into different cards or sections—record the expected container, icon, copy, baseline, and trailing-control anchors; compare at least the first, middle, and last or all instances when the set is small; and verify the actual edges with zoomed crops, guides, geometry inspection, or screenshot coordinates. A declared grid is not evidence that the render follows it. Treat any unexplained delta larger than rendering antialiasing as a blocker, fix the shared geometry owner, and repeat the same comparison on the confirmation render.

Trace the remaining declared alignment anchors and run a subtraction pass that challenges every border, fill, icon tile, badge, label, and persistent action.

Run a project-fit pass after the external comparison. Verify that borrowed patterns were translated through the project's approved foundations and components, that the screen fits neighboring and unrelated product areas, and that no product-specific signature, fashionable treatment, or known source flaw was imported without justification.

For a new or materially redesigned interface, run a convergence loop with at least:

1. a structural pass for information priority, grouping, containment, and subtraction;
2. a visual pass for text emphasis, alignment, proportion, icon integration, and optical polish;
3. a confirmation render in the integrated context.

Continue iterating whenever a reference-backed change would materially improve clarity, restraint, cohesion, or platform fit. Stop when no blocker or major issue remains and the next change would be minor, subjective, or outside scope. A small, tightly scoped visual edit may use one critique-and-confirmation cycle.

For visually consequential, novel, or high-exposure work, use an independent read-only visual reviewer when one is available after the implementing agent completes its own deterministic and failure-seeking checks. A second model may expose taste, hierarchy, or pattern-transfer issues, but it is not a substitute for measurable alignment, sizing, overflow, contrast, or state verification.

Do not claim visual verification from a successful build alone. If rendering is blocked, report the exact limitation and complete all other safe checks.

### 10. Hand off the result

Lead with the implemented outcome. Briefly report:

- reference lenses and project patterns that materially influenced the design;
- borrowed patterns and source treatments deliberately rejected;
- project design artifacts and reusable foundations created or changed;
- preview or screenshot states inspected;
- material issues found and corrected during self-critique;
- unresolved design gaps and provisional choices;
- proposed system-level closures;
- build, test, and accessibility verification performed.

Do not bury an unresolved design gap inside generic implementation notes.

## Project setup

When the user asks to establish a project visual language or the project has none, run [fresh-project-bootstrap.md](references/fresh-project-bootstrap.md). Keep project-specific taste, components, decisions, and screenshots in the repository rather than hardcoding them into this reusable skill.
