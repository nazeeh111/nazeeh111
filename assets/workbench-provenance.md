# Profile workbench image

The four `workbench-*.png` files are the profile's light, dark, desktop and narrow-screen images. Matching `workbench-*.svg` files retain the editable vector composition. This is an arrangement of three separate projects, not one combined application.

- **Solidrift:** the paired meshes show its original input and recorded `FLOAT` output, where one body is absent. Their projected filled polygons come from the [recorded native report](https://github.com/nazeeh111/Solidrift/blob/8fc9e23471a18165d73646e290700cc10d351eea/tests/fixtures/native-report.json) through the project's geometry generator. The comparison-only `MANIFOLD` wire overlay is omitted. The later 12-triangle witness is not pictured; see the [earlier plate's provenance](missing-body-provenance.md).
- **Capsulith:** the colored squares are a 32 × 32 crop of its [prepared example image](https://github.com/nazeeh111/Capsulith/blob/bc0b77bcd776d07bf43b8716fd9093e389962aee/examples/qoi/orbit.png), not a fresh execution capture. Pixel `(64, 48)` in that image is RGBA `(126, 135, 250, 255)`, also displayed by the existing [image workbench capture](https://github.com/nazeeh111/Capsulith/blob/bc0b77bcd776d07bf43b8716fd9093e389962aee/docs/image-workbench.jpg). The workbench's native QOI round trip and allocation lifecycle are separate product behavior.
- **Syllune:** the three ink lines were traced from its [current studio screenshot](https://github.com/nazeeh111/Syllune/blob/a0fae32f538de693cb66a58b57bd0e89e38c2a5f/docs/assets/studio.png). Its hosted exact checker uses the typed step transcript. Optional ink recognition requires the local Mac companion.

The README keeps the claims and project actions in ordinary text. The image's small labels are supplementary at phone width.
