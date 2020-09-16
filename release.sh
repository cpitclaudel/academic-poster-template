#!/usr/bin/env bash
zip --junk-paths academic-poster-template-$(git describe --abbrev=0 --tags).zip docs/tutorial/poster.html docs/tutorial/poster.css
