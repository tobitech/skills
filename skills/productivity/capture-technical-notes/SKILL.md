---
name: capture-technical-notes
description: Turn technical videos into title-named Markdown, HTML, PDF, and EPUB notes with verbatim source transcripts, exact supplied section titles, inline instructional visuals, readable syntax-highlighted code, and a mandatory second-pass completeness review. Use when Codex is asked to watch, capture, summarize, document, or take notes from a YouTube video, an authenticated course player, a non-downloadable technical site, or a local video, especially when the user requires auditable transcript-and-visual evidence or polished web, print, or Kindle-friendly output.
---

# Capture Technical Notes

Create a canonical Markdown note, a polished HTML presentation edition, matching PDF and EPUB editions generated from the HTML structure, and an evidence manifest. Treat “verified” as verified transcript-and-visual coverage, never as proof of human-like attention.

## Choose the source mode

1. Use **browser mode** when the user names the in-app browser, the video requires an authenticated session, or the media cannot be downloaded. Read [references/browser-audit.md](references/browser-audit.md) before controlling the player.
2. Use **local mode** when the user supplies a video file.
3. Use **download mode** only when the site permits it and `yt-dlp` can access the media. Run `python3 <skill-dir>/scripts/manifest_tool.py doctor` first. Never bypass DRM, paywalls, access controls, or site restrictions.

When the requested host is blocked by ads, rate limits, or unreliable seeking, an official creator-hosted copy may be used only after establishing that it is the same technical session from creator identity, title, duration, chapter sequence, and visible content. Record both the requested URL and capture URL, preserve the requested chapter markers, and disclose the fallback in `final-review.md`. If identity cannot be established, do not silently substitute another upload.

Use the in-app Browser skill for browser mode. If that skill is unavailable, mark browser verification blocked; do not silently substitute Chrome or another browser unless the user approves it. Use a purpose-built connector to publish into Notion when available; otherwise keep Markdown as the canonical artifact and edit Notion through the browser only when the user explicitly requests it.

## Create the working set

Use the resource's exact publisher-visible title as the note title and artifact basename. For YouTube, retrieve the title from the requested video's metadata and confirm it against the visible watch-page title. For a local video, use its embedded title metadata when present; otherwise use the filename without its extension. Preserve the exact title in document headings and metadata. Preserve it in filenames too, except that characters forbidden by the active filesystem must be replaced with the closest readable Unicode equivalent; disclose any filename substitution in `final-review.md`.

Store every capture under `~/captured-notes/` in the user's home directory. Create `~/captured-notes/` when it does not exist. Do not interpret “user root” as the filesystem root `/`, and do not save the canonical result in a thread-specific visualization folder unless the user explicitly requests another destination. If the environment restricts writes to the home directory, request the required filesystem approval instead of falling back to another location silently.

Create one directory per technical note. `<resource-title>` below means the exact resource title, subject only to the filesystem exception above:

```text
~/captured-notes/<resource-title>/
├── <resource-title>.md
├── <resource-title>.html
├── <resource-title>.pdf
├── <resource-title>.epub
├── final-review.md
├── final-review-assets.sha256
├── final-review-exports.sha256
├── watch-manifest.json
└── assets/
```

If a directory with the same title already represents the same source, update it without deleting unrelated files. If a different source has the same title, append a stable source identifier to the directory name only; keep the four note artifact filenames title-based.

Resolve `<skill-dir>` to this skill's directory. Copy [assets/note-template.md](assets/note-template.md) to `<resource-title>.md`. Set `<technical-notes-dir>` to `~/captured-notes/<resource-title>/` for all later commands. Initialize the manifest:

```bash
python3 <skill-dir>/scripts/manifest_tool.py init \
  --manifest <technical-notes-dir>/watch-manifest.json \
  --title "<title>" \
  --source "<URL-or-local-path>" \
  --mode browser \
  --duration <seconds> \
  --width <pixels> \
  --height <pixels> \
  --transcript-source site
```

## Capture the transcript

Resolve the transcript language before capture. Use the language the user requests. If the user does not specify a language, produce the final note in English and look for an English transcript or caption track first.

For a YouTube source that permits caption extraction, run `python3 <skill-dir>/scripts/manifest_tool.py doctor`, then run `yt-dlp --list-subs <URL>` before choosing the transcript source. When an English track is available and the user did not request another language, always extract it with `yt-dlp --skip-download` instead of manually copying captions from the rendered player. Prefer a publisher-provided English caption track over a YouTube auto-generated English track. Use an auto-generated track only when no publisher-provided English track is available. Select the exact track reported by `--list-subs` so its provenance is not ambiguous:

