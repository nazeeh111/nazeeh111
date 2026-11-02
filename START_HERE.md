# Selected work: a two-minute tour

Start with a recorded geometry failure, compiled image code, or a reconstruction from published measurements. Each path below connects an example to its implementation and evidence. Source links point to fixed revisions; hosted examples can change independently.

For a two-minute visit, open the Solidrift recorded case, then its evidence. Choose another section for a deeper inspection.

## Geometry and debugging: Solidrift

On upstream Manifold regression inputs, a Blender Boolean union drops a region of one input. Solidrift reduces the recorded failure from 132 triangles to a 12-triangle witness, then traces an intervention back to the original geometry.

[Explore the recorded case](https://nazeeh111.github.io/Solidrift/) · [Reducer source](https://github.com/nazeeh111/Solidrift/blob/1902168d1c6d64a448434e78dfe5ad840360093a/solidrift/reducer.py) · [Native evidence and controls](https://github.com/nazeeh111/Solidrift/blob/1902168d1c6d64a448434e78dfe5ad840360093a/docs/EVIDENCE.md)

**Limit:** The viewer replays stored results; the greedy search covers one declared failure family and does not guarantee a smallest witness.

## Native code and state: Capsulith

Run a prepared QOI image codec from its compiled ARM64 instructions and inspect the returned pixels. Separately, the LZ4 example restores an initialized object in a fresh worker and compares continued output with an independent native oracle. Both use existing codecs with explicit calling contracts.

[Try the image workbench](https://nazeeh111.github.io/Capsulith/studio/image.html) · [Object runtime](https://github.com/nazeeh111/Capsulith/blob/01f987cf4234872ca7a9cb98fd6ee020632f9863/runtime/object-core.js) · [LZ4 example and comparisons](https://github.com/nazeeh111/Capsulith/blob/01f987cf4234872ca7a9cb98fd6ee020632f9863/examples/native-objects/README.md)

**Limit:** The examples do not establish equivalence for arbitrary binaries or security isolation.

## Stateful code: Rewynth

Inspect a deliberately dropped memory write: an immediate return can still match while the post-state differs. Each subsequent call uses that model's resulting memory state.

[Try the state lesson](https://nazeeh111.github.io/Rewynth/lesson/) · [Lesson runtime](https://github.com/nazeeh111/Rewynth/blob/e9f4261b9ffda97186fa1ced4cbcfc6a78516189/docs/lesson/model-runtime.mjs) · [Scope and independent controls](https://github.com/nazeeh111/Rewynth/blob/e9f4261b9ffda97186fa1ced4cbcfc6a78516189/docs/lesson/README.md)

**Limit:** ARM64 recovery and fresh solver queries run locally; the browser executes the exported C models in WebAssembly.

## SQLite migrations: Keepstep

Inspect a recorded migration that leaves an update successful while search stops finding the updated article. Repaired and unchanged controls retain the search hit.

[Inspect the recorded reports](https://nazeeh111.github.io/SchemaRehearsal/) · [Workload engine](https://github.com/nazeeh111/SchemaRehearsal/blob/ec5fb93152744216781e65da13a68850a05ba72e/src/schema_rehearsal/engine.py) · [Method and reproduction](https://github.com/nazeeh111/SchemaRehearsal/blob/ec5fb93152744216781e65da13a68850a05ba72e/docs/full-text-search.md)

**Limit:** Only declared workloads are compared; the general database checks omit full FTS5 index/content consistency.

## Imaging research: EchoSight

Explore a reconstruction from published measured ultrasound data. The code adapts the released Figure 2 method and retains the source and output provenance.

[Explore the measured case](https://nazeeh111.github.io/EchoSight/) · [Reconstruction source](https://github.com/nazeeh111/EchoSight/blob/ce64ed79869ba0af86f9b9ecb560fc6d4ade4aa5/echosight/nlos.py) · [Method and evidence](https://github.com/nazeeh111/EchoSight/blob/ce64ed79869ba0af86f9b9ecb560fc6d4ade4aa5/docs/MEASURED_NLOS.md)

**Limit:** This is an attributed port of an external measurement; absolute depth calibration remains unresolved.

## Browser automation: ReplaySmith

Record a browser workflow, inspect how targets are resolved, and check its outcome. Its controlled benchmark distinguishes correct completion, wrong actions, abstention and timeout.

[Studio screenshot](https://github.com/nazeeh111/ReplaySmith/blob/62e3593f3bd06ba479029b4f63ea3185afda72bd/demo/launch-v1/captures-v2/03-verified.png) · [Target recovery source](https://github.com/nazeeh111/ReplaySmith/blob/62e3593f3bd06ba479029b4f63ea3185afda72bd/src/recovery.ts) · [Benchmark protocol and results](https://github.com/nazeeh111/ReplaySmith/blob/62e3593f3bd06ba479029b4f63ea3185afda72bd/docs/benchmarks.md)

**Limit:** The benchmark uses a small synthetic fixture suite built alongside the implementation.

## Exact computation: LadderProof

Find whether resistor variation can produce a decreasing step in an ideal digital-to-analog converter, then independently recompute the exported result.

[Workbench screenshot](https://github.com/nazeeh111/LadderProof/blob/89d7b9c082a4fdd9195d0e60503ff3f40c4dfded/docs/workbench.jpg) · [Independent verifier](https://github.com/nazeeh111/LadderProof/blob/89d7b9c082a4fdd9195d0e60503ff3f40c4dfded/src/ladderproof/verifier.py) · [Model and assumptions](https://github.com/nazeeh111/LadderProof/blob/89d7b9c082a4fdd9195d0e60503ff3f40c4dfded/docs/model.md)

**Limit:** The certificate describes a bounded ideal circuit model and independent resistor intervals, not measured hardware behavior.

[All projects](https://nazeeh111.github.io/) · [GitHub profile](https://github.com/nazeeh111)
