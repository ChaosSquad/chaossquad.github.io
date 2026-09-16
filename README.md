# ChaosSquad Documentation
This repository contains the documentation of the ChaosSquad projects.
It is published at [documentation.chaossquad.net](https://documentation.chaossquad.net/).

## Layout
| Path              | What it is                                                      |
|-------------------|-----------------------------------------------------------------|
| `documentation/`  | The sources. This is the mkdocs `docs_dir`, edit things here.    |
| `docs/`           | The built site (mkdocs `site_dir`), deployed to GitHub Pages. Generated, never edit by hand. |
| `mkdocs.yml`      | Site configuration and navigation.                               |
| `hooks/`          | Build hooks (writes `.nojekyll` into the built site).            |

The naming is unfortunate but forced: GitHub Pages can only deploy from `/docs`,
so that name is taken by the output and the sources live in `documentation/`.

## Building
```
pip install mkdocs-material
mkdocs build     # writes docs/
mkdocs serve     # live preview on http://127.0.0.1:8000
```
The built `docs/` directory is committed, because GitHub Pages serves it directly.
So: build before committing, and commit the result together with the sources.
