# Repository Sanitization PR Template

> Drop this template into any repo being scrubbed for OSINT exposure. One PR per repo.

## Title format

`Sanitize <repo>: remove OSINT exposure, generalize examples`

## PR body

```markdown
## Summary

Removes operationally sensitive content from this repository and generalizes
remaining examples per OSINT-HYGIENE.md.

## Scrubbed

### Identifiers
- [ ] Real domain names → `example.com` / `contoso.com`
- [ ] Real tenant IDs / GUIDs → `<tenant-id>`
- [ ] Real UPNs / email addresses → `user@example.com`
- [ ] Real IP addresses → RFC1918 (`10.x.x.x`) or TEST-NET (`198.51.100.x`)
- [ ] Real hostnames → `fw01`, `sw01`, generic
- [ ] Real client / employer names → removed or generalized

### Code / configuration
- [ ] Secrets scanned: `gitleaks detect` clean
- [ ] No API keys, tokens, connection strings
- [ ] No private keys or certificates
- [ ] Example configs use documentation-reserved placeholders

### Documentation
- [ ] README reframed as reference / illustrative where applicable
- [ ] First-person ("I deployed", "my network") rewritten as neutral voice
- [ ] No specific vendor version numbers where unnecessary
- [ ] No geographic markers below country level
- [ ] Cert / progression status removed if in-progress

### Media
- [ ] All images stripped of EXIF/XMP/IPTC: `exiftool -all= <image>`
- [ ] Canva `caBX` chunks stripped: `exiftool -all= <png>` or `convert in.png -strip out.png`
- [ ] No screenshots contain real IPs, MACs, hostnames, browser context
- [ ] All PDFs stripped of metadata
- [ ] Diagrams use generic labels

### Git history
- [ ] `git log -p | grep -iE "<your-real-identifiers>"` clean
- [ ] If sensitive content existed in history → history rewritten with `git filter-repo`
- [ ] If rewritten → force-push performed AND GitHub cache purge requested

### Repo metadata
- [ ] Repo description generalized
- [ ] Repo topics reviewed for entity-specific tags
- [ ] Repo name reviewed (renamed if it referenced an internal entity)

## Out of scope

List anything intentionally left as-is and why (e.g., "MTA-STS repos must list real domain — structural").

## Verification

- [ ] Rendered README reviewed on GitHub UI
- [ ] All links resolve
- [ ] Examples still functional after generalization
- [ ] No CI regressions introduced
```

## Quick commands

```bash
# Secret scan
gitleaks detect --source . --no-banner

# Find your identifiers
git grep -iE "your-real-name|your-employer|your-tenant-id|your-domain\.com"

# Find IPs in tracked files
git grep -E "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"

# Strip metadata from all PNGs/JPGs in repo
find . -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -exec exiftool -overwrite_original -all= {} \;

# Find images that still have metadata
find . -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -exec exiftool -S -G {} \;

# History rewrite (DESTRUCTIVE — confirm intent first)
git filter-repo --replace-text replacements.txt
```

## When to escalate vs. just commit

| Situation | Action |
|---|---|
| Real values appear only in current `main` | Sanitize, commit, merge |
| Real values appear in past commits but no credentials | Sanitize current `main`; accept history exposure or archive repo |
| Credentials in any commit | **Stop. Rotate credentials immediately. Then rewrite history.** |
| Client domains / names anywhere | Stop. Confirm with client before any public sanitization commit (the commit log itself is public evidence) |
| Uncertain whether something is sensitive | Default to scrub; ask before un-scrubbing |
