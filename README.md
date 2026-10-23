# What did the result leave out?

A Blender Boolean can silently lose a whole input and still produce a mesh. A saved program can take a different path after one return changes. A radio fit can pass its own check and still be far from synthetic truth. I build tools to open these results and find out why. I also make places to design and learn.

[Open the project index](https://nazeeh111.github.io/) · [Browse the repositories](https://github.com/nazeeh111?tab=repositories)

## The missing body

**132 triangles → a 12-triangle witness.** [Explore the Solidrift case](https://nazeeh111.github.io/Solidrift/) · [Watch the 19-second tour](https://nazeeh111.github.io/Solidrift/tour.html)

<a href="https://nazeeh111.github.io/Solidrift/"><img src="assets/solidrift-evidence-v2.png" alt="Solidrift's recorded Blender Boolean case: original meshes on the left; FLOAT output on the right omits one input. The source failure was reduced from 132 triangles to a 12-triangle witness." width="960"></a>

Step through the accepted reductions, trace the witness back to the full model, test an input repair, and undo it. The meshes and Boolean outputs come from a recorded native run; the browser lets you inspect them. [Source and limits](https://github.com/nazeeh111/Solidrift).

## Two more cases to open

- **A changed program path.** [Aetiory](https://nazeeh111.github.io/Aetiory/) compares what followed two returns in a retained Python failure. The browser case is recorded; live forking runs locally. [Source](https://github.com/nazeeh111/Aetiory).
- **A plausible answer that is wrong.** [Caustryn](https://nazeeh111.github.io/Caustryn/demo/?case=exact-counterfeit) lets you reveal why a held-position check passes at a point 3.488 m from synthetic truth. This is a counterexample to a test, not a real-world accuracy measurement. [Source](https://github.com/nazeeh111/Caustryn).

## I also make

- [SolidFrame](https://nazeeh111.github.io/SolidFrame/): design an editable plate or bracket in browser CAD, then export a STEP or STL file. Built on Chili3D. [Source](https://github.com/nazeeh111/SolidFrame).
- [Syllune](https://nazeeh111.github.io/Syllune/): work through a math problem with ink, step checks, and targeted practice in a private studio. [Source](https://github.com/nazeeh111/Syllune).

The [project index](https://nazeeh111.github.io/) has the rest of the browser experiments and local tools.

## Work accepted elsewhere

- [Pattern Projector #431](https://github.com/Pattern-Projector/pattern-projector/pull/431): merged viewport-outline fix across zoom, pan, rotation, reflection, and calibration. Projection hardware was not tested.
- [GitHub advisory GHSA-wvqv-fj8w-qmhm](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm): credited as Analyst for correcting the Django package and affected-version mapping. [Accepted change](https://github.com/github/advisory-database/pull/9912).
