# ACQ Advisor Academy

Independent interview preparation for October 19, 2026 at 2:00 PM Pacific (3:00 PM Mountain). Not affiliated with Acquisition.com. A working Next.js / TypeScript / Tailwind application, with optional server-side AI and Supabase progress.

## Run locally

Use Node.js 24 and pnpm 11.25.0. From this directory:

```powershell
corepack enable
pnpm install --frozen-lockfile
Copy-Item .env.example .env.local
pnpm dev
```

Open `http://127.0.0.1:3000`. The supplied example enables a local-only demo. Device progress, lessons, financial exercises, guided founder interviews, case assessment, and interview rehearsal require no third-party credentials.

For an optimized local build:

```powershell
pnpm build
pnpm start
```

Keep `.env.local` private. Do not deploy with `ACADEMY_LOCAL_DEMO=true`.

## What is included

- 32 lessons across nine learning tracks, each with explanations, calculations or investigations, source distinctions, common mistakes, and a graded check.
- Six-day October 13–18 preparation plan and the correct interview countdown.
- 20 financial exercises, three selectable difficulty levels, an optional timer, worked corrections, and saved accuracy history.
- 15 fictional founder businesses with bespoke hidden evidence, seven-step diagnostic workbooks, calculations, answer keys released after submission, and weighted educational feedback.
- Seven mock-screening rounds totaling 60 minutes, 20 extra practice questions, feedback, revised answer examples, and optional browser speech recognition.
- Device-persistent completion, drafts, answers, scores, and practice history; JSON export.
- Source inventory of 75 official lesson pages, 87 parsed PowerPoint slides (83 visible), and two fully read supplied recruitment transcripts.
- Optional live AI coaching through Vercel AI Gateway; optional Supabase email sign-in and per-user cloud progress.
- Private production password gate with signed expiring cookies, protected layouts, and API checks. Production fails closed without access configuration.

## Teaching and source boundaries

SPS is grounded in the supplied original Business Re-Imagined presentation, especially slides 42–44. Principles and exercises cite the relevant slide numbers. Slide 5's exact Georgia store figures are preserved; calculated comparisons are labeled as derived and no cause is invented.

Recruitment practice uses the supplied Advisory Practice and Careers transcripts. Those are user-supplied transcriptions with approximate text timestamps, possible transcription errors, and unverified video mapping. No independently verified video timestamps are claimed.

All four official course libraries were visited. `data/sources.json` records the observed menu titles, exact URLs, order, access status, available resource links, and caption-discovery results. The 75 linked lesson pages and player metadata were inspected. No subtitle tracks were found in the accessible public manifests, and no spoken video teaching has been analyzed. Every such lesson is flagged **transcript needed**. Related business explanations are labeled supplemental rather than attributed to unviewed videos. The inventory is the observed public linked set, not a claim that undiscoverable/gated lessons cannot exist.

The original source pack is preserved locally under `references/source-pack/` and is excluded from Git and the shareable application archive. `data/slides.json` is an extraction for provenance tests, not a replacement for full visual rendering. Embedded assets from the image-only slides were inspected, but full slide render verification remains unfinished.

## Feedback: what is genuinely working

The financial lab checks exact arithmetic. Founder answers use a fixed evidence ledger, which prevents invented business facts. Case and interview feedback includes worked corrections, missing evidence, competing-hypothesis prompts, execution requirements, and a stronger spoken answer.

The default evaluator is a transparent text checklist. Its numerical answers are checked, but keyword-based reasoning checks cannot establish semantic correctness, live communication, actual humility, or hiring readiness. The interface explicitly labels this limit. Live AI, when configured and successfully called, adds qualitative feedback grounded in the authored content and case evidence; a failed provider call falls back visibly to guided feedback.

Preparation weights: business reasoning 25%, financial accuracy 20%, diagnosis 20%, communication 15%, practical execution 10%, collaboration/coachability 10%. These are not official Acquisition.com hiring weights.

## Enable live AI

Set the following **server-only** environment values in `.env.local` or Vercel's project settings:

```text
AI_GATEWAY_API_KEY=<configure privately in the environment>
AI_MODEL=<a currently available gateway model ID>
```

