"""Write a .nojekyll marker into the built site.

GitHub Pages runs Jekyll over the published directory unless this file exists.
MkDocs skips dotfiles inside docs_dir, so it cannot simply be committed there --
it has to be created after every build.
"""

import os


def on_post_build(config, **kwargs):
    open(os.path.join(config["site_dir"], ".nojekyll"), "w").close()
