# Publication history

The public repository contains the complete tracked application source published through the authenticated GitHub connector. Its publication commits are distinct from the original local commits.

The original local Git history remains unmodified in the original local checkout. It was not uploaded publicly because historical documentation contains private account and deployment metadata. The current public files omit that metadata and all real credentials. The user canceled the ZIP request.

Use `git log --oneline` in the original checkout to inspect retained history. Do not force-push that historical branch over the public branch.

The public source is connected to the dedicated Vercel project and deployed at https://acq-advisor-academy.vercel.app. No unrelated repository or production project was modified.
