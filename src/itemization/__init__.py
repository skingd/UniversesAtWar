"""Itemization & capability aggregation pipeline.

See plans/itemization.prompt.md. Runs *after* `uaw-datacheck` has produced
canonical indices in data/index/. Emits catalogues and capability
distributions to output/itemization/.
"""
