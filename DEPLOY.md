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

The academy is accessible without a password in development and production. No AI or Supabase credential is needed for guided exercises and device progress.

## Existing hosted deployment

Live site: https://acq-advisor-academy.vercel.app
Repository: https://github.com/olsonan26/acq-advisor-academy

Deployment is complete. Use the existing `acq-advisor-academy` project in your Vercel dashboard; do not create a duplicate or select an unrelated application.

1. Open the live site. The academy opens without a password.
2. To update the app, publish changes to this repository's `main` branch. Its GitHub integration builds the existing Vercel project automatically.
3. In that project's settings, retain framework **Next.js**, root directory **repository root**, Node.js **24.x**, install command `pnpm install --frozen-lockfile`, build command `pnpm build`, and the default Next.js output directory.
4. Neither `ACADEMY_ACCESS_PASSWORD` nor `ACADEMY_LOCAL_DEMO` is used. You may delete those obsolete environment variables from Vercel project settings. Previews also open without a password.
5. Optional live AI: privately configure `AI_GATEWAY_API_KEY` and `AI_MODEL`, then redeploy and verify a successful live feedback badge. Guided feedback works now; live generation has not been tested.
6. Optional cross-device progress: configure a dedicated Supabase project using `database/schema.sql`, allowed auth redirect URLs, `NEXT_PUBLIC_SUPABASE_URL`, and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`. Never expose a service-role key. Device progress works now; cloud synchronization is not configured.
7. After any configuration change, redeploy the existing project. Verify anonymous dashboard access, anonymous practice API requests, a financial answer, progress after reload, founder evidence and assessment, and interview feedback.

The earlier `POST /v11/projects` request failed with HTTP `403 forbidden` under the selected account scope. The user subsequently created the dedicated academy project. Its framework was corrected from Other to Next.js, and the existing project deployed successfully. No unrelated repository or production project was changed.

## Publication history

Source was published through the authorized GitHub connector. Original local Git history remains in the local checkout; public publication commits have separate ancestry because historical documentation contains private account metadata. See `HISTORY.md`. The user canceled the ZIP request; no ZIP is required for access or deployment.
