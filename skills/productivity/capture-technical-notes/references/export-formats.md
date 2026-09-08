# HTML, PDF, and EPUB Editions

Use one content pipeline:

```text
final Markdown -> semantic HTML presentation source -> PDF and EPUB
```

Markdown remains the canonical editable content source. The title-named HTML is the canonical presentation/export source. Do not maintain a shortened or independently edited version for any edition.

## Names and metadata

- Use the exact resource title as the Markdown, HTML, PDF, and EPUB basename.
- Use that exact title as the HTML document title and PDF/EPUB metadata title.
- Keep all four artifacts and `assets/` together in `~/captured-notes/<resource-title>/`.
- When the filesystem forbids a title character, use the closest readable substitution in filenames only and record it in `final-review.md`.

## Shared content and asset contract

- The HTML article must preserve the complete Markdown chapter order, transcript wording, timestamp blocks, headings, code, captions, and reference links.
- Keep publication images under the technical-notes directory and use technical-note-relative paths.
- Render every screenshot as a separate semantic `figure`; never create screenshot tables, galleries, or side-by-side layouts.
- Give images descriptive alt text plus intrinsic `width` and `height` so lazy loading does not shift chapter anchors.
- Do not make any edition depend on remote image URLs. Package every local instructional asset into the EPUB and render it into the PDF.
- Ordinary external references remain hyperlinks and do not need to be copied into the package.

## Build the HTML presentation source

Generate `<resource-title>.html` from the final Markdown. Its reader-facing `<article>` must begin with the exact title and then the first chapter. Navigation or other interface elements may sit outside the article, but must not become note content.

Use semantic, accessible markup:

- one `h1` for the exact title;
- one `section` with an `h2` for each chapter and References;
- `figure`, `img`, and `figcaption` for each screenshot;
- `pre` and `code` for copyable code;
- real links and lists for References;
- a skip link and chapter navigation when useful.

### Present code as instructional content

Code must be as legible as the surrounding explanation, not a small monochrome afterthought.

- Give every Markdown fence the correct language tag. Export it as selectable `<pre class="code-listing"><code class="language-…">` text; never rasterize the copyable code to obtain highlighting.
- Apply syntax highlighting at build time and embed the resulting spans and colors in the HTML and EPUB. Do not add a CDN script or another network dependency. Use [../scripts/highlight_code.mjs](../scripts/highlight_code.mjs) as the dependency-free fallback for Swift, JavaScript, TypeScript, Python, shell, and JSON, or use an equivalent local highlighter when one is already available.
- Use or adapt [../assets/code-theme.css](../assets/code-theme.css). Its light neutral surface, generous padding, rounded corners, and palette are based on Apple Developer articles: purple types and calls, magenta keywords, blue numbers, red strings, and muted gray comments.
- Keep screen code close to body-text scale: normally `0.9–1em` of the surrounding text, never below `14px` at the phone layout. Use a line height around `1.55–1.7` and enough padding that the block reads as its own content surface.
- Let code scroll horizontally on screen without widening the page. For print and EPUB, wrap long lines or split a long excerpt at a meaningful boundary instead of shrinking the type until it is difficult to read.
- In generated PDFs, preserve syntax colors as text markup when the PDF engine supports it. Use an embedded or system monospace font, at least `8.5pt` code next to approximately `10pt` body text, and a line height of at least `1.4`. A plain-text PDF fallback must keep the same readable scale and surface treatment.
- Keep token colors high-contrast against the code surface and retain punctuation, spacing, indentation, and source text exactly. Color supports scanning; it must not be the only way code remains understandable.

Use restrained responsive styling with a readable text measure, clear heading hierarchy, high contrast, and system fonts unless local font files are deliberately packaged. On small screens, use one content column and let code scroll horizontally or wrap without widening the page. On print, hide navigation, remove decorative shadows, keep figures together when practical, and start later chapters on clean page boundaries.

Do not add a cover page, metadata preface, verification summary, or editorial labels to the article. Do not insert remote scripts, fonts, trackers, or network dependencies.

## Generate PDF and EPUB from HTML

The PDF generator must consume the semantic HTML article. A browser print engine may use the HTML print CSS directly. A document generator such as ReportLab may parse the HTML article into equivalent flowables when a browser PDF engine is unavailable, but it must not return to an independently shortened Markdown source.

The EPUB generator must consume the same HTML chapter fragments, convert them to valid XHTML when needed, create navigation and spine entries in chapter order, and package every referenced local asset.

Pandoc is acceptable when installed and when the selected HTML-to-PDF and HTML-to-EPUB path preserves the contract. A custom deterministic converter is also acceptable. Never fake an export by changing a filename extension. Request authorization before installing a missing converter when installation is necessary.

EPUB is the portable e-book deliverable for Kindle workflows such as Send to Kindle. Do not generate obsolete MOBI output unless the user explicitly requests it.

## Verify the HTML

1. Confirm the document title exactly matches the resource title.
2. Confirm the article's first two children are the exact title and the first chapter.
3. Confirm every Markdown chapter, timestamp block, code block, reference, and local image is present in order.
4. Confirm every image loads, has intrinsic dimensions, and appears as its own figure; confirm there are no screenshot tables.
5. Inspect the page at ordinary desktop and phone widths. Check text measure, chapter navigation, image sizing, code overflow, horizontal page overflow, and layout shift.
6. Inspect representative content containing long prose, screenshots, code, and References.
7. For every language-tagged fence, confirm that the exported code contains highlighting spans, remains selectable, and uses a visibly readable font size and line height. Confirm comments, strings, numbers, keywords, and types use distinct colors when those token kinds are present.

## Verify the PDF

1. Confirm the file opens, has a nonzero page count, uses the intended page size, and carries the exact title metadata.
2. Render every page to PNG with Poppler (`pdftoppm`) or an equivalent renderer.
3. Inspect every rendered page for missing images, blank pages, clipping, overlap, unreadable code, broken glyphs, and poor section transitions.
4. Confirm every instructional asset from the HTML article appears legibly.
5. Inspect every code-bearing page at normal viewing size. Reject code smaller than `8.5pt`, lost indentation, syntax colors with poor contrast, clipped long lines, and sparse pages caused by an oversized unsplittable code block.

## Verify the EPUB

1. Run `epubcheck` when available and resolve every error; record its absence when unavailable.
2. Run archive integrity and XML validity checks.
3. Confirm the package manifest contains every local asset referenced by the HTML.
4. Confirm navigation and reading-order spine entries reach every chapter chronologically.
5. Inspect representative prose, screenshots, code, links, and References at narrow and ordinary reader widths.
6. Confirm the metadata title exactly matches the resource title.
7. Confirm syntax spans and their local CSS are present in the package, code remains selectable, and the e-reader layout does not reduce code below the surrounding readable scale.

## Bind exports to the review

After all three editions pass, write the HTML, PDF, and EPUB SHA-256 entries to `final-review-exports.sha256` using technical-note-relative filenames in stable lexical order. Verify every entry from the technical-notes directory. Any Markdown, publication-asset, or HTML content change requires all affected editions to be regenerated and rechecked before the second-pass review can pass.
