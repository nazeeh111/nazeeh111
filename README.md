# Nazeeh Abdul-Hadi

I build local software for mechanical design, circuit analysis, scheduling, text annotations and database checks. I also work on graphics and sensing experiments.

[Open SolidFrame CAD](https://nazeeh111.github.io/SolidFrame/) · [Open Muster](https://nazeeh111.github.io/Muster/) · [Try a migration rehearsal](https://github.com/nazeeh111/SchemaRehearsal#try-a-migration-that-loses-an-audit-trail) · [Inspect an AgentLedger run](https://nazeeh111.github.io/AgentLedger/)

## Featured original projects

**[Muster](https://github.com/nazeeh111/Muster)** repairs volunteer schedules while preserving locked commitments. It prioritizes coverage, then fewer changes, and explains staffing shortages; timed results state when optimality is unproven. [Open the worksheet](https://nazeeh111.github.io/Muster/).

**[Camwright](https://github.com/nazeeh111/Camwright)** designs in-line roller cams from an editable motion cycle. Geometry checks return Pass, Fail or Unresolved, with saved inputs and inspection evidence. [Run Camwright locally](https://github.com/nazeeh111/Camwright#run-locally).

**[Sley](https://github.com/nazeeh111/Sley)** adapts supported rising-shed weaving drafts to declared physical pedals and allowed pairs, preserving thread structure, colors and fixed tie-ups. It reports Feasible, Infeasible or Unknown and exports the draft and pedal instructions. [Run Sley locally](https://github.com/nazeeh111/Sley#run-locally).

**[Signelet](https://github.com/nazeeh111/Signelet)** transfers text annotations only when every minimum-cost character alignment agrees on an unchanged span under its alignment model. Ambiguous originals remain available for review. [Try the repeated-word example](https://github.com/nazeeh111/Signelet#try-the-example).

**[SchemaRehearsal](https://github.com/nazeeh111/SchemaRehearsal)** replays declared application scenarios on isolated before-and-after SQLite copies. Its example detects a lost payment-audit trigger despite preserved rows and passing integrity checks. [Rehearse the migration](https://github.com/nazeeh111/SchemaRehearsal#try-a-migration-that-loses-an-audit-trail).

**[AgentLedger](https://github.com/nazeeh111/AgentLedger)** runs bounded local task graphs, verifies artifacts and records command results. Durable checkpoints resume verified command tasks after interruption; Codex review is optional. [Run the offline example](https://github.com/nazeeh111/AgentLedger#run-the-complete-offline-example).

**[PhysicsBench](https://github.com/nazeeh111/PhysicsBench)** explores ideal projectile motion, mass–spring oscillation and one-dimensional collisions with time scrubbing, conservation checks and portable model sessions. Units and assumptions stay visible. [Open the physics lab](https://nazeeh111.github.io/PhysicsBench/).

<details>
<summary>More projects and experiments</summary>

**[LadderProof](https://github.com/nazeeh111/LadderProof)** computes exact voltage-step bounds for ideal 2–6-bit resistor ladders with independent component intervals. Inspect a decreasing transition and compare a tighter design with complete independent verification. [Run the circuit example](https://github.com/nazeeh111/LadderProof#try-the-complete-workflow).

**[Reticle](https://github.com/nazeeh111/Reticle)** checks microscopy exports for changed, missing or unit-equivalent physical calibration and supported image-plane mappings. [Compare synthetic TIFFs](https://github.com/nazeeh111/Reticle#run).

**[DurableStore](https://github.com/nazeeh111/DurableStore)** is Rust key-value storage with atomic batches, checksummed recovery, exclusive locks and compaction. Process-crash tests and an outbox example are included; power-loss behavior depends on filesystem and hardware. [Source release](https://github.com/nazeeh111/DurableStore/releases/tag/v0.2.0).

**Developer tools:** [PolicyDelta](https://github.com/nazeeh111/PolicyDelta) compares OpenBao policies using identical requests and synthetic fixtures. [VaultLens](https://github.com/nazeeh111/VaultLens) audits password exports offline with redacted output.

**Scientific software:** [ModelForge](https://github.com/nazeeh111/ModelForge) implements numerical modeling in Rust; [SequenceForge](https://github.com/nazeeh111/SequenceForge) covers sequence alignment and phylogenetics; [MoleculeBench](https://github.com/nazeeh111/MoleculeBench) compares molecular bond models against numerical references.

**Research software and sensing experiments:** [HiddenWave](https://github.com/nazeeh111/HiddenWave), [CornerVision](https://github.com/nazeeh111/CornerVision) and [ApertureTrace](https://github.com/nazeeh111/ApertureTrace) explore hidden-scene reconstruction. [RadarVolume](https://github.com/nazeeh111/RadarVolume) and [SoundMap](https://github.com/nazeeh111/SoundMap) connect array geometry and recorded signals to spatial results. [ChirpMotion](https://github.com/nazeeh111/ChirpMotion) adds a portable C17 analyzer that streams recorded chirps without MATLAB. [Build its generated demo](https://github.com/nazeeh111/ChirpMotion#native-analysis-no-matlab-required). Some sensing projects still need specialized hardware or datasets for real-world evaluation.

**Data applications:** [MarketObservatory](https://github.com/nazeeh111/MarketObservatory) compares CSV price series and portfolio allocations with HTML, JSON and CSV exports. [MarketWeave](https://github.com/nazeeh111/MarketWeave) provides prediction-market data and order-book interfaces.

</details>

## Graphics, sensing and developer tools

| Project | Open it | Contribution |
| :--- | :--- | :--- |
| **[SolidFrame](https://github.com/nazeeh111/SolidFrame)** | [Browser CAD](https://nazeeh111.github.io/SolidFrame/) | Adds an editable mechanical part builder for drilled plates and brackets, hole-pattern validation, and a reorganized keyboard-accessible workspace, alongside the fixture and local-project safeguards. |
| **[LumaField](https://github.com/nazeeh111/LumaField)** | [Browser viewer](https://nazeeh111.github.io/LumaField/) | Adds local `.splat` and binary `.ply` loading, camera import, conversions, and an original procedural scene. |
| **[PhotonRelay](https://github.com/nazeeh111/PhotonRelay)** | [Browser app](https://nazeeh111.github.io/PhotonRelay/) | Adds a phone setup link and a channel lab for testing frame loss and duplication. |
| **[EchoAtlas](https://github.com/nazeeh111/EchoAtlas)** | [macOS download](https://github.com/nazeeh111/EchoAtlas/releases/latest) | Experimental acoustic gesture controls with calibration, stale-audio rejection, explicit stop controls, and analyzer replay. Live-hand accuracy still needs testing. |
| **[MotionizedAudio](https://github.com/nazeeh111/MotionizedAudio)** | [Known-motion experiment](https://github.com/nazeeh111/MotionizedAudio/blob/main/experiments/known_motion.py) | Adds a generated known-motion experiment, frequency and timing checks, and safer WAV output handling; real-speech recovery is unverified. |

**[ToolScope](https://github.com/nazeeh111/ToolScope)** provides browser, CLI and terminal inspection plus offline comparison of exported tool definitions. [Try the offline example](https://github.com/nazeeh111/ToolScope#cli-and-terminal-interface).

**[WorkHarbor](https://github.com/nazeeh111/WorkHarbor)** provides a local task/run workspace with an isolated launcher and selected-file review packets. [Download the source](https://github.com/nazeeh111/WorkHarbor/releases/tag/v0.1.1). Board workflows, responsive draft retention, rejected-save recovery and mocked run lifecycles are tested; real provider execution remains unvalidated.

Source notes: SolidFrame uses Chili3D; LumaField uses antimatter15/splat; PhotonRelay uses Decimen Optical Transfer; ToolScope uses MCP Inspector; WorkHarbor uses Paperclip; MotionizedAudio continues the earlier VisualMic code. Each repository retains detailed credits and terms.

## Runnable SQLite examples

Two small, dependency-free examples behind my database tooling:

- [A table rebuild that loses a payment audit](https://gist.github.com/nazeeh111/4714ddbec0b1df2edc78c8a1ed64000f): identical rows and a passing integrity check, but a missing trigger changes behavior.
- [A main-file copy that misses committed WAL data](https://gist.github.com/nazeeh111/8e06fcc6bca04f5131e464815d2c26ac): compare file copying with SQLite's backup snapshot.

## Upstream contribution

Corrected Django package and affected-version mapping in an existing GitHub security advisory. The [published advisory](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm) credits me as **Analyst**. [Accepted change](https://github.com/github/advisory-database/pull/9912).

See each repository's verification notes for its tested scope.

**Publication note:** Projects are published in batches from local Git workspaces. GitHub upload dates are publication dates, not a development timeline.
