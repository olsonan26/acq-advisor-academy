import subprocess,zipfile,json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
paths=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
archive=root.parent/'ACQ_Advisor_Academy_App.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for name in paths:
  if name:z.write(root/name,'acq-advisor-academy/'+name)
 bundle=root.parent/'ACQ_Advisor_Academy.git.bundle'
 if bundle.exists():z.write(bundle,'acq-advisor-academy/ACQ_Advisor_Academy.git.bundle')
print('Application archive:',archive)
print('SHA256:',hashlib.sha256(archive.read_bytes()).hexdigest())
