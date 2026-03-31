# PassAudit

A command-line tool for auditing password policies and rating password strength. Built in Python.

## What it does

PassAudit gives you four modes:

- **Policy Analysis** - Feed it your org's password policy parameters and it scores them against NIST guidelines, calculates entropy, and flags what's weak.
- **Password Rating** - Coming soon.
- **Password Rating (Bulk)** - Coming soon.
- **Password Entropy Calculation** - Coming soon.

## How to run it

```bash
python Main.py
```

No dependencies outside the standard library. Just `math`.

## Policy Analysis

This is the only mode that works right now. It takes your policy parameters interactively:

- Minimum length
- Character classes in use (uppercase, lowercase, numbers, special chars)
- Password expiry duration (months)
- Whether passwords are checked against breach databases
- Whether MFA is mandatory

It then calculates entropy from those inputs, scores your policy across each dimension, and prints what passes and what doesn't. The output tells you exactly what's weak and why, not just that something failed.

The scoring isn't arbitrary. It's grounded in NIST SP 800-63B, which is the current standard for password policy in most security contexts.

## NIST baseline (what the tool checks against)

- Minimum length of 8, with 15+ recommended
- All alphanumeric and special characters should be allowed
- Passwords should be screened against known breach lists
- MFA should be mandatory (or at least available)
- No security questions
- No dictionary words or repeated characters

## What's next

Password Rating and Bulk Rating are stubbed out. Entropy Calculation mode is also pending. These will fill in as the project grows.

---

Made by Yash.