```bash
# Inspect publisher-provided and automatic caption tracks separately.
yt-dlp --list-subs <URL>

# Preferred: publisher-provided English captions.
yt-dlp --skip-download --write-subs \
  --sub-langs "<publisher-English-track>" --sub-format vtt <URL>

# Fallback: YouTube auto-generated English captions.
yt-dlp --skip-download --write-auto-subs \
  --sub-langs "<automatic-English-track>" --sub-format vtt <URL>
```

If no English transcript or captions are available, use speech-to-text from authorized local media when permitted, or disclose that English transcript capture is blocked. Do not silently switch to another language.

Prefer, in order:

1. Creator- or publisher-provided transcript or captions.
2. Platform-provided automatic captions.
3. Speech-to-text from authorized local media.

Record the transcript language, source URL, extraction method, exact caption track when applicable, and one explicit provenance label in `watch-manifest.json` and `final-review.md`: `publisher-provided`, `platform-auto-generated`, `creator-provided site transcript`, or `speech-to-text`. Never describe automatic captions as publisher-provided. Do not add this capture metadata before the Introduction in the reader-facing note. Record the same high-level source category in the manifest (`captions`, `site`, or `asr`).

Treat the transcript as source text, not material to summarize. Reproduce the speaker's wording and sequence verbatim. When the transcript supplies numbered sections or chapter titles, copy each number, title, capitalization, and punctuation exactly; do not rename it. Validate supplied chapter timestamps against transcript and visual transitions. When a marker is mistimed, retain the original marker and the semantic assembly range in `final-review.md` rather than adding a marker table before the note. Infer concise titles only when the source has no usable sectioning. Do not rewrite grammar, tone, terminology, or examples for clarity. Correct only an obvious transcription error, and disclose the correction next to the affected passage.

Keep added explanations, recaps, and glossaries outside the raw transcript under a heading such as `Supplementary reference — not part of the transcript`. Never blend a paraphrase into the transcript or substitute a summary for it.

Treat source references as knowledge elements, even when captions omit them. Extract URLs, dataset names, papers, repositories, commands, and citations that appear on slides or in demos. Resolve each to the most direct actionable destination shown or named—session, dataset, paper, repository, or documentation page—not a generic home page, and verify that the destination resolves. If the user supplies an existing note, retain useful supplementary links from it. Label each reference as `mentioned in video`, `creator-provided`, or `supplementary`; never imply that an added resource appeared in the video.

## Audit the visual timeline

Capture the actual rendered video, not thumbnails or search results.

Record raw player telemetry at the beginning, during each playback batch, and at the end:

```bash
python3 <skill-dir>/scripts/manifest_tool.py add-observation \
  --manifest <technical-notes-dir>/watch-manifest.json \
  --timestamp <currentTime> \
  --state playing \
  --duration <duration> \
  --ready-state <readyState> \
  --width <videoWidth> \
  --height <videoHeight> \
  --notes "<what established progression>"
```

- Record a checkpoint at the beginning and end, every 5–10 seconds, every transcript boundary, and every meaningful visual change.
- Establish one timestamp basis before capture. For local media, verify representative decoded frames against the player or transcript transitions; never assume a numbered frame file represents `index × interval`. After every browser seek, read back the actual player time and rendered frame before recording it.
- Separate the coverage sweep from the publication pass. Use frequent checkpoints to prove continuity, then revisit selected timestamps for clear note-quality frames.
- Record coverage-sweep frames with `--role audit` and note-quality significant visuals with `--role publication`. Keep both roles in monotonic timeline order.
- Describe visual facts unavailable from the transcript: slide layout, chart axes, colors, IDE state, code, terminal output, cursor location, or UI transitions.
- Classify each retained frame as `slide`, `slide-build`, `demo`, `code`, `diagram`, `talking-head`, or `other`.
- Group candidate frames into slide families by title, layout, and persistent content; never deduplicate by title alone.
- For a cumulative presentation slide, keep earlier states as `slide-build` audit evidence and publish the last stable frame that contains the maximal completed content. Before leaving the section, confirm that the publication frame covers the union of every bullet, label, code line, diagram element, and source reference revealed in that family.
- A meaningful procedure or code sequence may retain earlier states when their order helps the reader follow the instructor's actions. It must also include the final maximal state, omit states that add no useful transition, keep every image vertically stacked, and keep the copyable consolidated code immediately below the sequence. Do not misclassify an incomplete slide as a procedure sequence merely to retain it.
- When same-title frames replace or introduce material rather than strictly adding to the prior frame, treat them as distinct continuations. Publish every complete state needed to preserve their unique information in chronological order.
- Treat every source transcript end time as a mandatory publication probe. For each section with instructional visuals, seek to approximately one second before the section ends, capture the last stable state before the next section, and compare it with the proposed publication frame. A periodic 5–10-second checkpoint cannot substitute for this boundary probe.
- During fast code scrolling, animated zooms, terminals, or demo state changes, sample at 0.25–1-second intervals around the transition until consecutive frames prove the overlap. Preserve closure lines, outputs, status text, and the handoff between continuations; a complete fenced block cannot repair a screenshot described as complete when the screenshot is visibly clipped.
- Reject blur, transitions, obstructed controls, decorative talking-head repetition, and near-duplicates.
- After a seek or slide change, wait for media readiness and for visible slide-build or code animations to settle. Confirm that the retained frame shows the completed statement, command, or output; recapture when it does not.
- Keep uncropped audit frames for provenance. For note-quality publication images, crop away the presenter, player chrome, and empty margins whenever every relevant title, bullet, diagram, plot, code line, output, caption, and URL remains intact. Prefer the smallest complete instructional rectangle; keep presenter pixels only when removing them would cut relevant content.
- Determine crops from the actual instructional rectangle in each frame; do not reuse a fixed half-screen crop without checking titles, bullets, footers, code endings, and related-session links at full resolution.
- For a supplied deck, align original pages to video timestamps and embed the higher-resolution original while retaining the rendered-video checkpoint as provenance.
- For demos, retain stable before/after states as separate, vertically stacked images in chronological order. Never place screenshots in Markdown tables or side by side.

