# PassAudit

A command-line Python tool that checks password policies and rates password strength.

## What It Does

PassAudit is built around four modes. 

| Mode | Description |
|---|---|
| Policy Analysis | Scores your policy parameters against NIST guidelines, calculates entropy, and flags what is weak. |
| Password Rating | Coming soon. |
| Password Rating (Bulk) | Coming soon. |
| Password Entropy Calculation | Coming soon. |

## How To Run It

```bash
python Main.py
```

It only uses the standard Python library, so there is nothing to install.

## Policy Analysis

This mode asks you for your policy parameters interactively. It needs the minimum length, what character classes you require, the password expiry duration, whether you check against breach databases, and whether MFA is mandatory.

It uses those inputs to calculate entropy and score your policy. The output prints exactly what fails and why, instead of just giving a pass or fail grade. The scoring relies on NIST SP 800-63B. 

## The NIST Baseline

The tool checks your inputs against the NIST baseline. It looks for an 8-character minimum length, though 15 or more is recommended. It checks that all alphanumeric and special characters are allowed and that passwords are screened against known breach lists. It also looks for mandatory MFA, no security questions, and no dictionary words or repeated characters.

## What Is Next

The password rating, bulk rating, and entropy calculation modes are stubbed out right now. They will be added as the project grows.

---

Made by Yash.
