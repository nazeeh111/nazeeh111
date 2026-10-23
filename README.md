# A mesh, a pixel, a signal

I'm Nazeeh. I build systems software, geometry tools, and scientific workbenches. I like getting close to the details: the instructions behind a pixel, the topology behind a mesh failure, the assumption behind a radio fit.

**Open a working example:** [Inspect the missing-body case](https://nazeeh111.github.io/Solidrift/) · [Open the native image workbench](https://nazeeh111.github.io/Capsulith/studio/image.html) · [Investigate a passing counterfeit](https://nazeeh111.github.io/Caustryn/demo/?case=exact-counterfeit) · [Open PhysicsBench](https://nazeeh111.github.io/PhysicsBench/)

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/workbench-sensing-mobile-dark.png">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/workbench-sensing-mobile-light.png">
  <source media="(prefers-color-scheme: dark)" srcset="assets/workbench-sensing-dark.png">
  <img src="assets/workbench-sensing-light.png" alt="Three separate projects: Solidrift's original two-solid inputs and recorded FLOAT output with one body absent; its 132-to-12-triangle reduction is described, not pictured. Capsulith's prepared image crop marks source pixel 64,48 with RGBA 126,135,250,255. Caustryn's recorded synthetic radio fit passes two held poses but sits 3.488 metres from the generator's point in 3D. The X/Y plot and numeric 3D separation are distinct; stable response remains a trusted assumption." width="1000">
</picture>

*Three separate projects: a recorded geometry failure, prepared image bytes, and a synthetic radio fit that passes while missing its target. [Image sources](assets/workbench-provenance.md).*

## Inside the projects

- **Geometry · [Solidrift](https://github.com/nazeeh111/Solidrift):** reduce a recorded Blender failure from 132 to 12 triangles while keeping both inputs valid. Inspect mesh ancestry, repair and undo. New native runs use local Blender.
- **Systems · [Capsulith](https://github.com/nazeeh111/Capsulith):** run an original compiled image codec in your browser, inspect its returned pixels, and reopen initialized memory in a fresh worker.
- **Radio · [Caustryn](https://nazeeh111.github.io/Caustryn/demo/?case=exact-counterfeit):** a synthetic fit passes two held positions while missing the generator's point by 3.488 m. Inspect what the check proves and what it assumes.

Also explore:

- **Physics · [PhysicsBench](https://github.com/nazeeh111/PhysicsBench):** test acoustic models against a separate probe, infer motion from image observations, and reopen records that recompute their results. [Open the live lab](https://nazeeh111.github.io/PhysicsBench/).
- **Motion · [Kinetyl](https://nazeeh111.github.io/Kinetyl/):** inspect a label collision at 3.00 s, compile the layout, and compare the repaired trajectory.
- **Numerical computing · [Certloom](https://github.com/nazeeh111/Certloom):** check linear-equation error bounds independently of the original solver.
- **CAD · [SolidFrame](https://nazeeh111.github.io/SolidFrame/):** edit plates and brackets in a browser, then export STEP and STL.

[Browse the project index →](https://nazeeh111.github.io/)

## Work accepted elsewhere

My [Pattern Projector viewport fix](https://github.com/Pattern-Projector/pattern-projector/pull/431) was merged across zoom, pan, rotation, reflection, and calibration; projection hardware was not tested. GitHub credited me as Analyst on an [advisory correction](https://github.com/github/advisory-database/pull/9912) to Django's package and affected-version mapping ([GHSA-wvqv-fj8w-qmhm](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm)).
