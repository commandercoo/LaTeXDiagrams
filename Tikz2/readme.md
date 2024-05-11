<h1 align="center">
  <a href="https://janosh.github.io/tikz">
    <img src="assets/favicon.svg" alt="TikZ" height=150>
  </a>
</h1>

<h3 align="center">

[![Made with LaTeX](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg?logo=latex)](https://latex-project.org)
[![Site](https://github.com/janosh/tikz/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/janosh/tikz/actions/workflows/gh-pages.yml)
[![Link Check](https://github.com/janosh/tikz/actions/workflows/link-check.yml/badge.svg)](https://github.com/janosh/tikz/actions/workflows/link-check.yml)
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?logo=github)](https://github.com/janosh/tikz/pulls)
[![DOI](https://zenodo.org/badge/286220365.svg)](https://zenodo.org/badge/latestdoi/286220365)

</h3>

Collection of **111** `standalone` TikZ figures for illustrating concepts in physics, chemistry and machine learning.

Check out [janosh.github.io](https://janosh.github.io/tikz) to search, sort, open in Overleaf and download figures (PDF/SVG/PNG) from this collection.

Have a TikZ image you'd like to share? [Submit a PR](https://github.com/janosh/tikz/pulls) with a `.tex` and metadata `.yml` file in the `assets/` directory and add yourself to the [`citation.cff`](citation.cff) file.

## Images

| &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; |
| :----------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: |
|                                      [`autoencoder`](assets/autoencoder/autoencoder.tex)                                      |                                           [`aviary`](assets/aviary/aviary.tex)                                           |
|                                       ![`autoencoder.png`](assets/autoencoder/autoencoder.png)                                       |                                              ![`aviary.png`](assets/aviary/aviary.png)                                               |
|                               [`basis-plus-lattice`](assets/basis-plus-lattice/basis-plus-lattice.tex)                               |                                     [`bloch-sphere`](assets/bloch-sphere/bloch-sphere.tex)                                     |
|                            ![`basis-plus-lattice.png`](assets/basis-plus-lattice/basis-plus-lattice.png)                             |                                     ![`bloch-sphere.png`](assets/bloch-sphere/bloch-sphere.png)                                      |
|                    [`bose-einstein-distribution-3d`](assets/bose-einstein-distribution-3d/bose-einstein-distribution-3d.tex)                    |                       [`bose-einstein-distribution`](assets/bose-einstein-distribution/bose-einstein-distribution.tex)                       |
|            ![`bose-einstein-distribution-3d.png`](assets/bose-einstein-distribution-3d/bose-einstein-distribution-3d.png)            |                ![`bose-einstein-distribution.png`](assets/bose-einstein-distribution/bose-einstein-distribution.png)                 |
|                                 [`branch-and-bound`](assets/branch-and-bound/branch-and-bound.tex)                                 |                                    [`branch-cuts-1`](assets/branch-cuts-1/branch-cuts-1.tex)                                    |
|                               ![`branch-and-bound.png`](assets/branch-and-bound/branch-and-bound.png)                                |                                    ![`branch-cuts-1.png`](assets/branch-cuts-1/branch-cuts-1.png)                                    |
|                                    [`branch-cuts-2`](assets/branch-cuts-2/branch-cuts-2.tex)                                    |                              [`change-of-variables`](assets/change-of-variables/change-of-variables.tex)                              |
|                                    ![`branch-cuts-2.png`](assets/branch-cuts-2/branch-cuts-2.png)                                    |                           ![`change-of-variables.png`](assets/change-of-variables/change-of-variables.png)                           |
|                         [`closed-string-topologies`](assets/closed-string-topologies/closed-string-topologies.tex)                         |                            [`complex-sign-function`](assets/complex-sign-function/complex-sign-function.tex)                            |
|                   ![`closed-string-topologies.png`](assets/closed-string-topologies/closed-string-topologies.png)                    |                        ![`complex-sign-function.png`](assets/complex-sign-function/complex-sign-function.png)                        |
|                                [`concave-functions`](assets/concave-functions/concave-functions.tex)                                |                                           [`conv2d`](assets/conv2d/conv2d.tex)                                           |
|                              ![`concave-functions.png`](assets/concave-functions/concave-functions.png)                              |                                              ![`conv2d.png`](assets/conv2d/conv2d.png)                                               |
|                                 [`convex-functions`](assets/convex-functions/convex-functions.tex)                                 |                             [`critical-temperature`](assets/critical-temperature/critical-temperature.tex)                             |
|                               ![`convex-functions.png`](assets/convex-functions/convex-functions.png)                                |                         ![`critical-temperature.png`](assets/critical-temperature/critical-temperature.png)                          |
|                                [`cylinder-to-plane`](assets/cylinder-to-plane/cylinder-to-plane.tex)                                |                                 [`detailed-balance`](assets/detailed-balance/detailed-balance.tex)                                 |
|                              ![`cylinder-to-plane.png`](assets/cylinder-to-plane/cylinder-to-plane.png)                              |                               ![`detailed-balance.png`](assets/detailed-balance/detailed-balance.png)                                |
|                                      [`dft-choices`](assets/dft-choices/dft-choices.tex)                                      |                                         [`diagrams`](assets/diagrams/diagrams.tex)                                         |
|                                       ![`dft-choices.png`](assets/dft-choices/dft-choices.png)                                       |                                           ![`diagrams.png`](assets/diagrams/diagrams.png)

## Scripts

Files in [`/scripts`](scripts) render and compress the standalone `.tex` files in [`/assets`](assets) to various formats:

- low + high-res PNG
- PDF
- SVG

To run the scripts requires the following dependencies:

- [`pdf-compressor`](https://github.com/janosh/pdf-compressor) (`pip install pdf-compressor`)
- [`gs` (GhostScript)](https://ghostscript.com) (optional, worse compression but needs no API key so less setup than `pdf-compressor`)
- [`pdf2svg`](https://github.com/dawbarton/pdf2svg) (`brew install pdf2svg`)
- `convert` (part of [ImageMagick](https://imagemagick.org/script))
- [`pngquant`](https://github.com/kornelski/pngquant) (`brew install pngquant`)
- [`zopflipng`](https://github.com/google/zopfli) (`brew install zopfli`)

To run `pdf-compressor` directly or to use it as part of the [`render-tikz.py`](scripts/render-tikz.py) pipeline, you need a free public API key from <https://developer.ilovepdf.com>. Pass it to `pdf-compressor` with:

```sh
pdf-compressor --set-api-key project_public_7c854a9db0...
```
