# A mesh, a pixel, a math step

I'm Nazeeh Abdul-Hadi. These artifacts come from three separate tools I built: one traces a missing body in a recorded Blender result, one runs a prepared ARM64 image routine, and one pairs handwritten math with checks on typed steps. Pick a working example below.

**Open a working example:** [Inspect the missing-body case](https://nazeeh111.github.io/Solidrift/) · [Open the native image workbench](https://nazeeh111.github.io/Capsulith/studio/image.html) · [Check a math step](https://nazeeh111.github.io/Syllune/)

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/workbench-mobile-dark.png">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/workbench-mobile-light.png">
  <source media="(prefers-color-scheme: dark)" srcset="assets/workbench-dark.png">
  <img src="assets/workbench-light.png" alt="Three separate projects: Solidrift's original two-body input and recorded one-body FLOAT output; a pixel crop from Capsulith's prepared image with RGBA 126, 135, 250, 255 at 64,48; and three inked equations from the current Syllune studio. The Solidrift image does not show the later reduced witness. Syllune's hosted checks use typed steps, not handwriting recognition." width="1000">
</picture>

*Three separate projects. Syllune ink is pictured; its hosted step checker uses typed text. [Image sources](assets/workbench-provenance.md).*

## The work behind the objects

- **[Solidrift](https://github.com/nazeeh111/Solidrift)** reduces a recorded Blender Boolean failure from 132 input triangles to a 12-triangle witness while keeping the missing-body behavior. The paired meshes above show the *original* input and FLOAT output; the smaller witness is in the case. The browser inspects recorded native results, with local Blender reproduction available from source.
- **[Capsulith](https://github.com/nazeeh111/Capsulith)** keeps original ARM64 instructions inside a prepared QOI image component. Its workbench encodes, decodes, checks RGBA pixels, and restores an owned native image allocation in a fresh worker. This is a known-source component with declared contracts, not arbitrary application recovery.
- **[Syllune](https://github.com/nazeeh111/Syllune)** is a private math notebook for ink, supported exact step checks, and practice. The ink above is from its current studio. The hosted check reads a typed transcript; optional handwriting recognition needs the local Mac companion.

Elsewhere, [Caustryn](https://nazeeh111.github.io/Caustryn/demo/?case=exact-counterfeit) exposes a synthetic radio-fit check that accepts a wrong point; [Certloom](https://github.com/nazeeh111/Certloom) checks stored linear equations independently of its solver; and [SolidFrame](https://nazeeh111.github.io/SolidFrame/) makes editable browser CAD that exports STEP and STL. [Browse the full project index](https://nazeeh111.github.io/).

## Work accepted elsewhere

My [Pattern Projector viewport fix](https://github.com/Pattern-Projector/pattern-projector/pull/431) was merged across zoom, pan, rotation, reflection, and calibration; projection hardware was not tested. GitHub credited me as Analyst on an [advisory correction](https://github.com/github/advisory-database/pull/9912) to Django's package and affected-version mapping ([GHSA-wvqv-fj8w-qmhm](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm)).
