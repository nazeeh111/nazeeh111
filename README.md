# A mesh, a pixel, a math step

I'm Nazeeh. I build systems software, geometry tools, and scientific workbenches. I like getting close to the details: the instructions behind a pixel, the topology behind a mesh failure, the step that changed a math answer.

**Open a working example:** [Inspect the missing-body case](https://nazeeh111.github.io/Solidrift/) · [Open the native image workbench](https://nazeeh111.github.io/Capsulith/studio/image.html) · [Check a math step](https://nazeeh111.github.io/Syllune/)

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/workbench-mobile-dark.png">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/workbench-mobile-light.png">
  <source media="(prefers-color-scheme: dark)" srcset="assets/workbench-dark.png">
  <img src="assets/workbench-light.png" alt="Three separate projects: Solidrift's original two-solid inputs and recorded FLOAT output with one body absent; its 132-to-12-triangle reduction is described, not pictured. Capsulith's prepared image crop marks source pixel 64,48 with RGBA 126,135,250,255. Syllune's typed checker flags 2x=20 after 2x+6=14, explains the changed solution set, and blocks x=10 until that earlier step is reviewed." width="1000">
</picture>

*Three separate projects: a recorded geometry failure, prepared image bytes, and an actual typed-step check. [Image sources](assets/workbench-provenance.md).*

## Inside the projects

- **Geometry · [Solidrift](https://github.com/nazeeh111/Solidrift):** reduce a recorded Blender failure from 132 to 12 triangles while keeping both inputs valid. Inspect mesh ancestry, repair and undo. New native runs use local Blender.
- **Systems · [Capsulith](https://github.com/nazeeh111/Capsulith):** run an original compiled image codec in your browser, inspect its returned pixels, and reopen initialized memory in a fresh worker.
- **Math learning · [Syllune](https://github.com/nazeeh111/Syllune):** find an incorrect typed step and practice from the first error. Ink stays editable; optional recognition runs through a local Mac companion.

Also explore:

- **Radio · [Caustryn](https://nazeeh111.github.io/Caustryn/demo/?case=exact-counterfeit):** a synthetic fit passes while missing the generator's point by 3.488 m.
- **Numerical computing · [Certloom](https://github.com/nazeeh111/Certloom):** check linear-equation error bounds independently of the original solver.
- **CAD · [SolidFrame](https://nazeeh111.github.io/SolidFrame/):** edit plates and brackets in a browser, then export STEP and STL.

[Browse the full project index →](https://nazeeh111.github.io/)

## Work accepted elsewhere

My [Pattern Projector viewport fix](https://github.com/Pattern-Projector/pattern-projector/pull/431) was merged across zoom, pan, rotation, reflection, and calibration; projection hardware was not tested. GitHub credited me as Analyst on an [advisory correction](https://github.com/github/advisory-database/pull/9912) to Django's package and affected-version mapping ([GHSA-wvqv-fj8w-qmhm](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm)).