Select a current model from the [AI Gateway model catalog](https://ai-gateway.vercel.sh/v1/models). Do not place these variables behind a `NEXT_PUBLIC_` prefix or commit secrets. The installed AI SDK's bundled documentation was checked for `generateText`, `gateway`, and the options used.

Verification after configuration: ask the professor a question, verify that its badge says **Live AI professor**, then submit a case and confirm **Live AI feedback received** appears. Without an actual successful response, this feature is not considered verified. No key or model was available in the build environment, so live AI has not been tested.

## Enable Supabase cloud progress

1. Choose or create a dedicated Supabase academy project. No existing remote database was modified in this build.
2. Apply `database/schema.sql` in its SQL editor. It creates only the progress table, enables RLS, and restricts every operation to the authenticated row owner.
3. Set `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`. Never expose a service-role/secret key.
4. Configure the local and deployed app origins as allowed auth redirect URLs and enable email sign-in.
5. Use the email sign-in form on My Performance. Verify saved progress from a second browser and test that another user cannot read it.

Device persistence is tested. Supabase cloud sign-in, RLS in a real database, and cross-device synchronization remain unverified until a dedicated project is configured. Local progress may be replaced by an existing cloud profile on sign-in; export first if preserving a device-only history matters.

## GitHub and Vercel deployment

The local project has its own Git repository and commit. Do not replace an unrelated existing project or repository. The user selected the dedicated public repository olsonan26/acq-advisor-academy. Original source-pack binaries and transcripts are excluded from Git.

1. Use the dedicated repository [olsonan26/acq-advisor-academy](https://github.com/olsonan26/acq-advisor-academy). Do not use an unrelated production repository.
2. Push this local repository to that repository:

```powershell
git remote add origin https://github.com/olsonan26/acq-advisor-academy.git
git push -u origin main
```

3. In Vercel, select the intended account/team, choose **Add New → Project**, and import that repository. Framework: Next.js; repository root: this project root; install: `pnpm install --frozen-lockfile`; build: `pnpm build`; Node.js: 24.x. Do not select one of your unrelated production projects.
4. Set `ACADEMY_ACCESS_PASSWORD` to a long, unique secret in both preview and production. Leave `ACADEMY_LOCAL_DEMO` unset. Add AI and Supabase values only if ready to enable those services.
5. Deploy, then verify that unauthenticated requests reach the access page and that the correct password permits lessons and API workflows. Repeat the finance → saved history and case → assessment workflows on the deployment.

The current build has **no live Vercel URL**. Exact blocker:

```text
Account link: the selected Vercel account
Operation: POST /v11/projects
HTTP: 403 forbidden
Scope: the selected account scope
Team ID: the selected team
Message: Not authorized: Trying to access resource under that scope.
The API asks for re-authentication to that scope or a token with access.
```

The connector could list projects, but its teams and Git deployment context were empty. No dedicated Vercel academy project was found. The user subsequently provided the empty academy GitHub repository with push permission; only that dedicated repository is used. A Vercel CLI was not installed and the standard local CLI credential paths were absent, so there was no authenticated CLI fallback. The error does not reveal whether the missing access is a role, connector scope, or stale credential; it is specifically the create-project operation that failed. No production deployment or existing project was changed.

## Validation

```powershell
pnpm typecheck
pnpm test
pnpm build
```

The browser suite uses Playwright and a browser executable. Install Playwright in your test environment or point `WORKSPACE_NODE_MODULES` at a directory containing it; set `TEST_BROWSER_PATH` to your Chromium/Edge executable; run `node scripts/browser-test.cjs` against the local server. The suite uses a fresh browser profile and does not erase your real progress.

See `VERIFICATION.md` for completed checks and remaining gaps. Optional microphone behavior depends on browser support and permission and was not verified by speaking into a microphone.

## Remaining work

- Restore deployment permission or authorize a dedicated academy repository/project, then deploy and verify.
- Configure and test live AI and Supabase cloud persistence.
- Obtain precise official lesson transcripts/captions; analyze teaching before adding source-attributed frameworks, examples, exceptions, and timestamps.
- Supply the Director of Business Workshops job posting, résumé, and verified history to personalize defensible leadership stories.
- Fully render and inspect the original PowerPoint, especially image-only slides.
- Add broader course coverage and stronger model-assisted evaluations after the initial interview sprint.

## Completed demonstrations and direct deployment guide

Open /review for three actual UI-completed demonstrations, their submissions, numerical results, corrections, and screenshots. They are labeled examples and are not added to personal progress. See DEMONSTRATIONS.md for a portable record and DEPLOY.md for exact GitHub/Vercel dashboard steps.
