# Final Second-Pass Review

Run this review only after the note has been fully assembled, spot checks are recorded, and the manifest has been finalized and validated. Treat it as an adversarial inspection of another author's work; do not trust the original publication choices. This is the last verification gate: do not mutate the note, publication assets, links, or manifest after it passes.

## Review inputs

Use the finished title-named Markdown, HTML, PDF, and EPUB, `watch-manifest.json`, uncropped audit frames, section-boundary captures, publication derivatives, transcript source, and any fenced code or reference links in the note. Do not use a comparison report or prior conclusions as evidence.

## Review every section

For each transcript section:

1. Confirm the supplied section number, title, wording, order, and timestamp are preserved.
2. Build the visible knowledge-element union from the boundary capture and all frames in the slide family.
3. Confirm the note's image or continuation sequence covers that union without relying on the transcript to replace omitted visual information. Earlier strict-subset frames are defects for ordinary slide builds, but are allowed in a meaningful procedure/code sequence when they show sequential states and the final maximal state is also present. Every retained frame must be a separate vertically stacked figure.
4. Inspect the actual publication file for clipped titles, bullets, code, outputs, diagrams, axes, captions, URLs, presenter obstruction, player controls, seek overlays, and unreadable scaling.
5. Confirm every code or command screenshot has an accurate fenced transcription immediately below it, including visible output.
6. Confirm each visible or added resource has a working link and the correct provenance label.
7. Mark the row `pass` only when every applicable check passes. Record the exact defect otherwise.

After any correction, restart at the first section. A targeted recheck is insufficient because paths, crops, ordering, or shared images may have changed elsewhere.

## Review global properties

Confirm that the Markdown starts with the exact title and then the first chapter, with no metadata preface or verification summary. Confirm that all image paths exist, visuals and transcript sections remain chronological, screenshots are never in tables or side-by-side layouts, supplementary prose is clearly separated, repeated images are intentional, `final-review.md` matches the manifest verdict, and no earlier cumulative slide build substitutes for the final maximal state. Intentional procedure/code sequences may retain meaningful earlier states only when the final maximal state is also present.

Inspect the HTML at ordinary desktop and phone widths. Confirm that the document title is exact, the article begins with the title and first chapter, chapters are semantic sections in order, every screenshot loads as its own figure with intrinsic dimensions, code does not widen the page, navigation remains outside the article, and the page contains no screenshot tables or unwanted editorial labels. Confirm every language-tagged code block remains selectable, contains syntax-highlighting spans, uses distinct high-contrast token colors, and is close enough to body-text size to read comfortably at both widths.

Render every PDF page to images and visually inspect them for missing assets, blank pages, clipping, overlap, broken glyphs, unreadable code, and damaged links or captions. Inspect every code-bearing page at normal viewing size: require at least `8.5pt` code, preserved indentation, visible syntax colors when supported, and no clipped long lines or sparse pages caused by an unsplittable block. Inspect the PDF metadata and confirm its title exactly matches the resource title. Confirm the PDF was generated from the reviewed HTML article.

Validate the EPUB archive, package manifest, navigation document, and reading-order spine. Confirm it was generated from the reviewed HTML chapter fragments, every local asset referenced by the HTML is packaged, every chapter is reachable in order, images are readable at common e-reader widths, and the EPUB metadata title exactly matches the resource title. Confirm highlighted code spans and their local CSS are packaged, code remains selectable, and its reader-width scale is comparable to the prose. Use `epubcheck` when available; if it is unavailable, record that limitation and perform archive, XML, manifest, link, and reader-preview checks manually.

Only after all rows and global checks pass:

1. Compute `shasum -a 256 "<resource-title>.md"` and `shasum -a 256 watch-manifest.json`. Record both hashes in `final-review.md`, not inside the Markdown note; embedding a file's own hash in that file would be self-referential.
2. Extract every local asset embedded by the Markdown, compute its SHA-256, and write one entry per file to `final-review-assets.sha256` using technical-note-relative paths in stable lexical order.
3. Verify the asset checksum file from the technical-notes directory with `shasum -a 256 -c final-review-assets.sha256` and record the number of passing assets in `final-review.md`.
4. Write the title-named HTML, PDF, and EPUB hashes to `final-review-exports.sha256` in stable lexical order, verify all three entries, and record their browser/rendering/package checks in `final-review.md`.

If the current note hash, manifest hash, embedded-asset checksum, or HTML/PDF/EPUB checksum differs later, treat the review as stale, regenerate affected exports, and rerun the review completely.

Use a fresh independent subagent when available and safe; otherwise use a fresh self-review. Independence improves error detection but does not replace the exhaustive matrix.
