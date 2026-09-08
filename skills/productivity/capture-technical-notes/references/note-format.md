# Note Format

Keep Markdown as the canonical editable content source. Generate matching title-named HTML, PDF, and EPUB editions after the note is complete. The reader-facing note contains the technical content; capture provenance, telemetry, and verification details belong in `watch-manifest.json` and `final-review.md`.

## Required reader-facing order

1. Exact resource title as the only level-one heading.
2. First transcript chapter immediately after the title, normally Introduction.
3. Remaining transcript chapters in chronological order.
4. Optional supplementary material only when the user asks for it.
5. A single References section after the actual note content, unless a link must appear beside the passage that introduces it.

Do not put YAML frontmatter, source metadata, a chapter-marker table, a verification callout, a verification summary, or a table of contents before the first chapter. Do not add organizational labels such as `Verbatim transcript`, `Visual timeline`, or `Code walkthrough`. The timestamped transcript, screenshots, captions, and code should read naturally within each chapter.

## Chapter pattern

```markdown
# <Exact resource title>

## 1. Introduction - 00:00:00-00:01:43

![Title card at 00:00:05](assets/embedded/publication-0005.png)

*00:00:05 - Title card identifies the technical session and presenter.*

**00:00:07 - 00:00:37**

<Source transcript wording in its original sequence.>
```

Copy source-provided section numbers, titles, capitalization, punctuation, and transcript wording exactly. Infer titles only when the source provides none. Disclose an obvious transcription correction next to the affected passage; do not silently improve grammar, tone, terminology, or examples.

## Screenshot placement

- Place each screenshot inside the chapter whose timestamp range contains it.
- Put it immediately after the nearest transcript passage that introduces or explains the visible state.
- Keep screenshots in chronological order within the chapter.
- Render every screenshot as its own standalone Markdown image and caption.
- Never place screenshots in a Markdown table, gallery, column layout, or side-by-side arrangement.
- A single source screenshot may itself contain multiple panels when that is what the technical session showed.
- Use descriptive alt text and include the exact screenshot timestamp in the alt text or caption.
- Keep the uncropped audit frame separately; crop publication images only when every instructional element remains visible.

For a cumulative slide reveal, publish only the final stable frame that contains the completed content. For same-title continuations or meaningful procedure states, retain every complete state needed to preserve unique information, but stack the images vertically in chronological order.

## Code and command screenshots

Keep a code or command screenshot for its editor state, output, selection, or layout context. Put a copyable fenced transcription immediately below that screenshot. For a short sequence of related screenshots, put the consolidated fenced block immediately below the final image in the sequence.

Transcribe the visible union: code lines, closing delimiters, commands, output, status, filenames, and metrics. When the source viewport clips content, describe both the image and fenced block as a visible excerpt. Mark uncertain OCR with `<!-- verify transcription -->` until it is resolved.

## References

Preserve reference provenance explicitly at the end of the note:

```markdown
## References

- **Mentioned in the video:** [Dataset API](https://example.com/api)
- **Creator-provided:** [Course repository](https://example.com/repository)
- **Supplementary:** [Background guide](https://example.com/guide)
```

Capture references that appear visually even when the transcript omits them. Resolve each named resource to its direct destination rather than a generic home page. Add supplementary links only when they materially help later study and never imply that the instructor mentioned them.

## Supplementary material

Omit recaps, explanations, and glossaries unless the user requests them. When included, place them after the transcript chapters under `Supplementary reference — not part of the transcript` or an equally explicit heading, before References. Never interleave paraphrases with the verbatim transcript.

## Presentation editions

Generate the HTML presentation source and its PDF and EPUB derivatives only after the Markdown note has this final structure. Read [export-formats.md](export-formats.md) for the shared HTML pipeline and format-specific checks.
