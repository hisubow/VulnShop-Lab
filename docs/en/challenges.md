# Challenge Mode - English

Challenge Mode helps learners practice actively instead of only reading solutions.

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

## C02 - Profile IDOR

**Goal:** Check whether a user can view another user's profile.

Hints:

1. Log in as `alice`.
2. Open `/profile`.
3. Try changing the `id` query parameter.
4. Compare the behavior with the secure app.

## C03 - Search Input Handling

**Goal:** Observe how the search box handles user input.

Hints:

1. Search for normal product keywords.
2. Try special input in the local lab.
3. Compare vulnerable and secure behavior.

## C04 - Feedback Rendering

**Goal:** Check how feedback data is stored and rendered.

Hints:

1. Submit normal feedback.
2. Submit feedback containing simple HTML characters.
3. Compare how both apps render the content.

## C05 - Weak Password Storage

**Goal:** Understand why insecure password storage is a serious issue.

Hints:

1. Open the admin panel in the vulnerable app.
2. Read `vulnerable-app/app.py`.
3. Compare it with `secure-app/app.py`.
