"""Bundle editable static HTML/CSS/images into one portable HTML file."""
from pathlib import Path
import base64,re
root=Path(__file__).parent
source=root/'slides'
html=(source/'index.html').read_text(encoding='utf8')
assert len(re.findall(r'<section\b',html))==7, 'Keep exactly seven slide sections.'
html=html.replace('<link rel="stylesheet" href="static.css">','<style>'+(source/'static.css').read_text(encoding='utf8')+'</style>')
def image(match):
    file=source/match.group(1)
    mime='image/svg+xml' if file.suffix=='.svg' else 'image/png'
    return '"data:'+mime+';base64,'+base64.b64encode(file.read_bytes()).decode()+'"'
html=re.sub(r'"(assets/[^\"]+\.(?:png|svg))"',image,html)
(root/'ArgoTwin-Pitch.html').write_text(html,encoding='utf8')
print('Built ArgoTwin-Pitch.html. Editable slide source is unchanged.')
