# Web Platform Guidance

Apply this guidance to responsive web applications and desktop web interfaces.

## Preserve the project system

Inspect the existing component library, design tokens, layout primitives, breakpoints, interaction conventions, and accessibility approach before adding styles. Prefer established primitives over page-local CSS.

Do not default to generic dashboard cards, excessive gradients, decorative pills, or “modern SaaS” conventions when the project visual language does not call for them.

## Responsive structure

Verify:

- intended content hierarchy at narrow, medium, and wide viewports;
- navigation changes across breakpoints;
- readable line length and content density;
- overflow, wrapping, sticky regions, and scroll ownership;
- touch and pointer interaction;
- loading, empty, error, offline, and slow-network behavior.

Use responsive changes to preserve hierarchy, not merely shrink dimensions.

## Interaction and accessibility

Prefer semantic HTML and existing accessible primitives. Verify:

- keyboard order and visible focus;
- hover, focus, active, selected, and disabled states;
- landmark and heading structure;
- form labels, errors, and recovery;
- reduced motion and contrast preferences;
- zoom and reflow;
- screen-reader names and state announcements.

Do not make essential actions hover-only.

## Reference adaptation

Production web references may be structurally close, but still adapt:

- typography and spacing to the project's tokens;
- component density to the product context;
- navigation to the project's information architecture;
- motion to performance and accessibility constraints;
- branded or proprietary assets to project-owned equivalents.

## Verification

Capture browser screenshots at explicit representative viewport sizes. Inspect the live DOM for clipping, overflow, focus, and responsive behavior. Include at least one narrow viewport and one common desktop viewport when the surface is responsive.
