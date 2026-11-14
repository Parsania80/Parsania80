# Publish this GitHub profile

This folder is the source for the profile README displayed at https://github.com/Parsania80.

See GitHub’s [profile README requirements](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) for the repository naming and visibility rules.

1. Create a **public** GitHub repository named **Parsania80** under the **Parsania80** account. Leave the initialization options unchecked, since these files already include a README.
2. Upload `README.md`, the entire `assets` folder, `scripts`, and `.github/workflows/profile-assets.yml` to the root of that repository. The workflow and scripts maintain the activity artwork. You can also include `.gitignore` and this guide.
3. Commit the files to the default branch. The README will appear on the profile automatically.

Alternatively, after creating the empty repository, publish from this folder:

```bash
git init -b main
git add README.md assets scripts .github .gitignore SETUP.md
git commit -m "Create GitHub profile"
git remote add origin https://github.com/Parsania80/Parsania80.git
git push -u origin main
```

## Maintain the design

- Edit the profile text in `README.md`.
- Update the names, labels, or colors in `scripts/generate_assets.py`, then run `python3 scripts/generate_assets.py` to regenerate the artwork.
- Edit `scripts/forg_panels.py` to update the six FORG contribution panels. Each result stays with its relevant contribution area: connection validation in the device-server panel, implementation-time savings in testing, and component packaging in CI/CD.
- Edit `scripts/research_feature.py` for the master’s research feature and its binary/four-way tree illustration. The research summary itself is in `README.md`.
- All graphics are local SVG assets. Rendering uses no remote stats services, analytics, JavaScript, or external fonts.
- The README switches artwork with the GitHub light/dark color scheme using `<picture>` elements.
- At mobile viewport widths, the hero and project cards switch to simpler artwork with larger lettering.
- `scripts/preview.py` generates local light and dark previews in `.preview/`. It requires the Python `markdown-it-py` package and is only a review aid; the published profile uses GitHub’s Markdown renderer.

## Activity updates

- Run `python3 scripts/refresh_activity.py` to fetch your public GitHub repository metadata, language bytes, and GitHub-visible contribution calendar. The updater uses the current date in Asia/Tehran. It never reads local private repositories.
- The source snapshot is `assets/activity-data.json`. Both the statistics and the isometric contribution terrain use that real data.
- `.github/workflows/profile-assets.yml` refreshes activity every six hours or when started manually from Actions. GitHub may delay scheduled jobs or disable schedules for inactive repositories.
- The workflow uses GitHub's automatically supplied `GITHUB_TOKEN` with permission to update this profile repository. No personal access token is required, and no token is stored in the graphics or source snapshot. Branch protection or repository policies can prevent automatic commits.
- GitHub contribution counts may include anonymized private counts if your account exposes them. Language shares cover public non-fork repositories only; smaller languages are grouped into Other. Work in a separate company GitLab is outside this data.
- A failed calendar fetch or unexpected calendar markup stops the updater and preserves the existing snapshot.

## Editorial notes

- The company and private-app descriptions summarize the owner’s contributions. No private source code, internal file paths, infrastructure addresses, or credentials are included.
- The 100,000-connection statement is based on the owner’s confirmation that the workload was designed and validated with a connection tester. It does not claim a production deployment size or a throughput benchmark.
- The 3-month-to-14-day testing improvement is the owner’s reported result.
- FluxGet and parsBackUp descriptions were checked against their public repositories on November 14, 2026. parsBackUp is described as an ongoing development project.
- The Master-Hybrid-MLS entry was checked against its public thesis PDF and current `implementation/new` code on November 14, 2026. It describes an experimental Rust research prototype, without claiming audited security, production suitability, standard interoperability, or an amortized performance improvement.
