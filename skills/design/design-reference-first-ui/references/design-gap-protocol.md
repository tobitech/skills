# Design Gap Protocol

A design gap exists when a reusable visual or interaction decision lacks an approved project precedent, or when existing guidance conflicts.

Assess gaps per decision rather than per screen. Reusing a screen's split-view structure does not automatically resolve row typography, density, icon color, card hierarchy, or toolbar placement.

Inspect the full set of recurring visual decisions before sending the notice. Combine closely related issues under a broader gap such as “workspace catalog row pattern,” but list distinct gaps separately when their eventual system homes differ.

## Change ownership before implementation

Classify a requested visual change before editing the nearest view:

| Ownership | Use when | Action |
|---|---|---|
| Foundation token or rule | The request changes the default meaning or presentation of a semantic role across the product | Update the foundation, inspect its consumers, and render representative affected screens |
| Shared component | The request changes anatomy, behavior, or styling owned by an existing reusable component | Change the component and review its variants, states, and call sites |
| Contextual semantic role or component variant | A recurring context legitimately differs without redefining the global role | Add or evolve a named reusable role or variant and document its scope |
| Local composition choice | The decision is content-specific, optical, or unique to one composition | Keep it local, use existing tokens, and do not present it as global precedent |

Treat words such as “base,” “default,” “everywhere,” “app-wide,” or a named semantic role as evidence for a foundation change. Treat “this screen,” “this card,” or “only here” as evidence for a scoped choice. An explicit request to modify a design-system component normally authorizes its shared effect, but still requires consumer review.

When wording is ambiguous:

1. Inspect the current owner and call sites.
2. Determine whether the same semantic role should remain consistent elsewhere.
3. Check whether the local request exposes a design-system bypass or missing reusable role.
4. Prefer a named semantic role or component variant over repeated raw overrides.
5. Ask the user only when local and shared interpretations remain plausible and the shared blast radius is meaningful.

For example, if a project defines a semantic body style and the user asks for one body instance to be smaller, determine whether that text is actually a different semantic role. Use or add a named scoped role when it is; change the body foundation only when the request is truly app-wide. Do not create a local raw size while continuing to call it body.

## Classification

### Local implementation choice

Examples include an optical offset, line limit, or content-specific divider inset. Decide autonomously unless the rendered result remains questionable.

### Design-system gap — non-blocking

Examples include:

- missing row density or typography roles;
- no semantic icon-color policy;
- conflicting sibling component alignment;
- no established placement for a recurring control;
- a repeated need for an arbitrary raw value;
- a new pattern likely to recur across features.
- a framework default used because no project role is documented;
- an isolated implementation being treated as precedent without reviewed visual evidence.

Notify the user and continue with a reversible provisional decision.

### Product design decision — potentially blocking

Examples include:

- list-detail navigation versus a modal workflow;
- inline editing versus a dedicated editor;
- moving a preference between feature scope and global settings;
- alternatives that materially change the user journey, data model, or feature scope.

Pause only when a safe assumption would likely cause meaningful rework or diverge from the user's intent.

## Non-blocking notice

Use concise commentary:

> **Design gap — non-blocking: [pattern]**  
> [What is missing or conflicting, and what evidence was inspected.]  
> **Provisional direction:** [Reference-backed choice.] I’ll continue with this direction and propose [token/component/pattern/documentation] after visual review.

Do not ask the user to approve the notice before continuing.

## Provisional implementation

- Prefer a reversible, narrowly scoped choice.
- Reuse the closest semantic token or component when it remains truthful.
- Do not silently declare the choice a global standard.
- Avoid adding duplicated local workarounds when an approved shared abstraction already exists.
- If a shared API must change for the feature to work cleanly, report that scope explicitly.

## Closure lifecycle

1. Identify the missing pattern.
2. Gather internal and production evidence.
3. Implement and render a provisional choice.
4. Review with the user when appropriate.
5. Approve, revise, or reject the direction.
6. Document the final rule.
7. Promote it into a semantic token, component, pattern, or golden screen.
8. Reconcile conflicting implementations within authorized scope.

Keep unresolved gaps visible in the final handoff. Use the project's existing decision-log convention when one exists.
