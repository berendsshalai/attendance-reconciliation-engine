# Non-Technical Guide

## What This Project Does

The Attendance Reconciliation Engine compares two simple ideas:

1. Who was planned to work.
2. Who actually clocked in or out.

When those records do not line up, the project creates a review list. A human can then decide what happened and what should be corrected.

## What It Does Not Do

This is not payroll software. It does not decide legal compliance, calculate wages, submit payroll, or replace manager review.

## Why It Matters

Many operations teams rely on repeated spreadsheet checks. That creates risk because formulas, filters, manual notes, and copied files can drift. This project shows how that work can become structured, testable, and easier to explain.

## Fictional Example

Worker 002 was planned for a shift from 08:00 to 16:00 at Site 001. The fictional clock record shows an 08:22 clock-in and a 15:30 clock-out. The engine reports late arrival and early departure for review.

No real employee, site, payroll, or financial data is used.
