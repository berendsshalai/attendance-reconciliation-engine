# Attendance Reconciliation Engine

Reconciles planned shifts with actual attendance records and produces auditable exception reports.

## Problem Solved

Manual attendance checks often require operators to compare rostered shifts, clock events and exception notes across spreadsheets. This project provides a clean-room local engine for validating those records with synthetic examples and configurable rules.

## Capabilities

- CSV and JSON input paths.
- Deterministic synthetic demonstration.
- Planned-versus-actual reconciliation.
- Roster review against neutral coverage requirements.
- Overlapping planned shift, long shift, duplicate identifier and coverage gap detection.
- Missing clock event, absent while rostered, present while unrostered, lateness and early departure detection.
- CLI, Python API, browser demo and local stdio MCP server scaffold.
- Audit trail with rule identifiers and validation messages.

## Quick Start

```bash
python -m pip install -e .
python -m attendance_reconciliation.synthetic data/demo
python -m attendance_reconciliation.cli reconcile --shifts data/demo/shifts.csv --attendance data/demo/attendance.csv --output out/report.json
python -m attendance_reconciliation.cli review-roster --shifts data/demo/shifts.csv --coverage data/demo/coverage.csv --output out/roster-review.json
```

## Public Pages

- [Project page](https://berendsshalai.github.io/attendance-reconciliation-engine/)
- [Check My Socials](https://berendsshalai.github.io/attendance-reconciliation-engine/socials/)

The social page is part of the deployed project site and connects this repository to the creator's verified public profiles and portfolio.

## Check My Socials

<p align="center">
  <a href="https://github.com/berendsshalai"><img src="https://img.shields.io/badge/GitHub-berendsshalai-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/sha-lai-berends"><img src="https://img.shields.io/badge/LinkedIn-Sha--Lai_Berends-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn"></a>
  <a href="https://x.com/berendsshalai"><img src="https://img.shields.io/badge/X-berendsshalai-000000?style=for-the-badge&amp;logo=x&amp;logoColor=white" alt="X"></a>
  <a href="https://www.instagram.com/berendsshalai"><img src="https://img.shields.io/badge/Instagram-berendsshalai-E4405F?style=for-the-badge&amp;logo=instagram&amp;logoColor=white" alt="Instagram"></a>
  <a href="https://www.facebook.com/p/Sha-Lai-Berends-61591546301365/"><img src="https://img.shields.io/badge/Facebook-Sha--Lai_Berends-1877F2?style=for-the-badge&amp;logo=facebook&amp;logoColor=white" alt="Facebook"></a>
  <a href="https://bit.ly/3sA5312"><img src="https://img.shields.io/badge/EasyEquities-Investor_Profile-623BD3?style=for-the-badge" alt="EasyEquities"></a>
  <a href="https://sha-lai-be-2a6c6108-shalaiberends.wix-site-host.com"><img src="https://img.shields.io/badge/Portfolio-Website-061D46?style=for-the-badge&amp;logo=googlechrome&amp;logoColor=white" alt="Portfolio website"></a>
</p>

<p align="center"><strong><a href="https://berendsshalai.github.io/attendance-reconciliation-engine/socials/">Open the complete Check My Socials experience →</a></strong></p>

## Non-Technical Explanation

This repository is written for both technical and non-technical reviewers. Start with:

- `docs/NON_TECHNICAL_GUIDE.md`
- `docs/RECRUITER_BRIEF.md`
- `docs/ROSTER_SYSTEM_GUIDE.md`
- `docs/SOCIAL_MEDIA_REFERENCE.md`

## Privacy

This project uses synthetic data and neutral identifiers. It is an independent clean-room implementation and contains no private organisational source code, data, branding or proprietary documentation.

## Limitations

This is not a payroll-calculation product and does not claim legal compliance. Rates, thresholds, break rules and pay-period definitions must be configured by the user.
