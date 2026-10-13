# Access and deployment

## Practice now on this computer

Open [the local academy](http://127.0.0.1:3000) or [the completed demonstrations](http://127.0.0.1:3000/review). The local preview is running when handed off; if the app or computer restarts, launch it again using the commands below.

```powershell
cd acq-advisor-academy
corepack enable
pnpm install --frozen-lockfile
Copy-Item .env.example .env.local
pnpm dev
```

Requires Node.js 24 and pnpm 11.25.0. If Corepack is not available with your Node installation, install pnpm using its official instructions, then continue with `pnpm install`.

The example configuration uses `ACADEMY_LOCAL_DEMO=true` for local-only practice. No AI or Supabase credential is needed for the guided exercises and device progress. Do not set that demo flag on a public deployment.

## Deploy from your own Vercel dashboard

Repository: [olsonan26/acq-advisor-academy](https://github.com/olsonan26/acq-advisor-academy). It is public at the user's explicit request.

1. Sign in to [Vercel](https://vercel.com/new) with your own account and select the account/team where you have project-creation permission.
2. Choose **Import Git Repository** and select `olsonan26/acq-advisor-academy`. If it is missing, authorize the Vercel GitHub integration for this repository. Do not import or replace another application.
3. Project name: `acq-advisor-academy` if available; framework: **Next.js**; root directory: repository root; Node.js: **24.x**.
4. Install command: `pnpm install --frozen-lockfile`. Build command: `pnpm build`. Let Next.js choose its output directory.
5. Add the server environment variable `ACADEMY_ACCESS_PASSWORD` with a long unique value. Keep it secret. Leave `ACADEMY_LOCAL_DEMO` unset. The deployed application fails closed without access configuration.
6. Optional AI: add `AI_GATEWAY_API_KEY` as a server secret and `AI_MODEL` as a current supported gateway model ID. Without them, feedback remains guided and explicitly labeled.
7. Optional cloud progress: choose a dedicated Supabase project, apply `database/schema.sql`, configure email redirect URLs, and add `NEXT_PUBLIC_SUPABASE_URL` plus `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`. Never expose a service-role key. Device persistence works without this setup.
8. Click **Deploy**. Open the returned URL, confirm that the password gate appears, sign in, and complete a financial drill. Reload My Performance to verify persistence. Complete a founder diagnosis and check its feedback. The review page should show the three labeled completed demonstrations without adding them to your own history.

## Why the agent did not deploy

The connected Vercel account could list projects but denied `POST /v11/projects` with HTTP `403 forbidden` in scope `the selected account scope`, team ID `the selected team`. Its teams and Git-deployment-context responses were empty. The error identifies denied project creation, but does not establish whether the underlying cause is role permissions, connector grants, or stale authentication. No existing production project was changed.

A successful GitHub push does not itself confirm a Vercel deployment. No hosted academy URL is claimed until Vercel actually returns a successful deployment and the resulting site is tested.

## ZIP and commit-history fallback

The ZIP contains tracked source, configuration templates, tests, instructions, completed demonstration records/screenshots, and a Git bundle. It excludes installed packages, generated build output, local environment files, original source-pack binaries, passwords, tokens, and real API secrets. Test files contain explicitly fake test fixtures, not account credentials.

To recover the complete commit history from the bundle:

```powershell
git clone ACQ_Advisor_Academy.git.bundle acq-advisor-academy-with-history
cd acq-advisor-academy-with-history
git remote set-url origin https://github.com/olsonan26/acq-advisor-academy.git
```

To push an existing local checkout to this dedicated repository, use a normal authenticated GitHub login and a non-forced push. Do not paste a token into the remote URL.

The build machine's normal Git push required an unavailable GitHub sign-in. Publication uses the authenticated connector instead; exact original history is retained in the local ZIP bundle, not uploaded publicly or represented as the publication branch's native ancestors. See `HISTORY.md` for the distinction and recovery steps.
