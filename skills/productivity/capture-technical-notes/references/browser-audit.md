# Browser Audit

Use this procedure for authenticated, streamed, or non-downloadable technical videos.

## Establish the player

1. Follow the in-app Browser skill’s setup, tab-claiming, interaction, and cleanup rules.
2. Claim the user’s existing course tab instead of opening a duplicate.
3. Read a fresh DOM snapshot and identify the exact player iframe or video element from observed attributes.
4. Locate the real `video` element, including through a frame locator when necessary.
5. Read `currentTime`, `duration`, `paused`, `readyState`, `videoWidth`, and `videoHeight` through a read-only locator evaluation. Do not mutate media state through page evaluation.
6. Control play, pause, seek, and speed only through visible player controls or supported browser interaction APIs.
7. Record the initial telemetry with `manifest_tool.py add-observation` before capture begins.

For YouTube and similar hosts, first clear consent, ad, age, sign-in, or rate-limit states through normal visible controls. Do not treat an ad duration, placeholder thumbnail, stale frame, or a seek that the player ignored as technical-session telemetry. If the requested host remains unreliable, follow the skill's identical official-source fallback rule and disclose it.

Fail browser verification when no real player telemetry is available, screenshots are blank or protected, or playback cannot be observed progressing. Continue with transcript-only notes only if the user accepts an `unverified` result.

## Capture in bounded batches

Process playback in batches short enough to provide a user update at least once per minute.

For each batch:

1. Confirm the observed player time.
2. Record a telemetry observation, including playback state, duration, readiness, and resolution.
3. Capture the video region rather than the whole page when practical.
4. Save screenshot bytes under the technical note’s `assets/` directory.
5. After a seek, allow roughly 1–2 seconds for slide builds, syntax highlighting, plots, and terminal output to finish rendering; media readiness alone is insufficient.
6. Read back `currentTime` after the seek and describe the rendered frame before deciding whether to retain it. Reject a stale frame or a timestamp outside the intended tolerance.
7. Add retained frames to the manifest immediately.
8. Confirm that time advanced before starting the next batch.

After the interval sweep, run a separate section-boundary sweep. For every timestamped transcript section with instructional visuals, seek to `section_end - 1 second` or the latest stable moment before the next title appears. Move the pointer away from the player controls, allow overlays to disappear, and capture that state even when an earlier checkpoint looked complete. Compare the boundary state with the proposed publication image before selecting it.

Use a default checkpoint interval of five seconds for demos and ten seconds for mostly static slides. Add checkpoints at every transcript boundary regardless of the interval. Reduce the interval during fast IDE, terminal, drawing, or UI demonstrations.

For fast code scrolls, animated zooms, or output changes, inspect the transition at 0.25–1-second resolution. Require overlapping visible lines or state between continuation frames so no code, closing delimiter, output, or status can fall into an unsampled gap.

Playback may run at up to 2× when the player supports it, but checkpoint spacing is measured in video time. Return to 1× around dense demonstrations when needed.

## Select meaningful visuals

Retain:

- a new slide or meaningful animation build;
- a chart, diagram, table, or equation being explained;
- a stable IDE, terminal, browser, or application state after an action;
- code or output that the transcript alone does not preserve;
- a completed animation/build state when earlier frames show partial bullets, code, or output;
- URLs, dataset names, citations, repository names, and other source references visible only on screen;
- a visual comparison or sequence.

Discard:

- repeated presenter-only frames;
- fades, spinners, tooltips covering the subject, and seek overlays;
- frames with no meaningful difference from a retained frame;
- frames whose only information is already captured more clearly by a supplied slide.

For procedure or code demo flows, retain before/after states and any indispensable intermediate state, even when later code visually contains earlier code, because the sequence can document the instructor's actions. Always include the final maximal state, omit redundant transitions, label the flow explicitly, and group no more than four frames in one row so each remains readable.

Use two passes when the player animates content: an audit pass at the configured interval, then a publication pass that revisits important timestamps and captures stable completed states. Keep the audit checkpoints for provenance even when the clearer publication frames are the ones embedded in the note.

For publication derivatives, crop to the instructional content. Remove presenter-only regions, player controls, and empty margins when doing so preserves every relevant title, bullet, diagram, plot axis, code line, output, caption, and visible source reference. Keep the uncropped audit frame in the evidence set. Do not force a presenter-free crop when the presenter overlaps or points to information that would otherwise be lost.

## Resolve slide builds and continuations

1. Group candidate frames by stable slide identity: title, background, layout, persistent text, and persistent visual elements. Do not use the title as the identity by itself.
2. Inventory the visible knowledge elements in each frame: bullets, sub-bullets, labels, code lines, outputs, diagram nodes, axes, captions, and source references.
3. When a later presentation-slide frame has the same identity and strictly contains the earlier frame's elements, classify the earlier frame as a cumulative `slide-build`. Retain it only as audit evidence and embed the last clear maximal state. For a deliberately labeled procedure/code demo flow, meaningful earlier steps may also be embedded when the final maximal state is present.
4. When a later same-title frame removes, replaces, reflows, or introduces material so neither state contains the other, classify it as a continuation. Retain each complete state whose unique information is required, in chronological order.
5. Use the mandatory `section_end - 1 second` boundary capture to confirm that no later reveal exists. The publication image or continuation sequence must cover the union of the family's knowledge elements.
6. For code or demo sequences, retain useful intermediate states only when they explain an action flow. Always include the completed state and place the consolidated copyable code immediately below the sequence.
7. Treat the retained sequence as a visible-union contract. The adjacent fence must transcribe all visible code, closures, commands, outputs, statuses, filenames, and metrics. If any source viewport remains clipped, label it as an excerpt; do not describe that frame as complete.

Do not discard a frame merely to avoid duplicates when doing so would omit a unique knowledge element.

Before assembly, make a completion matrix with one row per transcript section: section end, boundary-capture timestamp, visible knowledge-element union, selected publication frame or continuation frames, and pass/fail. Record boundary checkpoints with `--role boundary` and persist every row with `manifest_tool.py add-section-completion`. Do not mark the note verified while any instructional section lacks a passing boundary row.

## Prove independent visual access

Descriptions must include at least one visual fact not stated in the adjacent transcript. Examples include the arrangement of a slide, plot shape, axis labels, color coding, visible filename, selected UI control, code line, or terminal result.

After note assembly, choose at least three spot-check timestamps distributed across the video. Revisit and freshly capture those states. Open each fresh frame and record the concrete visual facts compared. Record a pass only when the new visual is consistent with both the earlier checkpoint and the note; a distinct hash by itself is insufficient.

Do not describe this protocol as proof of consciousness or attention. It establishes that Codex accessed and processed the rendered visual timeline with bounded gaps.

If the site exposes no transcript and its audio cannot be made available through an authorized transcription path, continue only as a visual-only `unverified` draft and disclose the missing transcript.
