# Threat Model — Public GitHub Presence

> Scope: this GitHub account, its public repositories, and any account-linked assets (profile metadata, GitHub Pages, hosted MTA-STS policies).

## Assets

| Asset | Sensitivity | Notes |
|---|---|---|
| Public brand identity (name, website) | Public by design | Brand surface |
| Held certifications | Public by design | Brand surface |
| Public repository code | Public by design | Subject to OSINT-HYGIENE.md |
| Account email | Restricted | Should not appear in repo contents |
| Repo commit metadata (author email, timestamps, signing keys) | Restricted | Inherent in git, minimize |
| GitHub Pages-hosted content | Public by design | Brand surface |
| MTA-STS policy repos | Public, structural | Reveals domain ownership inherently |
| Private repository contents | Confidential | Compartmentalized |

## Adversaries

| Adversary | Capability | Motivation |
|---|---|---|
| **Opportunistic OSINT collector** | Low — public sources only | Doxxing, social engineering setup |
| **Competing service provider** | Medium — public + commercial OSINT | Client poaching, competitive intel |
| **Targeted attacker pivoting through identity** | Medium-High — combines GitHub OSINT with phishing, credential stuffing | Account takeover, supply-chain attack via published code |
| **Client adversary** | Variable — interested in supplier-of-supplier intel | Identifying MSP → client relationships to expand attack surface |
| **Social engineer** | Low capability, high payoff | Pretexting based on disclosed work patterns and personal interests |

## Attack Surface Inventory

### Surface 1: Profile metadata
- Display name, bio, profile email, location, company, blog
- Public repository list (cannot be hidden if repos are public)
- Public gist list
- Followers / following (relationship graph)
- Contribution graph (work pattern + timezone fingerprint)

### Surface 2: Repository contents
- README and documentation
- Code (including comments, debug strings, commit messages)
- Issues and pull requests (titles, bodies, labels)
- Image and document assets (EXIF, embedded metadata)
- Release artifacts (binaries with author metadata)

### Surface 3: Git history
- Author name + email on every commit
- GPG/SSH signing keys
- Commit timestamps (timezone fingerprint, work pattern)
- Past content that has been "deleted" but remains in history
- Co-authored-by trailers

### Surface 4: Account-linked external assets
- GitHub Pages hosted content
- MTA-STS policy repositories (prove domain ownership)
- DNS records pointing to GitHub infrastructure
- Linked third-party services (apps, OAuth grants)

## Threats and Mitigations

### T1 — Identity correlation across personas
**Threat:** Adversary correlates multiple email addresses, brand names, and domains to build a unified identity graph.
**Mitigation:** Single contact email across all public surfaces. Single brand name. Domains used for personal vs operational purposes are not cross-referenced in public repos.

### T2 — Employer / client relationship disclosure
**Threat:** Adversary identifies the employer or clients an MSP operator serves, enabling targeted attacks against those downstream organizations.
**Mitigation:** Public repos do not name specific employers, clients, or client domains. Code, screenshots, and examples use placeholder identifiers. Repo names do not reference internal organizations.

### T3 — Credential exposure via commit
**Threat:** Secrets committed to a public repo, even in old history, are scraped within seconds of push.
**Mitigation:** Pre-commit secret scanning (`gitleaks`, `trufflehog`). GitHub push protection enabled. Branch protection on default branches. Any exposed credential is rotated within 1 hour and history rewritten.

### T4 — EXIF / metadata leakage via image and document assets
**Threat:** Image EXIF reveals camera, location, software, account; PDF metadata reveals author and creation tool; Canva PNG `caBX` chunks reveal design account links.
**Mitigation:** All committed media is scrubbed of metadata. CI check enforces metadata-free media on PRs.

### T5 — Timezone and work-pattern fingerprinting
**Threat:** Commit timestamp distribution reveals working hours and timezone, narrowing physical location and routine.
**Mitigation:** Accepted residual risk. Brand surface inherently identifies country. Sub-country narrowing is bounded.

### T6 — Cert progression disclosure
**Threat:** Publishing in-progress or retake status signals skill gaps to social engineers and recruiters with adversarial intent.
**Mitigation:** Only held certifications appear in public documentation. Study and retake status is private.

### T7 — Home lab / personal infrastructure mapping
**Threat:** Documented personal infrastructure (firewall vendor, VLAN layout, hostnames) provides an attack map.
**Mitigation:** Lab documentation is framed as reference architecture using placeholder values, not deployed infrastructure. See OSINT-HYGIENE.md for the soft-caution standard.

### T8 — Repository name leakage
**Threat:** Repo names containing employer abbreviations, client names, or product codenames disclose relationships before a reader even opens the repo.
**Mitigation:** Repo names are descriptive of function (`m365-assessment-framework`), not entity-specific (`acme-corp-tool`).

### T9 — Stale public repos
**Threat:** Old public repos retain pre-policy content (real configs, screenshots, names) in history even after current `main` is sanitized.
**Mitigation:** Quarterly review of public repo history. Repos that cannot be retroactively sanitized are archived or deleted with care taken to delete via the API to invalidate caches.

### T10 — MTA-STS structural disclosure
**Threat:** MTA-STS hosting repos inherently prove domain ownership. Linking multiple personal/operational domains via shared hosting account exposes the identity graph.
**Mitigation:** Accepted for operational/brand domains. Personal-name domains are reviewed for whether public ownership disclosure is desired.

## Residual Risks (Accepted)

- Country-level location disclosure
- Held certification disclosure
- Brand identity disclosure
- Public repo enumeration via profile page
- Timezone inference from commit metadata
- Domain ownership disclosure for operational MTA-STS

## Review Cadence

This threat model is reviewed:
- On every new public repository created
- On any change to held certifications, brand identity, or employer relationships
- Quarterly as a baseline check
- Immediately following any disclosure incident