Add each retained checkpoint:

```bash
python3 <skill-dir>/scripts/manifest_tool.py add-checkpoint \
  --manifest <technical-notes-dir>/watch-manifest.json \
  --timestamp <seconds> \
  --frame <technical-notes-dir>/assets/<frame>.png \
  --kind slide \
  --description "<visual-only facts>" \
  --transcript-section "<section title>" \
  --note-anchor "<heading or block id>" \
  --capture-method browser-rendered \
  --role publication
```

Record each dedicated section-end probe with `--role boundary`, then persist the completion comparison rather than leaving it only in prose:

```bash
python3 <skill-dir>/scripts/manifest_tool.py add-section-completion \
  --manifest <technical-notes-dir>/watch-manifest.json \
  --section "<number and exact title>" \
  --section-end <seconds> \
  --boundary-timestamp <seconds> \
  --boundary-frame <technical-notes-dir>/assets/<boundary>.png \
  --knowledge-union "<all visible knowledge elements>" \
  --publication-frame <technical-notes-dir>/assets/<publication-1>.png \
  --publication-frame <technical-notes-dir>/assets/<publication-2>.png \
  --result pass \
  --notes "<how the publication union covers the boundary and slide family>"
```

## Assemble the note

Follow [references/note-format.md](references/note-format.md).

- Preserve chronological order.
- Start the reader-facing Markdown with the exact `# <resource-title>`, followed immediately by the first transcript chapter, normally Introduction. Do not place YAML frontmatter, source metadata, a chapter-marker table, a verification callout, a verification summary, or other capture-process material before that chapter. Keep provenance and verification details in `watch-manifest.json` and `final-review.md`.
- Do not add organizational labels such as `Verbatim transcript`, `Visual timeline`, or `Code walkthrough`. The timestamped transcript, visuals, and fenced code should read naturally inside each chapter.
- Place each visual immediately after the transcript passage that introduces it.
- Keep every screenshot as its own standalone Markdown image and caption, vertically stacked in chronological order. Do not use screenshot tables or side-by-side image layouts. A single source screenshot may itself contain multiple panels when that is what the video showed.
- Whenever a screenshot contains code or commands, keep the screenshot and place a copyable fenced code block immediately below it. For a short sequence of code screenshots, place the consolidated fenced block immediately below the final image in that sequence. Transcribe the visible union: every code line, closing delimiter, command, output, status, filename, and metric shown across the retained frames. When the source viewport itself clips content, describe it as a visible excerpt; never call it complete. Include visible outputs as comments or a separate output block.
- Mark uncertain OCR or inferred code for review.
- Put concise explanations only in a clearly labeled supplementary section; never replace or interleave them with the verbatim transcript.
- Add a references block near the section where each source is introduced. Distinguish in-video references from supplementary enrichment.
- Put a single `## References` section after the actual note content unless a source link must appear next to the passage where it is introduced. Keep source and verification records out of the reader-facing note unless the user explicitly requests them there.

## Export the HTML and portable editions

After the Markdown note is complete, read [references/export-formats.md](references/export-formats.md). Generate `<resource-title>.html` as the shared presentation source, then generate `<resource-title>.pdf` and `<resource-title>.epub` from its semantic article and chapter structure. Markdown remains the canonical editable content source; HTML is the canonical presentation/export source. All editions must carry the exact resource title in their document metadata and must contain every local instructional image, diagram, slide, screenshot, code block, reference, and chapter present in the Markdown note.

