# Fresh-Project Design Bootstrap

Use this protocol when a project has no trustworthy visual language, reference map, design-system implementation, or reviewed screen precedent.

## Contents

- [Goal](#goal)
- [Operating rules](#operating-rules)
- [1. Understand the product and platform](#1-understand-the-product-and-platform)
- [2. Audit before scaffolding](#2-audit-before-scaffolding)
- [3. Build a starter reference source map](#3-build-a-starter-reference-source-map)
- [4. Establish the minimum visual contract](#4-establish-the-minimum-visual-contract)
- [5. Create a discoverable project contract](#5-create-a-discoverable-project-contract)
- [6. Implement the minimum reusable foundation](#6-implement-the-minimum-reusable-foundation)
- [7. Use the first screen to close the loop](#7-use-the-first-screen-to-close-the-loop)
- [8. Readiness check](#8-readiness-check)
- [Commentary and handoff](#commentary-and-handoff)

## Goal

Leave the project able to produce a coherent first interface immediately and make the next interface easier. Bootstrap a minimum viable design contract, not a speculative comprehensive component library.

The default is **just-in-time bootstrap**: establish the reusable decisions required by the requested first screen, implement that screen, render it, critique it, and promote only the decisions supported by evidence.

## Operating rules

- Do not require a particular filename such as `design.md`.
- Do not pause ordinary implementation merely because the design system starts empty.
- Do not fill the repository with blank templates, generic design advice, or tokens with no consumer.
- Do not treat generated starter values as approved taste. Mark them provisional until reviewed through a rendered interface or explicitly approved by the user.
- Prefer native platform behavior, accessibility, and input semantics. Customize presentation through semantic project roles.
- Use references per decision. Never copy one product wholesale or import its brand expression.
- Keep documentation, implementation, previews, and design-gap status connected so later agents can discover the intended owner of a decision.

## 1. Understand the product and platform

Derive as much as possible from the user request, product code, package metadata, and repository instructions:

- primary user and job;
- target platform, form factor, and input modes;
- product character and emotional tone;
- first screen's user goal and dominant scan path;
- accessibility, localization, resizing, and appearance requirements;
- any products, screenshots, bookmarks, or collections the user already trusts.

Ask only when the missing answer would materially change the product flow or platform architecture. Otherwise record a reversible assumption and continue.

## 2. Audit before scaffolding

Confirm whether the project already has any useful fragments:

- framework theme, asset catalog, CSS variables, appearance environment, or typography helpers;
- reusable controls or layout containers;
- screenshots, prototypes, preview fixtures, Storybook stories, snapshot tests, or design notes;
- repository instructions that future UI agents will read;
- accidental styling defaults that should not become precedent.

Preserve useful infrastructure. Evolve it toward semantic roles instead of creating a competing second system.

## 3. Build a starter reference source map

If the user supplied references, begin with those. Otherwise inspect a compact starter set:

- the target platform's first-party conventions for behavior;
- several examples from two or three mature production interfaces with the same interaction or information-structure problem;
- a focused Mobbin or curated-collection search when stronger direct sources are unavailable.

Cover the lenses the first screen actually needs: whole-product system, end-to-end flow, screen archetype/category, component family, data shape, states/scale, platform convention, and project continuity. For material or novel UI, a reasonable default is four to eight examples across at least four applicable lenses, including multiple areas of a preferred product rather than one isolated screenshot.

Record influence at decision level:

| Source and examples | Status and lens | Problem inspected | Pattern evidence | Reject or omit | Project adaptation |
|---|---|---|---|---|---|
| Product, flow, screens, or component family | Evidence status plus flow, archetype, component, data, state, system, platform, or internal lens | Concrete UI problem | Scan order, text emphasis, containment, icon, alignment, action, data, or state relationship | Source flaw, trend, signature, or irrelevant behavior | Platform and product-specific translation |

Do not list a product without naming the examples inspected and what they are evidence for. Label project screenshots as audit evidence unless the user explicitly approves them. Treat production references as reviewed evidence, not flawless authority.

## 4. Establish the minimum visual contract

Use `project-visual-language-template.md` as a checklist. Fill only evidence-backed sections, but cover these foundations before the first screen is declared complete:

### Identity and platform posture

- three to five product qualities and explicit “never feels like” qualities;
- native-versus-custom boundary;
- shared product identity versus platform-specific adaptation.

### Semantic visual roles

- page, section, row, card, supporting, metadata, and micro typography;
- readable base text and hierarchy relationships;
- bounded primary, secondary, tertiary, disabled, and semantic-status emphasis roles;
- required-copy contrast rules that prevent explanatory content from becoming faint metadata;
- base, grouped, content, floating, accent, and semantic-status color roles;
- bare-glyph, tiled, tinted, semantic-status, and brand icon policy;
- radius, border, elevation, and material philosophy.

### Composition grammar

- a compact spacing relationship ladder;
- stable alignment anchors for repeated anatomy;
- an explicit alignment ledger for recurring rows and cards;
- content width and minimum/ideal/maximum sizing rules;
- legal surface nesting and environmental separation;
- a containment budget and subtraction rule for cards, fills, borders, dividers, badges, icon tiles, and rounded rectangles;
- typography recipes for the first recurring archetypes.

### Interaction grammar

- primary, secondary, and destructive action hierarchy;
- hover, pressed, selected, focus, disabled, loading, error, and empty behavior;
- pointer, touch, keyboard, motion, and reduced-motion expectations;
- native control policy: what remains native, what receives a project presentation, and what warrants a reusable custom control.

Use real values only when the first interface needs them. Give each value a semantic owner and avoid raw feature-local constants.

## 5. Create a discoverable project contract

Adapt to the repository's existing documentation conventions. One concise document is acceptable for a small project; split documents only when it improves discovery.

The project must have a discoverable design entry point that covers or links to:

- visual language and platform posture;
- reference source map;
- composition and implementation foundations;
- reusable component and screen-pattern catalog;
- golden screens or reviewed preview locations;
- unresolved design gaps and decision status.

Add a short bridge to `AGENTS.md` or the repository's equivalent instructions:

> Before material UI work, read the project design entry point. Reuse semantic foundations and components, render the change in application context, perform a failure-seeking self-critique, and report recurring design gaps instead of adding unexplained local styling.

Keep the bridge concise and point to the project artifacts. Do not duplicate the entire skill in repository instructions.

## 6. Implement the minimum reusable foundation

Create the smallest idiomatic implementation that can own the first screen's recurring decisions:

- semantic typography, color, spacing, radius, surface, and motion roles;
- page or content-region composition;
- the recurring row/cell and card/surface anatomy the screen needs;
- native control presentation or reusable variants where framework defaults conflict;
- deterministic fixtures and an isolated component catalog or preview.

Use the relevant platform reference for implementation:

- SwiftUI/AppKit/UIKit: semantic Swift APIs, dynamic appearance, accessibility, previews, and native input behavior;
- web: theme or CSS custom properties, semantic primitives, focus-visible and pointer states, responsive behavior, and a component preview surface.

Do not build unused controls “for completeness.” Add the next primitive when a real screen exposes the need.

For high-cost regressions, add focused tests or source policies such as:

- foundation roles must remain semantically named;
- shared rows own hover and selection treatment;
- floating surfaces own border/elevation behavior;
- feature screens cannot silently bypass the approved base typography.

Tests enforce ownership; rendered review determines taste.

## 7. Use the first screen to close the loop

Treat the requested first interface as both product work and a system calibration surface:

1. Perform the reference-first design preflight.
2. Confirm that the reference set covers the relevant flow, component, data, state, system, platform, and internal-continuity questions.
3. Implement with the starter foundations.
4. Render isolated component states and the integrated screen.
5. Check light/dark appearance, resizable or responsive behavior, and important edge states as relevant.
6. Run the self-critique and visual quality gate.
7. Complete a structural/subtraction pass and a visual hierarchy/alignment pass.
8. Re-render, compare the candidate with both the extracted reference patterns and the project's broader language, and repeat while a material improvement remains.
9. Promote proven relationships into semantic roles or shared components.
10. Record unresolved choices as design gaps.
11. Mark the integrated render as a **candidate golden** until the user or project explicitly approves it.

This loop is what turns provisional starter values into a project-specific system.

## 8. Readiness check

The project can “hit the ground running” when:

- future agents can find the design entry point from repository instructions;
- the reference map explains where to look and what to borrow;
- the reference set covers more than one isolated screen and records source treatments that should not transfer;
- the first screen uses semantic foundations rather than scattered raw styling;
- the recurring primitives have isolated and integrated previews;
- the first screen has converged through failure-seeking structural and visual critique passes;
- provisional decisions and unresolved gaps are visible;
- no document or component claims approval without reviewed evidence.

## Commentary and handoff

At bootstrap start, send a concise non-blocking update:

> **Fresh-project design bootstrap — proceeding**  
> This project has no established visual contract. I’ll create the minimum reference map, semantic foundations, reusable primitives, and previews needed for the first screen, then validate them through an integrated self-critique.

At handoff, identify:

- artifacts and reusable code created;
- production and platform references used per decision;
- what remains provisional versus approved;
- first-render issues found and corrected;
- gaps the next design pass should close.
