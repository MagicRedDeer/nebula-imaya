> Mirror of [nebulapipeline/nebula-imaya](https://bitbucket.org/nebulapipeline/nebula-imaya), part of the
> Nebula Pipeline. Kept here for reference; the original is canonical.

# nebula-imaya

Maya utilities for the Nebula Pipeline: the parts of the pipeline that live inside the application rather
than beside it.

- `files.py`, `references.py` — scene file info, reference loading, and the bookkeeping that keeps a
  referenced shot intact through a save.
- `geosets.py` — geometry set handling.
- `textures/` — texture path resolution. Redshift texture, sprite, normal-map and IES nodes, UDIM and
  frame-sequence detection, `pathmap.py` for resolving map paths by token rather than by absolute path.
- `xgentools.py` — XGen description and guide queries.
- `utils.py`, `general.py`, `exceptions.py` — shared helpers, including render-layer token substitution.

## Authorship

Built between 2019 and 2021, with commit dates running back to 2013 from history carried over when the
repository was created.

Of 184 commits:

| Author | Commits |
|---|---|
| Talha Ahmed (pipeline lead) | 106 |
| Qurban Ali | 42 |
| Hussain Parsaiyan | 36 |

Qurban and Hussain worked on this module under my direction. The split is visible in the log because it
happened that way; this mirror is not a claim to have written all of it.

## Two things that are not mine

- **`__init__.py` embeds a MEL procedure**, `doCreateGeometryCache2`, a modified copy of Maya's own
  `doCreateGeometryCache` that forces per-geometry caching. The original is Autodesk's. It is kept as it
  was written rather than stripped, because the override is the point of the file.
- The rest of the pipeline, and its architecture, is indexed in the
  [Nebula Pipeline repository](https://github.com/MagicRedDeer/nebula-pipeline).

## Licence

The original repository carries **no licence file**, and this mirror does not add one. Nothing here is
offered under a separate grant; it is published for reference only.