The HTML article must begin with the exact title and then the first chapter, contain one semantic section per chapter, render screenshots as separate full-width figures, and contain no screenshot tables or side-by-side galleries. Use note-relative assets, responsive image sizing with intrinsic dimensions, readable syntax-highlighted code with selectable source text, accessible navigation outside the article, and print styles suitable for the PDF. Verify it at ordinary desktop and phone widths before exporting.

Do not satisfy this requirement by changing file extensions. Regenerate the HTML, PDF, and EPUB after any content or embedded-asset change; regenerate affected portable editions after an HTML presentation-style change. If a required converter is unavailable, install or enable it only with the user's authorization when required; otherwise report the capture as incomplete rather than silently omitting an edition.

## Spot-check and verify

After assembling the note and completing checkpoint coverage, select timestamps across the beginning, middle, and end that were not chosen merely because they were convenient. Revisit each timestamp, capture a fresh frame, compare it with the recorded visual state, and record the result:

```bash
python3 <skill-dir>/scripts/manifest_tool.py add-spot-check \
  --manifest <technical-notes-dir>/watch-manifest.json \
  --timestamp <seconds> \
  --frame <technical-notes-dir>/assets/<spot-check>.png \
  --result pass \
  --notes "<what was independently confirmed>"
```

Open every fresh spot-check frame and record the concrete visual facts compared. File existence or a new hash alone is not a passing visual inspection.

Finalize using the actual counts:

```bash
python3 <skill-dir>/scripts/manifest_tool.py finalize \
  --manifest <technical-notes-dir>/watch-manifest.json \
  --transcript-total <count> \
  --transcript-mapped <count> \
  --visual-events-total <count> \
  --visual-events-captured <count> \
  --max-gap-seconds 10 \
  --min-spot-checks 3 \
  --min-playback-observations 3

python3 <skill-dir>/scripts/manifest_tool.py validate \
  --manifest <technical-notes-dir>/watch-manifest.json
```

## Run the mandatory second-pass review

Only after spot checks are recorded, the manifest is finalized and validated, the title-named Markdown is in its intended final form, and its HTML, PDF, and EPUB editions have been exported, read [references/final-review.md](references/final-review.md). Copy [assets/final-review-template.md](assets/final-review-template.md) to `<technical-notes-dir>/final-review.md` and review the finished `<resource-title>.md`, `<resource-title>.html`, `<resource-title>.pdf`, and `<resource-title>.epub` against the raw evidence from scratch.

- Review every transcript section; do not sample.
- Compare each embedded visual with its section-boundary capture and the full slide family.
- Check transcript fidelity, visual completeness, crop integrity, code transcription, reference provenance, chronology, file existence, and consistency with the finalized manifest.
- Prefer a fresh subagent when available and safe. Give it the skill, assembled note, finalized manifest, and raw evidence, but not prior publication decisions or comparison conclusions. Otherwise perform a fresh self-review using the same matrix.
- Resolve every failure, then restart the second pass from section 1. Do not merely recheck the corrected row.
- Record the SHA-256 of the exact reviewed title-named Markdown and finalized manifest in `final-review.md`; the note itself should link to that artifact instead of trying to contain its own hash.
- Write `final-review-assets.sha256` with one SHA-256 entry for every local image or other asset embedded by the Markdown note, using paths relative to the technical-notes directory, and verify every entry before passing.
- Write `final-review-exports.sha256` with entries for the title-named HTML, PDF, and EPUB in stable lexical order. Verify all three entries, inspect the HTML at desktop and phone widths, visually review every PDF page, and verify that the EPUB package contains every referenced local asset and a readable chapter spine.
- Any subsequent change to the Markdown note, an embedded publication asset, code block, link, manifest, HTML, PDF, or EPUB invalidates the review and requires the affected exports and the complete second pass to be regenerated.
- Do not report `verified` unless every section row and every global check passes and the recorded note hash still matches.

Read [references/verification-standard.md](references/verification-standard.md) before reporting the verdict. If verification fails, deliver the useful draft but label it `unverified` and list the exact gaps. Never claim the video was fully processed when playback telemetry, rendered frames, or end-to-end coverage could not be established.

## Finish

Deliver the title-named Markdown, HTML, PDF, EPUB, assets, and manifest together from `~/captured-notes/<resource-title>/`. Report:

- transcript coverage;
- visual-event coverage;
- maximum checkpoint gap;
- passed spot checks;
- second-pass review mode, reviewed-note hash, and pass count;
- playback observations and span;
- HTML desktop/mobile verification, PDF page/render verification, and EPUB package/asset verification;
- any site/player limitations;
- the precise verdict: `verified`, `unverified`, or `draft`.
