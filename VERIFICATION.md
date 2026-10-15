# Verification record

## Public access change — October 15, 2026

The academy's custom password gate, signed access cookie, redirect, and API sign-in checks have been removed. The dashboard and `/api/practice` are intentionally accessible without an academy password. The previous access verification below is retained as historical test evidence only, not the current expected behavior. The core unit suite now has 17 tests; use `node scripts/public-access-test.cjs` against a running server to check public access.

Validated October 12, 2026 (user's Mountain time context).

## Priority workflows

| User story | Result | Evidence |
| --- | --- | --- |
| Financial lab → submitted answer → worked correction → saved progress | Passed | Correct and incorrect answers exercised through browser; stored attempts inspected; reload preserved history. |
| Founder interview → specific question → evidence ledger | Passed | Capacity and finance questions released distinct factual responses; no answer key before submission. |
| Seven-step workbook → margin/CAC → assessment → answer key → history | Passed | HVAC case submitted through all seven fields; financial category earned 20/20 for 10% margin and $200 CAC; assessment saved. |
| Interview round → response → scoring → stronger answer | Passed | Mental math round checked $30,000 / 15% / $200 / $12,000; response and feedback saved. |
| Rehearsal timer | Passed | Start and pause exercised. |
| Lesson → quiz → completion | Passed | P&L lesson opened; correct answer completed lesson; completion survived reload. |
| Tutor → grounded response | Passed in guided mode | Returned authored lesson explanation, worked numbers, transfer question, source citation, and explicit non-AI status. |
| Source library → exact lesson search | Passed | Payback Period search produced its single exact official source row. |
| Navigation | Passed | All eight routes returned HTTP 200 and displayed their headings. |
| Mobile layout | Passed | Dashboard and three priority practice routes checked at 390 × 844; no horizontal page overflow; mobile navigation opened. |
| Browser runtime | Passed | No page errors captured across exercised workflows. |
| Premature diagnosis request | Passed | API returned HTTP 400 for incomplete steps/evidence. |

The final browser suite completed 22 checks, including an additional direct-reload test for saved interview drafts. Its report and screenshots are in `test-results/` locally. That directory is not committed.

Six private-access integration checks also passed against a separate local production server: page redirect without a session, anonymous API denial, invalid password denial, valid signed-session page access, authenticated API access with explicit guided status, and tampered-session denial. Test-only credentials were not written into the project or used for production.

## Automated content and calculation checks

18 tests passed:

- Every expected financial result accepted; blank, invalid, and wrong results rejected.
- All 20 financial answers match independent arithmetic, including break-even rounding, LTV assumptions, cash flow, and exact Georgia margin rounding.
- Original PPTX has 83 visible and four hidden slides; all seven step labels appear on slides 42–44.
- Georgia sales and profit values match original slide 5.
- Every lesson has substantive teaching, a worked example, feedback, and a valid prerequisite.
- Six-day plan references valid lessons; mock rounds total 60 minutes.
- Every case has complete public economics and bespoke hidden evidence.
- Discriminating questions release the expected case-specific evidence without leaking the key.
- Case scoring rejects wrong margin/CAC and avoids counting acquisition twice.
- Interview arithmetic checks all four expected calculations.
- Ledger preserves 75 exact URLs, order, and unverified timestamps.
- Signed access cookies reject expiry or tampering.

Production build and TypeScript checks passed. Dependencies are pinned and a matching lockfile is included.

## Not verified

- Live AI generation: no model ID, gateway key, or OIDC token configured. Guided logic is tested and clearly labeled.
- Supabase sign-in, RLS enforcement on a real database, and cross-device synchronization: optional adapter and SQL are supplied; no academy database configured or existing database changed.
- Speech recognition with actual audio: optional browser interface exists; no microphone recording tested.
- Preview deployments: private access configuration is production-only; separate previews have not been tested.
- Spoken official course teaching: no public subtitle tracks located; no video claimed as watched.
- Full PowerPoint rendered-slide review: text and tables parsed from original, extraction cross-checked, selected image-only assets inspected; full rendering unfinished.
- Candidate experience and exact role requirements: résumé and job description still absent.

Default case/interview scores are a transparent educational text checklist. They are not a validated semantic evaluator or an official hiring assessment.

## Review handoff update

- Dashboard visibly distinguishes 13 lessons grounded in supplied source material, 19 supplemental lessons, and 75 official video lessons awaiting transcripts.
- Three demonstrations were completed through the interface in a separate local origin, exported through the application's progress export, and stored as labeled examples. They do not modify student progress.
- Financial payback: five months; correct answer; 100/100.
- Northline Heating: all seven SPS fields submitted; five evidence categories released; 10% margin and $200 CAC correct; 97/100, with missing accountable-owner feedback.
- Interview mental math: 95/100; submitted 20% margin corrected to 15%; financial category 15/20.
- The `/review` page was opened and checked against these actual records, including feedback and source references. Completed screenshots are under `public/demos/`.
- The core suite now has 18 passing tests; the new test verifies all seven recorded SPS steps and the two demonstrated corrections. Production build and TypeScript checks passed after the review changes.
- GitHub publishing targets only the user-provided `olsonan26/acq-advisor-academy` repository, verified empty with push permission. It is public at the user's explicit request. Production deployment was subsequently completed and verified.

## Hosted production verification

Live site: https://acq-advisor-academy.vercel.app. Vercel returned READY for the protected Next.js production deployment.

- Anonymous page redirected to `/access`; anonymous practice API returned HTTP 401.
- Existing private password signed in successfully; protected dashboard showed the 13/19/75 source distinction.
- Browser financial exercise: 80 customers × $250 = $20,000, accepted as correct. One test attempt persisted after a full reload on the hosted origin. This is a deployment test attempt, not the student's own assessment.
- Authenticated hosted founder API released the specific 75 bookings / 60 installations / 15 monthly backlog / 3% callback evidence.
- The recorded complete seven-step HVAC submission was replayed against the hosted API: 97/100, with accountable-owner correction.
- The recorded interview response was replayed against the hosted API: 95/100, with 20% margin corrected to 15%.
- Hosted responses explicitly reported guided feedback and no configured live AI.

The production password is stored outside the repository. Original source history is retained locally; public publication ancestry is separate. No ZIP is required or newly generated.
