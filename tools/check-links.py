from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'site').resolve()
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for key in ('href','src'):
   if key in d:self.links.append((tag,d[key]))
errors=[];counts=0
for path in root.rglob('*.html'):
 parser=Links();parser.feed(path.read_text())
 for tag,raw in parser.links:
  u=urlsplit(raw)
  if u.scheme or u.netloc or not u.path:continue
  route=unquote(u.path)
  if route.startswith('/edgetx.github.io/'):target=root/route[len('/edgetx.github.io/'):]
  elif route.startswith('/'):target=root/route[1:]
  else:target=path.parent/route
  if target.is_dir():target=target/'index.html'
  counts+=1
  if not target.exists():errors.append((str(path.relative_to(root)),raw))
print('Local targets checked:',counts)
for row in sorted(set(errors)): print(*row,sep=' -> ')

if errors: raise SystemExit(1)
print("All local links and assets resolve.")
