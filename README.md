# Nazeeh Abdul-Hadi

**Graphics, sensing, and systems software.**

I build and adapt software for 3D modeling, computational imaging, acoustic sensing, and developer workflows.

[Open SolidFrame CAD](https://nazeeh111.github.io/SolidFrame/) · [Open LumaField](https://nazeeh111.github.io/LumaField/) · [Try optical transfer](https://nazeeh111.github.io/PhotonRelay/) · [Download EchoAtlas](https://github.com/nazeeh111/EchoAtlas/releases/latest) · [All repositories](https://github.com/nazeeh111?tab=repositories)

## Selected work

| Project | Open it | Implementation |
| :--- | :--- | :--- |
| **[SolidFrame](https://github.com/nazeeh111/SolidFrame)** | [Browser CAD](https://nazeeh111.github.io/SolidFrame/) | An OpenCascade-based browser CAD adaptation with parametric sketches and editable feature history. Start from seven native fixture solids; edit dimensions, save local documents, or exchange STEP, IGES, BREP, STL, OBJ, and PLY. |
| **[LumaField](https://github.com/nazeeh111/LumaField)** | [Browser viewer](https://nazeeh111.github.io/LumaField/) | A Gaussian-splat viewer adaptation. Load local `.splat` and binary `.ply` scenes, inspect camera files, save views, and export conversions. Includes a real captured scene and a generated architectural study. |
| **[PhotonRelay](https://github.com/nazeeh111/PhotonRelay)** | [Browser app](https://nazeeh111.github.io/PhotonRelay/) | Send files as animated QR codes and receive them in a browser. Scan a setup QR with an ordinary phone camera to open the receiver. Includes a simulation for testing recovery from lost frames. |
| **[EchoAtlas](https://github.com/nazeeh111/EchoAtlas)** | [macOS download](https://github.com/nazeeh111/EchoAtlas/releases/latest) | Experimental acoustic gesture controls for macOS, built in Swift. Includes calibration, stale-audio rejection, explicit stop controls, and analyzer replay. Live-hand accuracy still needs testing. |
| **[MotionizedAudio](https://github.com/nazeeh111/MotionizedAudio)** | [Known-motion experiment](https://github.com/nazeeh111/MotionizedAudio/blob/main/experiments/known_motion.py) | Recover sound from subpixel video motion. Generated signals probe frequency, amplitude ratios, silence, timing, and filter rejection through the CLI. |
| **[DurableStore](https://github.com/nazeeh111/DurableStore)** | [Source release](https://github.com/nazeeh111/DurableStore/releases/tag/v0.2.0) | Rust storage with atomic multi-key batches, checksummed recovery, exclusive locks and compaction. Includes process-crash tests and an outbox-state example. |

## Other projects

**AI and developer infrastructure:** [ToolScope](https://github.com/nazeeh111/ToolScope) adapts MCP Inspector with browser, CLI, and terminal interfaces, bundled local examples, and portable tool-schema baselines that can be exported, imported, and compared. It runs with a local backend. [PolicyDelta](https://github.com/nazeeh111/PolicyDelta) tests before-and-after OpenBao policies with the same requests and synthetic fixtures, then reports access changes. [AgentLedger](https://github.com/nazeeh111/AgentLedger) runs bounded local task graphs, verifies artifacts, and records command results alongside optional Codex reviews. [VaultLens](https://github.com/nazeeh111/VaultLens) is an offline Go tool for auditing password exports with redacted output.

**Local operations:** [Muster](https://nazeeh111.github.io/Muster/) repairs volunteer rotas while preserving locked commitments and explains staffing shortages. It runs locally in the browser, with project import/export and assignment CSV. [Source and download](https://github.com/nazeeh111/Muster/releases/tag/v0.1.0). [WorkHarbor](https://github.com/nazeeh111/WorkHarbor) adapts Paperclip into a local task and run workspace, with an isolated launcher and selected-file review packets. [Download the source](https://github.com/nazeeh111/WorkHarbor/releases/tag/v0.1.0); board workflows and mocked run lifecycles are tested, while real provider execution remains unvalidated.

**Scientific and numerical software:** [ModelForge](https://github.com/nazeeh111/ModelForge) implements numerical modeling in Rust; [SequenceForge](https://github.com/nazeeh111/SequenceForge) covers sequence alignment and phylogenetics. [MoleculeBench](https://github.com/nazeeh111/MoleculeBench) compares molecular bond models against numerical references.

**Signals and inverse problems:** [HiddenWave](https://github.com/nazeeh111/HiddenWave), [CornerVision](https://github.com/nazeeh111/CornerVision), and [ApertureTrace](https://github.com/nazeeh111/ApertureTrace) explore hidden-scene reconstruction. [RadarVolume](https://github.com/nazeeh111/RadarVolume), [SoundMap](https://github.com/nazeeh111/SoundMap), and [ChirpMotion](https://github.com/nazeeh111/ChirpMotion) connect array geometry and recorded signals to spatial or spectral results.

**Data applications:** [SchemaRehearsal](https://github.com/nazeeh111/SchemaRehearsal) replays application scenarios on isolated SQLite copies before and after a migration. Its included example detects a lost audit trigger even when database integrity checks pass. [Install the local CLI](https://github.com/nazeeh111/SchemaRehearsal/releases/tag/v0.1.0). [MarketObservatory](https://github.com/nazeeh111/MarketObservatory) compares CSV price series and portfolio allocations, with HTML, JSON, and CSV exports. [MarketWeave](https://github.com/nazeeh111/MarketWeave) provides prediction-market data and order-book interfaces.

Some sensing projects still need specialized hardware or datasets for real-world evaluation. See each repository's verification notes for its tested scope.

**Publication note:** Projects are published in batches from local Git workspaces. GitHub upload dates are publication dates, not a development timeline.
