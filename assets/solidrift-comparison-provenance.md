# Solidrift comparison

The two panels in `solidrift-comparison.svg` and its responsive phone variant depict the **original 132-triangle stage**, not the later reduced witness. This is a technical visualization of recorded geometry, not a fresh Blender computation. The unchanged original illustration is `missing-body-light.svg`; [prior provenance](missing-body-provenance.md) remains intact.

Its mesh projections derive from Solidrift's [native report](https://github.com/nazeeh111/Solidrift/blob/8fc9e23471a18165d73646e290700cc10d351eea/tests/fixtures/native-report.json) and [projection generator](https://github.com/nazeeh111/Solidrift/blob/8fc9e23471a18165d73646e290700cc10d351eea/tools/tour/generate-geometry.py). The original operands descend from Manifold regression fixtures under Apache-2.0; the [license](solidrift-fixture-LICENSE.txt) is retained.

The preserved original is [missing-body-light.svg](missing-body-light.svg). The [recomposition script](build-solidrift-figure.py) reproduces both responsive variants from those source projections. Geometry and recorded output are unchanged; layout and labels changed. No new geometry or solver result was invented for this image.
