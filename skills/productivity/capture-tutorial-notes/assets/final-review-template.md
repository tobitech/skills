# Final second-pass review

- Reviewed artifacts: `<resource-title>.md` · `<resource-title>.html` · `<resource-title>.pdf` · `<resource-title>.epub`
- Reviewed note SHA-256: `<compute only after all checks pass>`
- Reviewed manifest SHA-256: `<compute only after all checks pass>`
- Embedded-asset checksums: [`final-review-assets.sha256`](final-review-assets.sha256) · `<passed>/<total>`
- Export checksums: [`final-review-exports.sha256`](final-review-exports.sha256) · `<3/3>`
- HTML review: `<exact title; title then first chapter; sections/figures/tables; desktop and phone result>`
- PDF review: `<page count; every page rendered and inspected; exact metadata title; result>`
- EPUB review: `<archive/package/spine/assets/metadata/reader-preview result>`
- Review mode: `<independent-agent|fresh-self-review>`
- Completed at: `<UTC timestamp>`

| Section | Transcript | Visual union | Crop | Code | References | Result | Findings |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `<source section title>` | `<pass|fail>` | `<pass|fail|n/a>` | `<pass|fail|n/a>` | `<pass|fail|n/a>` | `<pass|fail|n/a>` | `<pass|fail>` | `<exact defect or none>` |

## Global checks

- [ ] Every transcript section has exactly one review row.
- [ ] All embedded image paths exist and open successfully.
- [ ] Visuals and transcript sections remain chronological.
- [ ] No earlier cumulative slide build substitutes for the final maximal state; intentional procedure/code sequences include that final state.
- [ ] Same-title continuations preserve every unique knowledge element.
- [ ] Crops retain all instructional content and exclude avoidable presenter/player chrome.
- [ ] Every screenshot is a standalone vertically stacked figure; no screenshot appears in a table or side-by-side layout.
- [ ] Every code screenshot or related sequence has copyable fenced code immediately below it.
- [ ] References have working links and correct provenance labels.
- [ ] Supplementary prose is clearly separated from the verbatim transcript.
- [ ] The Markdown starts with the exact title and then the first chapter, with no metadata preface, verification summary, or unwanted editorial labels.
- [ ] The review verdict and recorded coverage metrics match `watch-manifest.json`.
- [ ] The recorded note SHA-256 matches the current title-named Markdown.
- [ ] The recorded manifest SHA-256 matches the finalized `watch-manifest.json`.
- [ ] Every checksum in `final-review-assets.sha256` matches the local asset embedded by the Markdown.
- [ ] The HTML article preserves every chapter, timestamp, code block, reference, and local image from the Markdown.
- [ ] The HTML passes desktop and phone-width layout checks without broken images or horizontal page overflow.
- [ ] Every language-tagged HTML code block remains selectable, contains syntax-highlighting spans, and is comfortably readable at desktop and phone widths.
- [ ] Every PDF page renders cleanly and the title metadata matches the exact resource title.
- [ ] PDF code is at least 8.5pt with preserved indentation, visible syntax colors when supported, and no clipped long lines or sparse pagination defects.
- [ ] The EPUB package, navigation, reading-order spine, and title metadata validate.
- [ ] EPUB code retains its highlighting CSS, selectable text, and a scale comparable to the prose at common reader widths.
- [ ] The PDF and EPUB are generated from the reviewed HTML structure.
- [ ] Every local asset referenced by the HTML is embedded in both portable editions.
- [ ] The HTML, PDF, and EPUB checksums match `final-review-exports.sha256`.

## Verdict

`<pass|fail>`

Do not mark `pass` while any section or global check fails.
