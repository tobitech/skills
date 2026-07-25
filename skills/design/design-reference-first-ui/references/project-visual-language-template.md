# Project Visual Language Template

Use this structure when establishing project-specific design guidance. Keep it concise and evidence-backed. In a fresh project, label unreviewed starter decisions as provisional.

## Contents

- [Status and ownership](#status-and-ownership)
- [Product character](#product-character)
- [Platform posture](#platform-posture)
- [Reference source map](#reference-source-map)
- [Visual roles](#visual-roles)
- [Composition foundation](#composition-foundation)
- [Interaction rules](#interaction-rules)
- [Implementation map](#implementation-map)
- [Screen archetypes](#screen-archetypes)
- [Golden screens](#golden-screens)
- [Explicit anti-patterns](#explicit-anti-patterns)
- [Open design decisions](#open-design-decisions)

## Status and ownership

- Design entry point and implementation owner
- Last reviewed date
- Approved, provisional, and deprecated guidance
- Locations of component previews and golden screens

## Product character

- Three to five qualities the interface should consistently express
- Emotional tone
- What the product should never feel like

## Platform posture

- Target platforms
- Native-versus-custom boundary
- Shared identity versus platform-specific adaptation

## Reference source map

List approved internal and production references. For each, record:

- screen or flow;
- evidence status: approved, external inspiration, or current-state audit;
- design problem it demonstrates;
- ranked information and intended scan order;
- text-emphasis relationships and maximum neutral levels;
- boundary count, surface strategy, and deliberate omissions;
- icon treatment and explicit alignment anchors;
- decisions to adopt;
- decisions not to transfer;
- relevant target platform.

## Visual roles

Define:

- workspace, section, card, row, supporting, metadata, and micro typography;
- primary, secondary, tertiary, disabled, accent, semantic-status, and brand color-emphasis roles;
- rules that keep required explanatory copy readable and reserve tertiary emphasis for optional metadata;
- neutral bare-glyph, tiled, tinted, semantic-status, and brand icon roles;
- surface, border, elevation, and radius philosophy;
- density, row height, padding, grouping, and content-width conventions.

Prefer semantic roles over raw values in feature code.

## Composition foundation

Define relationships in addition to values:

- spacing ladder from paired content through major page regions;
- repeated alignment anchors for icons, text baselines, copy columns, and trailing controls;
- an alignment ledger for recurring rows and cards, including single-line and multiline behavior;
- content-derived sizing, stable frames, and minimum/ideal/maximum width rules;
- named base, grouped, content, and floating surface planes with legal nesting;
- a containment budget that requires a semantic reason for cards, fills, borders, dividers, badges, icon tiles, and nested surfaces;
- a default bare-icon policy and the roles that earn a tile, tint, or independent surface;
- typography recipes for recurring page headers, rows, settings, cards, and metadata.

Record when a grid or optical correction applies. Treat proportional systems as exploration aids, not mandatory geometry.

## Interaction rules

Define:

- primary and secondary action hierarchy;
- toolbar and navigation responsibilities;
- placement of persistent settings;
- hover, focus, pressed, selected, expanded, and editing behavior;
- motion and feedback boundaries;
- keyboard, touch, pointer, and accessibility expectations.

## Implementation map

Record where each reusable decision lives:

- semantic tokens and named metrics;
- shared components and supported variants;
- native-control presentation policies;
- preview, story, fixture, or snapshot locations;
- focused source-policy or regression tests.

## Screen archetypes

Document the structures the product uses repeatedly, such as:

- settings or form;
- list-detail workspace;
- dashboard or home;
- review and approval;
- inspector;
- creation flow;
- empty state;
- task, activity, or transcript.

For each, state scan order, action placement, preferred components, and important states.

## Golden screens

Maintain a small set of explicitly approved rendered examples. Annotate what each example teaches. Include normal and important edge states where practical.

Keep unapproved first renders in a separate candidate state; do not silently treat implementation as approval.

## Explicit anti-patterns

Record rejected treatments with a reason, such as:

- decorative accent icons for neutral taxonomy;
- explanatory prose rendered as microcopy;
- required text rendered with tertiary or disabled emphasis;
- every text block rendered with the same dark emphasis;
- persistent settings placed among transient toolbar commands;
- nested surfaces without meaningful containment;
- decorative icon tiles placed on already bounded cards;
- repeated controls positioned by unrelated spacer chains instead of a shared trailing anchor;
- inconsistent alignment between sibling components.

## Open design decisions

Track unresolved gaps with:

- pattern or decision;
- evidence reviewed;
- provisional direction;
- status;
- intended final token, component, pattern, or documentation home.
