# Nazeeh Abdul-Hadi

**Graphics, sensing, and systems software.**

I build tools for staffing, migration checks, and storage, alongside graphics and sensing applications.

[Open Muster](https://nazeeh111.github.io/Muster/) · [Try SchemaRehearsal](https://github.com/nazeeh111/SchemaRehearsal#try-a-migration-that-loses-an-audit-trail) · [Explore DurableStore](https://github.com/nazeeh111/DurableStore) · [All repositories](https://github.com/nazeeh111?tab=repositories)

## Original software

| Project | Open it | Implementation |
| :--- | :--- | :--- |
| **[Muster](https://github.com/nazeeh111/Muster)** | [Browser worksheet](https://nazeeh111.github.io/Muster/) | Repairs volunteer rotas while preserving locked commitments. It maximizes coverage, then minimizes assignment changes, and explains collective shortages. Runs locally with project import/export and assignment CSV. |
| **[Camwright](https://github.com/nazeeh111/Camwright)** | [Run locally](https://github.com/nazeeh111/Camwright#run-locally) | Local in-line roller-cam design with an editable motion cycle and linked profile/displacement views. Checks pressure, pitch convexity and roller curvature over continuous angles; returns Pass, Fail or Unresolved. Saves the current inspection with exact inputs and evidence for any result; exports separate physical and pitch CSV/SVG with bounded approximation error after a passing check. |
| **[Sley](https://github.com/nazeeh111/Sley)** | [Run locally](https://github.com/nazeeh111/Sley#run-locally) | Adapts supported rising-shed weaving drafts to declared physical pedals and allowed pairs, preserving thread structure and colors. Retains exact selected tie-ups, including untied pedals, while assigning spare pedals. Shows the drawdown and per-pick actions; reports Feasible, Infeasible or Unknown. Exports adapted WIF, an action CSV and a printable tie-up sheet. |
| **[Signelet](https://github.com/nazeeh111/Signelet)** | [Repeated-word example](https://github.com/nazeeh111/Signelet#try-the-example) | Transfers native STAM annotations across text edits only when every minimum-cost character alignment agrees on an unchanged span. Preserves unresolved originals, offers offline decision review with explicit alignment pins, and records native data and provenance. |
| **[Reticle](https://github.com/nazeeh111/Reticle)** | [Synthetic TIFF comparison](https://github.com/nazeeh111/Reticle#run) | Checks whether microscopy exports preserve recorded physical scale. Distinguishes changed, missing and unit-equivalent calibration, checks supported image-plane mappings, and produces local batch reports. |
| **[SchemaRehearsal](https://github.com/nazeeh111/SchemaRehearsal)** | [Runnable example](https://github.com/nazeeh111/SchemaRehearsal#try-a-migration-that-loses-an-audit-trail) | Replays declared application scenarios on isolated before/after SQLite copies, including transaction commits and expected constraint failures. Its example detects a lost payment-audit trigger even though both migrations preserve rows and pass integrity checks. |
| **[DurableStore](https://github.com/nazeeh111/DurableStore)** | [Source release](https://github.com/nazeeh111/DurableStore/releases/tag/v0.2.0) | Rust key-value storage with atomic multi-key batches, checksummed recovery, exclusive locks, and compaction. Includes process-crash tests and an outbox-state example; power-loss behavior depends on the filesystem and hardware. |

## Adaptations and experiments

Each repository documents its source lineage, licenses, and added work.

| Project | Open it | Contribution |
| :--- | :--- | :--- |
| **[SolidFrame](https://github.com/nazeeh111/SolidFrame)** | [Browser CAD](https://nazeeh111.github.io/SolidFrame/) | Browser CAD adaptation with an editable native fixture, restricted URL plugin loading, separate project storage, and save-confirmation fixes. |
| **[LumaField](https://github.com/nazeeh111/LumaField)** | [Browser viewer](https://nazeeh111.github.io/LumaField/) | Gaussian-splat renderer adaptation with local `.splat` and binary `.ply` loading, camera import, conversions, and an original procedural scene. |
| **[PhotonRelay](https://github.com/nazeeh111/PhotonRelay)** | [Browser app](https://nazeeh111.github.io/PhotonRelay/) | Optical-transfer adaptation with a phone setup link and a channel lab for testing frame loss and duplication. |
| **[EchoAtlas](https://github.com/nazeeh111/EchoAtlas)** | [macOS download](https://github.com/nazeeh111/EchoAtlas/releases/latest) | Experimental acoustic gesture controls with calibration, stale-audio rejection, explicit stop controls, and analyzer replay. Live-hand accuracy still needs testing. |
| **[MotionizedAudio](https://github.com/nazeeh111/MotionizedAudio)** | [Known-motion experiment](https://github.com/nazeeh111/MotionizedAudio/blob/main/experiments/known_motion.py) | Continues earlier VisualMic code under a new name. Added a generated known-motion experiment, frequency and timing checks, and safer WAV output handling; real-speech recovery is unverified. |

## Other projects

**AI and developer infrastructure:** [ToolScope](https://github.com/nazeeh111/ToolScope) adapts MCP Inspector with browser, CLI, and terminal interfaces, bundled local examples, and portable tool-schema baselines that can be exported, imported, and compared. It runs with a local backend. [PolicyDelta](https://github.com/nazeeh111/PolicyDelta) tests before-and-after OpenBao policies with the same requests and synthetic fixtures, then reports access changes. [AgentLedger](https://github.com/nazeeh111/AgentLedger) runs bounded local task graphs, verifies artifacts, and records command results alongside optional Codex reviews. Durable checkpoints let it resume verified command tasks after an interrupted run. [VaultLens](https://github.com/nazeeh111/VaultLens) is an offline Go tool for auditing password exports with redacted output.

**Local operations:** [WorkHarbor](https://github.com/nazeeh111/WorkHarbor) adapts Paperclip into a local task and run workspace, with an isolated launcher and selected-file review packets. [Download the source](https://github.com/nazeeh111/WorkHarbor/releases/tag/v0.1.0); board workflows and mocked run lifecycles are tested, while real provider execution remains unvalidated.

**Scientific and numerical software:** [ModelForge](https://github.com/nazeeh111/ModelForge) implements numerical modeling in Rust; [SequenceForge](https://github.com/nazeeh111/SequenceForge) covers sequence alignment and phylogenetics. [MoleculeBench](https://github.com/nazeeh111/MoleculeBench) compares molecular bond models against numerical references.

**Signals and inverse problems:** [HiddenWave](https://github.com/nazeeh111/HiddenWave), [CornerVision](https://github.com/nazeeh111/CornerVision), and [ApertureTrace](https://github.com/nazeeh111/ApertureTrace) explore hidden-scene reconstruction. [RadarVolume](https://github.com/nazeeh111/RadarVolume), [SoundMap](https://github.com/nazeeh111/SoundMap), and [ChirpMotion](https://github.com/nazeeh111/ChirpMotion) connect array geometry and recorded signals to spatial or spectral results.

**Data applications:** [MarketObservatory](https://github.com/nazeeh111/MarketObservatory) compares CSV price series and portfolio allocations, with HTML, JSON, and CSV exports. [MarketWeave](https://github.com/nazeeh111/MarketWeave) provides prediction-market data and order-book interfaces.

Some sensing projects still need specialized hardware or datasets for real-world evaluation. See each repository's verification notes for its tested scope.

**Publication note:** Projects are published in batches from local Git workspaces. GitHub upload dates are publication dates, not a development timeline.
