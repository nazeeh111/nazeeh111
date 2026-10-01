# Nazeeh Abdul-Hadi

Local software for mechanical design, circuit analysis, scheduling, text annotations and database checks. I also work on graphics and sensing experiments.

[Open Muster](https://nazeeh111.github.io/Muster/) · [Try a migration rehearsal](https://github.com/nazeeh111/SchemaRehearsal#try-a-migration-that-loses-an-audit-trail) · [Inspect an AgentLedger run](https://nazeeh111.github.io/AgentLedger/)

## Featured original projects

**[Muster](https://github.com/nazeeh111/Muster)** repairs volunteer schedules while preserving locked commitments. It maximizes coverage, then minimizes changes, and explains staffing shortages. [Open the worksheet](https://nazeeh111.github.io/Muster/).

**[Camwright](https://github.com/nazeeh111/Camwright)** designs in-line roller cams from an editable motion cycle. Geometry checks return Pass, Fail or Unresolved, with saved inputs and inspection evidence. [Run Camwright locally](https://github.com/nazeeh111/Camwright#run-locally).

**[Sley](https://github.com/nazeeh111/Sley)** adapts supported rising-shed weaving drafts to declared physical pedals and allowed pairs, preserving thread structure, colors and fixed tie-ups. It reports Feasible, Infeasible or Unknown and exports the draft and pedal instructions. [Run Sley locally](https://github.com/nazeeh111/Sley#run-locally).

**[Signelet](https://github.com/nazeeh111/Signelet)** transfers text annotations only when every minimum-cost character alignment agrees on an unchanged span. Ambiguous originals remain available for review. [Try the repeated-word example](https://github.com/nazeeh111/Signelet#try-the-example).

**[SchemaRehearsal](https://github.com/nazeeh111/SchemaRehearsal)** replays application scenarios on isolated before-and-after SQLite copies. Its example detects a lost payment-audit trigger despite preserved rows and passing integrity checks. [Rehearse the migration](https://github.com/nazeeh111/SchemaRehearsal#try-a-migration-that-loses-an-audit-trail).

**[AgentLedger](https://github.com/nazeeh111/AgentLedger)** runs bounded local task graphs, verifies artifacts and records command results. Durable checkpoints resume verified command tasks after interruption; Codex review is optional. [Run the offline example](https://github.com/nazeeh111/AgentLedger#run-the-complete-offline-example).

<details>
<summary>More original software and experiments</summary>

**[LadderProof](https://github.com/nazeeh111/LadderProof)** computes exact voltage-step bounds for ideal 2–6-bit resistor ladders with independent component intervals. Inspect a decreasing transition and compare a tighter design with complete independent verification. [Run the circuit example](https://github.com/nazeeh111/LadderProof#try-the-complete-workflow).

**[Reticle](https://github.com/nazeeh111/Reticle)** checks microscopy exports for changed, missing or unit-equivalent physical calibration and supported image-plane mappings. [Compare synthetic TIFFs](https://github.com/nazeeh111/Reticle#run).

**[DurableStore](https://github.com/nazeeh111/DurableStore)** is Rust key-value storage with atomic batches, checksummed recovery, exclusive locks and compaction. Process-crash tests and an outbox example are included; power-loss behavior depends on filesystem and hardware. [Source release](https://github.com/nazeeh111/DurableStore/releases/tag/v0.2.0).

**Developer tools:** [PolicyDelta](https://github.com/nazeeh111/PolicyDelta) compares OpenBao policies using identical requests and synthetic fixtures. [VaultLens](https://github.com/nazeeh111/VaultLens) audits password exports offline with redacted output.

**Scientific software:** [ModelForge](https://github.com/nazeeh111/ModelForge) implements numerical modeling in Rust; [SequenceForge](https://github.com/nazeeh111/SequenceForge) covers sequence alignment and phylogenetics; [MoleculeBench](https://github.com/nazeeh111/MoleculeBench) compares molecular bond models against numerical references.

**Signals and inverse problems:** [HiddenWave](https://github.com/nazeeh111/HiddenWave), [CornerVision](https://github.com/nazeeh111/CornerVision) and [ApertureTrace](https://github.com/nazeeh111/ApertureTrace) explore hidden-scene reconstruction. [RadarVolume](https://github.com/nazeeh111/RadarVolume), [SoundMap](https://github.com/nazeeh111/SoundMap) and [ChirpMotion](https://github.com/nazeeh111/ChirpMotion) connect array geometry and recorded signals to spatial or spectral results. Some sensing projects still need specialized hardware or datasets for real-world evaluation.

**Data applications:** [MarketObservatory](https://github.com/nazeeh111/MarketObservatory) compares CSV price series and portfolio allocations with HTML, JSON and CSV exports. [MarketWeave](https://github.com/nazeeh111/MarketWeave) provides prediction-market data and order-book interfaces.

</details>

## Adaptations and experiments

| Project | Open it | Contribution |
| :--- | :--- | :--- |
| **[SolidFrame](https://github.com/nazeeh111/SolidFrame)** | [Browser CAD](https://nazeeh111.github.io/SolidFrame/) | Adapts Chili3D with an editable fixture, restricted URL plugin loading, separate project storage and save-confirmation fixes. |
| **[LumaField](https://github.com/nazeeh111/LumaField)** | [Browser viewer](https://nazeeh111.github.io/LumaField/) | Gaussian-splat renderer adaptation with local `.splat` and binary `.ply` loading, camera import, conversions, and an original procedural scene. |
| **[PhotonRelay](https://github.com/nazeeh111/PhotonRelay)** | [Browser app](https://nazeeh111.github.io/PhotonRelay/) | Optical-transfer adaptation with a phone setup link and a channel lab for testing frame loss and duplication. |
| **[EchoAtlas](https://github.com/nazeeh111/EchoAtlas)** | [macOS download](https://github.com/nazeeh111/EchoAtlas/releases/latest) | Experimental acoustic gesture controls with calibration, stale-audio rejection, explicit stop controls, and analyzer replay. Live-hand accuracy still needs testing. |
| **[MotionizedAudio](https://github.com/nazeeh111/MotionizedAudio)** | [Known-motion experiment](https://github.com/nazeeh111/MotionizedAudio/blob/main/experiments/known_motion.py) | Continues earlier VisualMic code under a new name. Added a generated known-motion experiment, frequency and timing checks, and safer WAV output handling; real-speech recovery is unverified. |

**[ToolScope](https://github.com/nazeeh111/ToolScope)** adapts MCP Inspector with browser, CLI and terminal inspection plus offline comparison of exported tool definitions. [Try the offline example](https://github.com/nazeeh111/ToolScope#cli-and-terminal-interface).

**[WorkHarbor](https://github.com/nazeeh111/WorkHarbor)** adapts Paperclip into a local task/run workspace with an isolated launcher and selected-file review packets. [Download the source](https://github.com/nazeeh111/WorkHarbor/releases/tag/v0.1.0). Board workflows and mocked run lifecycles are tested; real provider execution remains unvalidated.

## Upstream contribution

Contributed Django package and version mapping to the GitHub Advisory Database. The [published advisory](https://github.com/advisories/GHSA-wvqv-fj8w-qmhm) credits me as **Analyst**. [Accepted change](https://github.com/github/advisory-database/pull/9912).

See each repository's verification notes for its tested scope.

**Publication note:** Projects are published in batches from local Git workspaces. GitHub upload dates are publication dates, not a development timeline.
