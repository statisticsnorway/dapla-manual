# AGENTS.md

## Scope
- This repo is a Quarto website, not an application/service repo. The site source lives under `dapla-manual/`; root-level changes are usually workflow, Nix shell, or repo metadata.

## Workflows
- Primary local check: `quarto preview dapla-manual`
- Focused render without preview: `quarto render dapla-manual --to html`
- If content should show executed output from committed/frozen artifacts rather than run in GitHub Actions, render that file locally with `quarto render <file.qmd|notebook.ipynb> --execute` and keep `freeze: true` in its YAML/front matter.
- If using Nix, `nix develop .#` provides `quarto`.
- CI renders from `dapla-manual/` and deploys `dapla-manual/_site/`.

## Site Structure
- Navigation is manually wired in `dapla-manual/_quarto.yml`; adding a page is not enough, update the relevant navbar/sidebar entry too.
- The published repo links use `repo-subdir: dapla-manual`, so source pages should stay inside that subtree.
- `news/index.qmd` lists `news/posts/*/index.qmd` and enables an RSS feed.
- `blog/index.qmd` lists `blog/posts/*/index.qmd` and does not enable a feed.

## Notebooks And Frozen Output
- Notebook output is intentionally committed in this repo. Do not strip `.ipynb` output here.
- The repo-local `.gitconfig` disables `nbstripout`; if needed, enable it with `git config --local include.path ../.gitconfig`.
- Quarto freeze is enabled globally in `dapla-manual/_quarto.yml` (`freeze: true`). Many notebook-backed pages also set `freeze: true` in front matter.
- For embedded notebooks or pages with executable content, render the specific file explicitly with `--execute`, e.g. `quarto render <file.qmd|notebook.ipynb> --execute`, so committed frozen output matches what the site shows.
- Do not assume GitHub Actions will execute that content; published output can depend on locally generated frozen artifacts committed to the repo.
- Only use open/shareable data in committed notebook output; the site is public.

## Content Conventions
- Internal links should target `.qmd` source files, not generated `.html` or absolute `manual.dapla.ssb.no` URLs.
- For substantial/manual-worthy changes, the repo expects a news post as well; this is reinforced by the PR template and contribution guide.
- The contribution guide asks pages to include a title block with at least title and `date-modified`.

## CI / Preview Behavior
- PRs automatically get a rendered preview from `dapla-manual/_site/` via the `PR Preview` workflow.
- Pushes to `main` render and publish the site to GitHub Pages; preview cleanup happens from `gh-pages` when PRs close.

## Files Worth Checking Before Structural Edits
- `README.md`
- `dapla-manual/_quarto.yml`
- `dapla-manual/statistikkere/appendix/contribution.qmd`
- `.github/workflows/render-preview.yml`
- `.github/workflows/render-and-publish.yml`
