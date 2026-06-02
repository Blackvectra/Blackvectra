# LinkedIn Posts

A lightweight content repo for **writing, versioning, and reviewing LinkedIn posts as
files**. There is no API, no developer app, no tokens, and no automation — you publish by
copy-pasting the post body into LinkedIn yourself. The git workflow gives you draft history,
PR review of wording, and a clean record of what was posted and where.

## Layout

```
posts/
├── TEMPLATE.md      # copy this to start a new post
├── drafts/          # work-in-progress posts
└── published/       # posts already live (with date + permalink recorded)
scripts/
└── check.py         # optional, dependency-free linter (frontmatter + length)
```

## Post format

Each post is a markdown file with YAML frontmatter:

```markdown
---
title: SPF/DKIM/DMARC the right way
status: draft            # draft | published
audience: PUBLIC         # PUBLIC | CONNECTIONS (intent only; informational)
tags: [email-security, m365]
published_date:          # YYYY-MM-DD, filled when moved to published/
permalink:               # LinkedIn URL, filled after posting
---

The post body — exactly what you paste into LinkedIn.
```

Everything below the closing `---` is the post body. Keep it under **3000 characters**
(LinkedIn's limit for a post).

## Workflow

1. **Draft** — copy `posts/TEMPLATE.md` to `posts/drafts/<yyyy-mm>-<slug>.md` and write
   the post.
2. **Review** — open a pull request. Refine the wording in the diff; merge when happy.
3. **Publish** — copy the body (everything under the frontmatter) into LinkedIn and post.
4. **Archive** — move the file to `posts/published/`, set `status: published`, and fill in
   `published_date` and `permalink`.

## Checking posts

Validate frontmatter and length with the bundled linter (Python 3, no dependencies):

```bash
python scripts/check.py
```

It reports missing/invalid frontmatter keys and any post body over 3000 characters, and
exits non-zero if anything is wrong — so you can wire it into CI later if you want.

## Using this as a standalone repo

This was scaffolded inside the `blackvectra/blackvectra` profile repo under
`linkedin-poster/`. To lift it into its own repo (e.g. `blackvectra/linkedin-posts`):

```bash
# from a fresh clone of an empty blackvectra/linkedin-posts repo
cp -r /path/to/blackvectra/linkedin-poster/. .
git add .
git commit -m "Initial LinkedIn posts content repo"
git push
```
