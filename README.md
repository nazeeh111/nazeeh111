# Nazeeh Abdul-Hadi

I build geometry tools, systems software, and scientific computing projects.

[Projects and research](https://nazeeh111.github.io/) · [A closer look at the engineering](START_HERE.md)

<a href="https://nazeeh111.github.io/Solidrift/">
<picture>
  <source media="(max-width: 600px)" srcset="assets/solidrift-comparison-mobile.svg">
  <img src="assets/solidrift-comparison.svg" alt="Solidrift: two input mesh solids beside the recorded Blender union, where one body is missing." width="1000">
</picture>
</a>

**A Blender union dropped a solid.** Solidrift reduces the recorded failure from 132 triangles to 12 while preserving the defect. [Follow the reduction](https://nazeeh111.github.io/Solidrift/) · [Code and evidence](https://github.com/nazeeh111/Solidrift). The figure shows the original case; [source and fixture credits](assets/solidrift-comparison-provenance.md).

## Explore the work

- **[SolidFrame](https://github.com/nazeeh111/SolidFrame)**: browser CAD built on Chili3D, with editable mechanical parts and STEP/STL export. [Open the workspace](https://nazeeh111.github.io/SolidFrame/).
- **[Capsulith](https://github.com/nazeeh111/Capsulith)**: execute compiled ARM64 image code, retain its pixel allocation, and inspect it in a fresh worker. [Run the image workbench](https://nazeeh111.github.io/Capsulith/studio/image.html).
- **[LadderProof](https://github.com/nazeeh111/LadderProof)**: find nonmonotonic steps in ideal resistor-ladder DACs using exact tolerance bounds and replayable counterexamples.
- **[MaterialMind](https://github.com/nazeeh111/MaterialMind)**: explore crystal features, stability models, and retrospective active-learning experiments.
- **[EchoSight](https://github.com/nazeeh111/EchoSight)**: reconstruct published ultrasound measurements with an attributed method port and an interactive volume viewer. [Measured-data case](https://nazeeh111.github.io/EchoSight/).
- **[QLOOM](https://github.com/nazeeh111/QLOOM)**: compile small quantum circuits and inspect independent numerical equivalence checks.
- **[nstack](https://github.com/nazeeh111/nstack)**: find and activate reviewed specialist tools from a native coding setup on a Mac.

## Research

[Quantum measurements, physical models, numerical methods and learning systems](https://nazeeh111.github.io/research/). Each study links its method, results, limits, manuscript and available source.

Start with [two-copy quantum measurements](https://nazeeh111.github.io/research/phaseglass-quantum/): an exact result for states whose whole-block purity statistics match, with a separate finite-shot simulation.

## Accepted contributions

- [PyVista](https://github.com/pyvista/pyvista/pull/9457): closed periodic seams in `ParametricKlein`.
- [Pattern Projector](https://github.com/Pattern-Projector/pattern-projector/pull/431): viewport transforms and calibration fixes. Projection hardware was not tested.
- [GitHub advisory database](https://github.com/github/advisory-database/pull/9912): corrected Django package and affected-version mapping. [Advisory and credit](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm).

<details>
<summary>Maintaining this profile</summary>

Run `python3 scripts/check_profile.py` from any working directory, using the script's full path when outside this checkout. It checks local inline Markdown and HTML references, the current image-to-provenance map in `profile-assets.json`, SVG descriptions and fixed-revision GitHub source-link syntax. Inline links support simple labels, balanced or angle-bracketed destinations and quoted or parenthesized titles. Reference-style links, autolinks and Markdown code-block interpretation are outside this small lint rule. It runs offline without dependencies and does not verify remote availability, rendered appearance or the scientific claims. Update the map and the credited provenance note together when replacing a current image. Historical artwork stays in `assets/`.

</details>
