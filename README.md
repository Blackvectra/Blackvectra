<p align="center">
  <img src="branding/logo.svg" alt="NextLayerSec Logo" width="600"/>
</p>

<h1 align="center">Matthew Levorson</h1>

<p align="center">
  <i>Security Engineer • MSP Security Operations • Blue Team</i><br>
  <i>Email Security • Identity • Microsoft Security Stack • DNS Hardening</i>
</p>

<p align="center">
  <i>ISC2 CC | CompTIA A+ | Network+ | Security+ | Linux+</i><br>
  <br><i>SSCP • CySA+ • AZ-500 (in progress)</i><br>
</p>

---

### Professional Links

<p align="center">
  <a href="https://nextlayersec.io">
    <img src="https://img.shields.io/badge/Website-nextlayersec.io-black?style=for-the-badge&logo=firefox"/>
  </a>
  <a href="https://linkedin.com/in/matthewlevorson">
    <img src="https://img.shields.io/badge/LinkedIn-Matthew%20Levorson-black?style=for-the-badge&logo=linkedin"/>
  </a>
  <a href="mailto:mlevorson@nextlayersec.io">
    <img src="https://img.shields.io/badge/Email-mlevorson%40nextlayersec.io-black?style=for-the-badge&logo=microsoftoutlook"/>
  </a>
</p>

---

## Professional Summary

Security Engineer at NRG Technology Services (MSP) and founder of NextLayerSec LLC,
an independent cybersecurity consulting practice focused on email security, endpoint
protection, M365 hardening, and threat intelligence.

My work emphasizes:
- Production-validated security controls -- not lab exercises
- Defense in depth across email, identity, DNS, and endpoint
- Repeatable frameworks adaptable for MSP client delivery
- Documentation that supports auditability, handoff, and scale

---

## Active Projects

### NextLayerSec Email Security Framework
Complete email security hardening framework deployed across multiple domains under
a single M365 Business Premium tenant. Every control implemented and validated in production.

[![SPF](https://img.shields.io/badge/SPF-Enforced-00c853?style=flat-square)]()
[![DKIM](https://img.shields.io/badge/DKIM-Active-00c853?style=flat-square)]()
[![DMARC](https://img.shields.io/badge/DMARC-p%3Dreject-00c853?style=flat-square)]()
[![MTA-STS](https://img.shields.io/badge/MTA--STS-Enforced-00c853?style=flat-square)]()
[![DNSSEC](https://img.shields.io/badge/DNSSEC-Enabled-00c853?style=flat-square)]()

**Controls deployed:**
- SPF, DKIM, DMARC `p=reject` across all domains
- MTA-STS enforce mode via GitHub Pages hosting
- DNSSEC + DNSSEC-aware M365 MX endpoints
- TLS-RPT reporting configured
- Full Exchange Online hardening via PowerShell

**Repos:** [nextlayersec-email-security](https://github.com/Blackvectra/nextlayersec-email-security) |
[nextlayersec-mta-sts](https://github.com/Blackvectra/nextlayersec-mta-sts) |
[nextlayersec-dev-mta-sts](https://github.com/Blackvectra/nextlayersec-dev-mta-sts) |
[blackvectra.github.io](https://github.com/Blackvectra/blackvectra.github.io)

---

### M365 Security Baseline Tool
PowerShell script that runs a comprehensive security baseline check against any M365
Business Premium tenant. 30+ controls across legacy auth, transport hardening, Defender
policies, audit logging, and email authentication. Color-coded pass/fail terminal output
with optional CSV export. No configuration required -- runs against any connected tenant.

**Repo:** [nextlayersec-m365-hardening](https://github.com/Blackvectra/nextlayersec-m365-hardening)

---

### Email Security Assessment Tool
Domain assessment script that checks the full email security stack via public DNS lookups.
No tenant access required. Checks SPF, DKIM, DMARC, MTA-STS, DNSSEC, TLS-RPT, BIMI,
and CAA records against any domain. Detects mail provider, DNSSEC-aware MX endpoints,
and enforcement levels.

**Repo:** [nextlayersec-m365-hardening](https://github.com/Blackvectra/nextlayersec-m365-hardening)

---

## Tools & Platforms

**Microsoft Security Stack**

<p>
  <img src="https://img.shields.io/badge/Microsoft%20365-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Defender%20for%20Endpoint-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Defender%20for%20Office%20365-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Microsoft%20Intune-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Entra%20ID-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Exchange%20Online-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
</p>

**Operations & Investigation**

<p>
  <img src="https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white"/>
  <img src="https://img.shields.io/badge/ConnectWise%20RMM-grey?style=flat-square"/>
  <img src="https://img.shields.io/badge/Sysinternals-0078D4?style=flat-square&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark"/>
  <img src="https://img.shields.io/badge/CyberChef-000000?style=flat-square"/>
</p>

**Email Security**

<p>
  <img src="https://img.shields.io/badge/DMARCian-grey?style=flat-square"/>
  <img src="https://img.shields.io/badge/MXToolbox-grey?style=flat-square"/>
  <img src="https://img.shields.io/badge/Cloudflare%20DNS-F38020?style=flat-square&logo=cloudflare&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub%20Pages-181717?style=flat-square&logo=github"/>
</p>

**Offensive / Lab**

<p>
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=flat-square&logo=kalilinux"/>
  <img src="https://img.shields.io/badge/Nmap-grey?style=flat-square"/>
  <img src="https://img.shields.io/badge/Burp%20Suite-FF6600?style=flat-square&logo=burpsuite&logoColor=white"/>
</p>

---

## GitHub Activity

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=blackvectra&show_icons=true&theme=github_dark"/>
  <br>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=blackvectra&theme=github-dark"/>
</p>

---

## Current Focus

- Email security hardening framework -- production deployment across 3 domains
- M365 tenant hardening automation via Exchange Online PowerShell
- SSCP retake preparation -- Domain 3 (Risk Identification, Monitoring, and Analysis)
- CySA+ and AZ-500 cert progression
- NextLayerSec service framework development

---

## Frameworks & Standards

NIST CSF 2.0 | NIST SP 800-53 | MITRE ATT&CK | CIS Controls v8 | ISO/IEC 27001 | RFC 8461 | RFC 7489

---

<p align="center">
  <b>Matthew Levorson</b> • <a href="https://nextlayersec.io">nextlayersec.io</a> • <a href="mailto:mlevorson@nextlayersec.io">mlevorson@nextlayersec.io</a>
</p>
