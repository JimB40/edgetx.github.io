"""Check that every generated HTML page opts out of search indexing."""
from pathlib import Path
from html.parser import HTMLParser
import sys
class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.protected = False
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "meta" and values.get("name", "").lower() == "robots":
            self.protected |= "noindex" in values.get("content", "").lower()
root = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
pages = list(root.rglob("*.html"))
assert pages, "No built HTML pages found"
failures = []
for path in pages:
    parser = MetaParser()
    parser.feed(path.read_text())
    if not parser.protected:
        failures.append(str(path))
assert not failures, "Missing noindex: " + ", ".join(failures)
assert "Disallow: /" in (root / "robots.txt").read_text()
print(f"Preview indexing protection verified on {len(pages)} pages")
