# Verification Standard

## Allowed verdicts

- `verified`: The transcript and rendered visual timeline satisfy every configured criterion and all evidence files validate.
- `unverified`: A useful note exists, but one or more required criteria failed or the player prevented evidence collection.
- `draft`: Capture or note assembly is still in progress.

Use the phrase **verified transcript-and-visual coverage**. Never state that a person or model “definitely watched attentively.” A note can demonstrate provenance and coverage, not subjective attention.

## Default verification criteria

Require all of the following:

1. A known video duration greater than zero.
2. A checkpoint near both the beginning and end.
3. At least three raw player-telemetry observations distributed from beginning through end, with observable monotonic time progression and at least one playing state. Record one before checkpoint capture, one during it, and one after the final checkpoint batch.
4. No checkpoint gap greater than ten seconds unless the user explicitly chooses a different threshold.
5. Every retained checkpoint has an existing frame, matching SHA-256 hash, classification, timestamp, and non-trivial visual description.
6. All transcript sections are mapped into the note. When a source transcript exists, its supplied section titles and wording are preserved verbatim; supplementary prose is clearly separated.
7. All identified significant visual events have specifically classified `publication` checkpoints, while separate `audit` checkpoints preserve the coverage sweep. For every progressive presentation-slide family, the publication frame is its last stable maximal state; for same-title continuations, the publication sequence covers the union of unique knowledge elements. A labeled procedure/code demo flow may additionally retain meaningful earlier states when it also includes the final maximal state and the sequence materially explains the instructor's actions.
8. Every timestamped transcript section with instructional visuals has a dedicated boundary capture within roughly two seconds of its end, taken before the next section appears, and its completion-matrix row passes. Periodic interval checkpoints do not satisfy this requirement.
9. A mandatory second-pass `final-review.md` covers every transcript section and every global check after note assembly. Every applicable check passes, its recorded hashes match the current title-named Markdown and finalized manifest exactly, every embedded local asset verifies against `final-review-assets.sha256`, and the HTML/PDF/EPUB entries verify against `final-review-exports.sha256`.
10. At least three independently revisited spot checks pass and none fail. Fresh spot-check frames must be captured after checkpoint capture and before the mandatory second-pass review, and must not reuse a checkpoint hash.
11. The requested source and capture source are identical, or an official identical-source fallback is documented with title, creator, duration, chapter, and visible-content evidence. Chapter timestamps are separately validated against transcript and visual transitions.
12. Every code or command publication sequence satisfies the visible-union contract: all visible lines, closing delimiters, outputs, statuses, filenames, and metrics are transcribed, and any source-viewport clipping is explicitly labeled as an excerpt.
13. Matching title-named HTML, PDF, and EPUB editions exist under the tutorial directory and match `final-review-exports.sha256`. The HTML article begins with the exact title and first chapter, preserves the complete Markdown content, uses separate vertically stacked figures with no screenshot tables, and passes desktop/phone checks. The PDF and EPUB are generated from that HTML structure, contain every referenced local publication asset, and pass the PDF rendering and EPUB package/reading-order checks.

For videos shorter than one minute, two spot checks may be accepted only when explicitly configured. For long static presentations, increase the gap threshold only after confirming that intervening frames contain no visual changes.

## Failure rules

Mark the result `unverified` when any of these occur:

- only the transcript was processed;
- the player did not expose duration or observable time progression;
- raw telemetry observations were absent, out of order, or inconsistent with the media;
- rendered screenshots were unavailable, blank, or protected;
- the beginning, end, or a timeline interval was not covered;
- transcript sections or identified visual events were omitted;
- a published presentation slide is superseded by a later cumulative build, a labeled demo flow omits its final maximal state, or a same-title continuation sequence omits a unique knowledge element;
- an instructional transcript section lacks a passing end-boundary capture and completion-matrix row;
- the exhaustive second-pass review is missing, incomplete, failing, or stale because its recorded note or manifest hash no longer matches, or an embedded-asset checksum fails;
- source-provided transcript wording or titles were replaced by paraphrases;
- a code screenshot lacks a copyable fenced transcription directly beneath it;
- a screenshot or continuation is described as complete while visibly clipping code, closing delimiters, output, status, a slide footer, or another knowledge element;
- an official-source fallback is undisclosed or source identity was not established;
- a chapter timestamp is accepted without checking it against transcript and visual transitions;
- a resource link points only to a generic home page when the named direct destination is available;
- an evidence file is missing or its hash changed;
- the title-named Markdown, HTML, PDF, or EPUB is missing, stale, incorrectly titled, fails its checksum, omits a referenced asset, or fails its format-specific browser/rendering/package checks;
- a random spot check failed;
- a spot check was not visually opened and compared, even if its file and hash exist;
- a spot check reused a checkpoint frame or was recorded before checkpoint capture finished;
- playback observations were not recorded before, during, and after checkpoint capture;
- authentication, session expiry, or site behavior interrupted capture.

List exact reasons in the manifest and in the user-facing handoff. Do not convert a failed criterion into a silent exception.

## Evidence interpretation

SHA-256 hashes show that evidence files did not change after being recorded. Playback telemetry shows that the browser observed a real media timeline. Visual descriptions and random recapture checks show that information unavailable from the transcript was processed. Together these provide high-confidence process evidence, not tamper-proof third-party attestation.
