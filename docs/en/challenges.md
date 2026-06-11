# Challenge Mode - English

Challenge Mode helps learners practice actively instead of only reading solutions. Use the `/scoreboard` page to track your progress during a local session.

## C01 - Missing Admin Authorization

**Goal:** Check whether a normal user can access the admin page.

Hints:

1. Log in to the vulnerable app as `alice / alice123`.
2. Visit `/admin`.
3. Record the result.
4. Repeat the same action on the secure app.

Expected observation:

- The vulnerable app allows a normal user to access admin functionality.
- The secure app returns `403 Forbidden`.

## C02 - Login SQL Injection

**Goal:** Compare unsafe SQL query construction with parameterized login handling.

Hints:

1. Review `vulnerable-app/app.py` and find the login query.
2. Compare it with `secure-app/app.py`.
3. Use the behavioral tests as evidence that the vulnerable and secure versions behave differently.

## C03 - Search Input Handling

**Goal:** Observe how the search box handles user input.

Hints:

1. Search for normal product keywords.
2. Try special input in the local lab.
3. Compare vulnerable and secure behavior.

Learning note:

- When user input is rendered inside normal page text, unsafe output may become reflected XSS.
- When the same input is rendered inside an HTML attribute such as `value="..."`, unsafe output may become attribute injection.
- Context matters: the right fix is context-aware escaping and avoiding `safe` on user input.

## C04 - Profile IDOR

**Goal:** Check whether a user can view another user's profile.

Hints:

1. Log in as `alice`.
2. Open `/profile`.
3. Try changing the `id` query parameter.
4. Compare the behavior with the secure app.

## C05 - CSRF Settings Update

**Goal:** Understand why state-changing requests should require CSRF protection.

Hints:

1. Log in as `alice`.
2. Open `/settings` in both apps.
3. Compare the form markup and server-side logic.
4. Observe that the secure app requires a CSRF token before updating the email value.

## C06 - Evidence Report

**Goal:** Generate a Markdown finding from structured evidence.

Hints:

1. Open one file in `examples/`.
2. Run the report generator.
3. Compare the generated report with `reports/sample-pentest-report.md`.
