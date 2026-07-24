# Apple Platform Guidance

Apply this guidance to iOS, iPadOS, and macOS work. Use current Apple documentation for APIs or conventions that may have changed.

## Shared principle

Use native behavior and project presentation.

Preserve platform semantics for navigation, focus, selection, accessibility, menus, text input, safe areas, windowing, and system settings. Do not accept an unsuitable default tint, density, typography, or surface merely because it is native.

Prefer SwiftUI and modern platform APIs when they satisfy the required behavior. Use AppKit or UIKit bridges when native behavior cannot otherwise be achieved cleanly.

## iOS and iPadOS

Verify:

- navigation stack, tab, sheet, popover, and inspector choices;
- safe areas, keyboard avoidance, and orientation;
- compact and regular size classes;
- touch-target size and gesture discoverability;
- Dynamic Type, VoiceOver order, contrast, and Reduce Motion;
- destructive-action confirmation and interruption recovery;
- loading, offline, empty, and permission states.

Use SF Symbols semantically unless a project-approved asset or recognizable provider mark is better. Treat tint as a role, not a default decoration.

Render representative devices and at least one larger text setting when layout risk is meaningful.

## macOS

Verify:

- window resizing and minimum useful dimensions;
- split-view, sidebar, table, list, inspector, sheet, popover, and toolbar semantics;
- keyboard navigation, focus rings, menus, context menus, and command shortcuts;
- hover and keyboard-focus parity;
- pointer precision and compact controls without sacrificing legibility;
- titlebar and toolbar placement;
- light and dark window surfaces.

Treat toolbars primarily as homes for commands, navigation, search, view controls, and menus. Place persistent labeled preferences in content or Settings unless the project has an approved exception.

Native `List` and sidebar styles may introduce accent icons, compact row metrics, or typography that conflicts with the project. Explicitly style semantic row presentation when needed while preserving native selection and accessibility behavior.

## Verification

Use SwiftUI previews for deterministic states and simulator, device, or real-window screenshots for final visual evidence. A preview should include representative content rather than placeholder-only geometry.
