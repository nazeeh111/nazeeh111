# Profile cover

`cover-wide-light.png`, `cover-wide-dark.png`, `cover-mobile-light.png` and `cover-mobile-dark.png` are renders of `cover.html` with Arial and the included `weights.svg`. `make-weights.py` extracts all 144 prism faces from `model.svg` without changing their geometry, adjusts the palette to neutral gray and cobalt, and gives the drawing room to fit. The 48 prisms encode the actual compiled coefficients: height is absolute weight, blue is positive, gray is negative and a flat white tile is zero. No placement on physical hardware is implied. The layout is original and the background has been removed from the illustration. Render with `node render.mjs` using a local Playwright and Chrome installation; its import and executable paths can be adapted to the local installation.

The illustration was generated from the compiler artifacts described below. The [Apache-2.0 license](SILICONPILOT-LICENSE.txt) and third-party notices in `THIRD_PARTY.md` are retained here.

# SiliconPilot evidence illustrations

The model illustration is generated from the [published case artifacts at fc774a8](https://github.com/nazeeh111/SILICONPILOT/tree/fc774a8411f0a008821e95637b810db2a508c962/docs/presentation). The case records compiler revision [6e2bbbe](https://github.com/nazeeh111/SILICONPILOT/tree/6e2bbbe2faca1f10eb4a2a1e71a8aa858c56ffd1). Run `python3 generate.py PATH_TO_SILICONPILOT` with a checkout containing that evidence. Generation uses the Python standard library and checks the original ZIP and expected-vector SHA-256 digests. No datasets, fonts or external artwork are bundled.

| View | Accessible description and interpretation |
| --- | --- |
| model.svg | The banknote classifier takes four standardized features, applies eight hidden ReLU units and returns two signed scores. Each tower represents one compiled integer coefficient from the 4 × 8 or 8 × 2 transformation. Height shows absolute magnitude on one common scale. Positive coefficients have blue faces, negative coefficients have slate faces and zeros have a flat white tile. The drawing describes logical weights. |

The project distributes its source under [Apache-2.0](https://github.com/nazeeh111/SILICONPILOT/blob/fc774a8411f0a008821e95637b810db2a508c962/LICENSE). The original [third-party and dataset notices](https://github.com/nazeeh111/SILICONPILOT/blob/fc774a8411f0a008821e95637b810db2a508c962/docs/THIRD_PARTY.md) remain in the [downloadable evidence](https://github.com/nazeeh111/SILICONPILOT/blob/fc774a8411f0a008821e95637b810db2a508c962/docs/presentation/compiled-example.zip). The drawing reads generated model coefficients and digital test results. It uses no photographed hardware or inferred physical placement.

The model SVG includes a title and description. When embedding it with an HTML image element, supply equivalent alt text in that element.
