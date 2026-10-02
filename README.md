# GitHub Pages course sample

This repository is a standalone public teaching example for DigitalTechIQ.
It contains only the static sample page, version metadata, a validation script,
and its Pages workflow. No private training repository files or recordings are
included.

Run `python scripts/check_site.py` to validate the sample locally. Serve `site/`
with a local HTTP server to preview it. During the hosted build, validation
records `GITHUB_SHA` in `site/version.json`. Compare that value on the live site
with the deployment's source commit.

The workflow validates and uploads the site before a separate deployment job.
Configure this repository's Pages source as GitHub Actions before deploying.
This local candidate has not yet been published.
