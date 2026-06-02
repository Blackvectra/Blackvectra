# OSINT Hygiene Guidelines

> Standards for what does and does not get published in this organization's public repositories.

## Purpose

Every public repository under this account is part of an attack surface. This document sets the baseline for what is safe to publish, what is not, and how to scrub material before commit.

## Always-Public (Brand Surface)

These are intentional public identifiers and form part of the organization's brand:

- Organization name and website
- Public-facing professional identity
- Held certifications (final state only)
- Frameworks, standards, and methodologies practiced
- Generic technology stack categories

## Never-Public (Hard Block)

Material in this list does not get committed under any circumstances. If discovered in history, rotate any credentials and rewrite history with `git filter-repo`.

- Live credentials of any kind: API keys, tokens, passwords, connection strings, certificates with private keys
- Production tenant identifiers: tenant GUIDs, subscription IDs, real UPNs, real email recipients
- Real client names or domains in any context (configuration, examples, documentation, screenshots)
- Real internal IP addresses, hostnames, or asset inventory
- Personal identifiers beyond the public brand: phone numbers, physical addresses, date of birth, government identifiers
- Hardware serial numbers, MAC addresses, device IDs
- Geographic markers below country level
- Employer name combined with internal tooling, processes, or client references

## Soft-Caution (Public, but reframe before publishing)

Acceptable in public repos only after generalization:

- Architectural reference designs (must be framed as reference / illustrative, not deployed)
- Lab topologies (use RFC1918 placeholders, generic hostnames)
- Configuration examples (use `example.com`, `contoso.com`, `<tenant-id>` placeholders)
- Screenshots (must be from sanitized lab data, never production)
- Threat intelligence sharing (verify upstream attribution and licensing)
- Cert progress (held only — do not publish in-progress or failed attempts)

## Pre-Commit Checklist

Before any public commit:

- [ ] `git diff` reviewed for real identifiers
- [ ] Grep run: `git diff | grep -iE "<your-real-domain>|<your-employer>|<your-tenant-id>"`
- [ ] No screenshots contain real IPs, hostnames, MACs, or browser context
- [ ] No log fixtures contain real source/destination IPs or usernames
- [ ] All example configs use documentation-reserved placeholders (`example.com`, RFC1918, RFC5737)
- [ ] No new EXIF or document metadata introduced (run scrubber on images and PDFs)

## Image and Document Scrubbing

### Images

- Strip EXIF, IPTC, XMP, and vendor private chunks before commit
- Common tools: `exiftool -all= file.png`, `convert in.png -strip out.png`
- Watch for vendor-specific chunks: Canva (`caBX`), Adobe (`XMP`), camera apps (GPS)

### PDFs

- Strip author, title, producer, creator metadata: `exiftool -all= file.pdf`
- Flatten any annotations or form fields that may contain user data
- Confirm no embedded fonts contain identifying subset data

### Office documents

- Run File → Inspect Document → Document Properties and Personal Information → Remove All
- Do not commit `.docx` / `.xlsx` / `.pptx` without scrubbing tracked changes, comments, and revision history

## Repository Lifecycle

- Default repo creation visibility: **private**
- Visibility change to public requires this checklist completed
- Archive rather than delete when retiring repos with public history
- For repositories that *must* be public (MTA-STS policy hosting, GitHub Pages): minimize contents to only what the protocol requires

## Incident Response

If a leak occurs:

1. Rotate any credentials exposed within 1 hour of discovery
2. Rewrite git history with `git filter-repo` to remove the content from all commits
3. Force-push the rewritten history
4. Request GitHub cache purge for the affected commits
5. Notify any third parties whose data was exposed
6. Document the incident, root cause, and control update in this repo's history
