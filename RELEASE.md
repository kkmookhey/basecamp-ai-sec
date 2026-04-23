# Release / Repo-Creation Procedure

These are the one-time manual steps required when creating or releasing
the Basecamp repository. Automate nothing that touches KK's GitHub
credentials — these steps must be performed interactively.

## First-time repo creation

1. Create the live repo on GitHub:
   - Name: `basecamp-ai-sec`
   - Owner: `kkmookhey` (personal account)
   - Visibility: public
   - Initialize with nothing (we'll push existing history)

2. Push the local repo:

   ```bash
   cd E:/Projects/basecamp-ai-sec
   git remote add origin https://github.com/kkmookhey/basecamp-ai-sec.git
   git branch -M main
   git push -u origin main
   ```

3. Verify CI runs:
   - Open the Actions tab on GitHub.
   - Both `integrity` and `link-check` workflows should complete green on the first push.

## Squat-prevention placeholder repos

Create two empty placeholder repos on the same account to prevent
name-squatting on close variants. These repos exist solely to
redirect any mistaken visitor to the live repo.

For each of `basecamp-aisec` and `ai-sec-basecamp`:

1. Create the repo on GitHub with the same visibility settings.
2. Initialize with a single `README.md`:

   ```markdown
   # basecamp-aisec (reserved)

   This repo name is reserved to prevent typosquatting.
   The real Basecamp repo is at:

   **<https://github.com/kkmookhey/basecamp-ai-sec>**
   ```

3. Archive the repo via Settings → General → Archive. Archived repos
   are read-only, unsquattable, and signal "this is intentional".

## Subsequent releases

Basecamp doesn't release versioned artifacts; `main` is the source of truth.
Mark significant milestones with an annotated tag:

```bash
git tag -a v0.1.0-scaffolding -m "Plan 1 complete: scaffolding and CI"
git push origin v0.1.0-scaffolding
```

Milestones worth tagging:

- `v0.1.0-scaffolding` — Plan 1 complete
- `v0.2.0-content-draft` — Plan 2 complete (all 16 topics status: ready)
- `v0.3.0-paths` — Plan 3 complete (4 paths woven)
- `v1.0.0` — Phase 1 DoD met, ready for Phase 2 (GitHub Pages layer)
