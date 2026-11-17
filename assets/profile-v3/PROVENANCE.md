# Profile v3 artwork and evidence

## Original typographic cover

`cover-wide-light.svg`, `cover-wide-dark.svg`, `cover-mobile-light.svg` and `cover-mobile-dark.svg` are original static compositions for Nazeeh Abdul-Hadi's profile. `cover-wide-light.png`, `cover-wide-dark.png`, `cover-mobile-light.png` and `cover-mobile-dark.png` are direct browser renders of those exact SVGs, without raster editing. The files contain only outlined type and flat color fields, with no activity metrics, product GUI, scientific plot or runtime claim. Light/dark and wide/phone compositions preserve the intended name breaks.

Typeface: Bricolage Grotesque by The Bricolage Grotesque Project Authors, under SIL Open Font License1.1. The unchanged [font source](https://github.com/google/fonts/blob/7af0d90b4d532ffa4b041937b560c6df4e7b1e95/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz%2Cwdth%2Cwght%5D.ttf) has Git blob SHA1 `9a4ca271ff84357bb8f8830ce71b85ea3571f731`. Full [OFL terms and copyright](fonts/OFL.txt) and the unchanged [font](fonts/BricolageGrotesque.ttf) are retained. The build uses weight750 for the name, weight500 for the role, width85 and optical size48. Outlining means no external font request is needed to display the SVG or PNG.

[build-cover.py](build-cover.py) is the editable layout/source recipe. It requires fontTools only; no network or analysis runs. Layout records retain text, sizes and measured advance widths. The SVG title/description and README alt text preserve the textual identity when outlined paths are not selectable.

The cover's composition was influenced by GitSkins' public cover/showcase approach, independently authored without copying its proprietary template code, images or widget assets. GitSkins is a design reference, not the source or host of these files.

## PhotonSmith numerical figure

`photonsmith.png` and `photonsmith-mobile.png` are unchanged copies of the public PhotonSmith [wide figure](https://github.com/nazeeh111/PhotonSmith/blob/a3ecad3af5f0bb957334f58f73379c886463aa42/docs/presentation/field-and-spectrum.png) and [phone figure](https://github.com/nazeeh111/PhotonSmith/blob/a3ecad3af5f0bb957334f58f73379c886463aa42/docs/presentation/field-and-spectrum-mobile.png). They show the stored M9 Maxwell real electric field and wavelength samples for the refined1550nm periodic grating. These are numerical outputs, not neural field predictions, physical measurements or fabricated-device validation. No pixels, labels, axes, color scale, aspect ratio or samples were changed for this profile.

The source and plotting choices are documented in the [pinned figure record](https://github.com/nazeeh111/PhotonSmith/blob/a3ecad3af5f0bb957334f58f73379c886463aa42/docs/presentation/README.md). The source project is MIT; its [complete notice](PhotonSmith-LICENSE.txt) is retained. `source-files.json` binds source URLs, Git blob identities, SHA256 and lengths of the exact downloaded files. The rest of the profile's earlier asset provenance remains in its original files and asset map.
