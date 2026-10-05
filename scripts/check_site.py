"""Validate the public sample and stamp the actual deployment source when on CI."""
import json
import os
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
site = root/'site'
html = (site/'index.html').read_text(encoding='utf-8')
metadata_path = site/'version.json'
metadata = json.loads(metadata_path.read_text(encoding='utf-8'))
assert metadata['version'] == 'lesson48-v1'
assert '<html lang="en">' in html and 'name="viewport"' in html
assert 'id="version">'+metadata['version'] in html
assert 'id="commit"' in html and "fetch('version.json')" in html
assert 'https://' not in html, 'This self-contained sample needs no external resource.'
assert set(p.name for p in site.iterdir()) == {'index.html', 'version.json'}
head = os.environ.get('GITHUB_SHA')
if head:
    assert re.fullmatch('[0-9a-f]{40}', head)
    metadata['source_commit'] = head
    metadata_path.write_text(json.dumps(metadata, indent=2)+'\n', encoding='utf-8')
print('Site validation passed: '+metadata['version'])
print('Source commit: '+metadata['source_commit'])
