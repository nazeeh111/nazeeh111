<a id="nazeeh-abdul-hadi"></a>

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/profile-v3/cover-mobile-dark.png">
  <source media="(max-width: 600px)" srcset="assets/profile-v3/cover-mobile-light.png">
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile-v3/cover-wide-dark.png">
  <img src="assets/profile-v3/cover-wide-light.png" width="1000" alt="Nazeeh Abdul-Hadi. Electrical engineering and physics at Virginia Tech.">
</picture>

I study electrical engineering and physics at Virginia Tech. I build tools for models, circuits and scientific computing.

**[Portfolio](https://nazeeh111.github.io/) · [Research](https://nazeeh111.github.io/research/) · [Engineering tour](START_HERE.md)**

<a id="find-your-field"></a>
## Selected work

### PhotonSmith

Design periodic photonic gratings and inspect the Maxwell field, spectrum and numerical cross-checks.

[Source and local setup](https://github.com/nazeeh111/PhotonSmith) · [Worked numerical design](https://github.com/nazeeh111/PhotonSmith/blob/a3ecad3af5f0bb957334f58f73379c886463aa42/docs/presentation/README.md)

<picture>
  <source media="(max-width: 600px)" srcset="assets/profile-v3/photonsmith-mobile.png">
  <img src="assets/profile-v3/photonsmith.png" width="1000" alt="PhotonSmith's retained 1550-nanometre numerical design: real electric field across one periodic cell and target-order efficiency across stored wavelengths. Axes, units and field color scale are retained.">
</picture>

Stored Maxwell simulation, not a fabricated-device measurement. [Figure source and terms](assets/profile-v3/PROVENANCE.md).

### SiliconPilot

Compile a small neural classifier into Verilog. Fixed-point RTL, simulation and synthesis.

[Source](https://github.com/nazeeh111/SILICONPILOT) · [Recorded circuits](https://nazeeh111.github.io/SILICONPILOT/)

### MaterialMind

Explore crystal-stability predictions and their uncertainty. Retrospective models against archived DFT.

[Source](https://github.com/nazeeh111/MaterialMind) · [Worked crystal example](https://github.com/nazeeh111/MaterialMind/blob/c879afa4b616649cac73ef46b010f24e12ed3544/docs/presentation/README.md)

### MorphProof

Translate supported numerical Python to Rust and reduce disagreements. Finite behavioral checks and reduced counterexamples.

[Compiler and Studio](https://github.com/nazeeh111/MorphProof)

### LadderProof

Bound resistor tolerances in ideal ladder DACs. Ideal static circuits with independent verification.

[Circuit workbench and source](https://github.com/nazeeh111/LadderProof)

<a id="research-you-can-inspect"></a>
## Research

[Two-copy quantum measurements](https://nazeeh111.github.io/research/phaseglass-quantum/): an exact result for a specified state family, plus separate finite-shot simulations.

[More research](https://nazeeh111.github.io/research/) in physical models, numerical methods and learning systems, with methods, sources and limits.

<a id="contributions-accepted-upstream"></a>
## Upstream contributions

- [PyVista](https://github.com/pyvista/pyvista/pull/9457): closed periodic seams in `ParametricKlein`.
- [Pattern Projector](https://github.com/Pattern-Projector/pattern-projector/pull/431): corrected viewport outlines under panning and projective transforms. Projection hardware was not tested.
- [GitHub advisory database](https://github.com/github/advisory-database/pull/9912): corrected Django package and affected-version mapping. [Advisory and credit](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm).

[Look closer at the engineering](START_HERE.md) for fixed-revision source links, reproduction paths and the boundaries of each result.

<details>
<summary>More fields and the earlier geometry case</summary>

**Geometry you can work with**  
[SolidFrame](https://github.com/nazeeh111/SolidFrame): browser CAD built on Chili3D, with editable mechanical parts and STEP/STL export. [Open CAD](https://nazeeh111.github.io/SolidFrame/).

**Physics made inspectable**  
[EchoSight](https://github.com/nazeeh111/EchoSight): an attributed reconstruction from published ultrasound measurements. [Explore the measured case](https://nazeeh111.github.io/EchoSight/). [QLOOM](https://github.com/nazeeh111/QLOOM): quantum circuit compilation with independent numerical checks.

**Systems with state that matters**  
[Capsulith](https://github.com/nazeeh111/Capsulith): prepared ARM64 image code with preserved pixel allocation. [Run the workbench](https://nazeeh111.github.io/Capsulith/studio/image.html). [Rewynth](https://github.com/nazeeh111/Rewynth): the memory changes a return value can miss.

**Machine learning and evaluation**\
[MaterialMind](https://github.com/nazeeh111/MaterialMind): crystal-stability models, active-learning decisions and native sessions with explicit uncertainty checks. [QubitGuard](https://github.com/nazeeh111/QubitGuard): compare learned and matching decoders through saved correction outcomes.

**Circuits with exact bounds**\
[LadderProof](https://github.com/nazeeh111/LadderProof): exact tolerance bounds for ideal resistor-ladder DACs.

**Tools for doing the work**  
[nstack](https://github.com/nazeeh111/nstack): reviewed specialist tools in a native Mac coding setup.


## The union that lost a solid

**Solidrift reduces a recorded Blender failure from 132 triangles to 12**, preserving the missing-body defect at every accepted step.

<a href="https://nazeeh111.github.io/Solidrift/">
<picture>
  <source media="(max-width: 600px)" srcset="assets/solidrift-comparison-mobile.svg">
  <img src="assets/solidrift-comparison.svg" alt="Solidrift's original recorded case: two overlapping mesh solids are input; one body is absent from Blender's returned union. The later reduction reaches a 12-triangle witness." width="1000">
</picture>
</a>

[Follow the reduction](https://nazeeh111.github.io/Solidrift/) | [Inspect the code and evidence](https://github.com/nazeeh111/Solidrift)

The figure shows the original 132-triangle case, not the reduced witness. [Figure source and fixture credits](assets/solidrift-comparison-provenance.md).


</details>

<details>
<summary>Profile source and checks</summary>

Run `python3 scripts/check_profile.py` from any working directory, using the script's full path when outside this checkout. It checks local inline Markdown and HTML references, the current image-to-provenance map in `profile-assets.json`, SVG descriptions and fixed-revision GitHub source-link syntax. Inline links support simple labels, balanced or angle-bracketed destinations and quoted or parenthesized titles. Reference-style links, autolinks and Markdown code-block interpretation are outside this small lint rule. It runs offline without dependencies and does not verify remote availability, rendered appearance or the scientific claims. Update the map and the credited provenance note together when replacing a current image. Historical artwork stays in `assets/`.

</details>
