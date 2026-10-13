# Commit-history handoff

The public repository contains the application source published through the authenticated GitHub connector. Its publication commit is distinct from the original local commits.

The original local Git history is retained unmodified in the privately downloadable application ZIP as `ACQ_Advisor_Academy.git.bundle`. It is not uploaded publicly because historical documentation contains private account and deployment metadata.

To recover the original history from your local download:

```powershell
git clone ACQ_Advisor_Academy.git.bundle academy-original-history
cd academy-original-history
git log --oneline
```

The public source is directly importable into Vercel. No unrelated repository or production project was modified.
