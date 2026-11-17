"""Outline licensed Bricolage Grotesque into self-contained profile covers.

Requires fontTools. Uses the bundled unchanged OFL font; no network requests.
PNG counterparts are browser renders of these exact SVGs, not edited screenshots.
"""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
import json

HERE=Path(__file__).resolve().parent
fonts={weight:instantiateVariableFont(TTFont(HERE/'fonts/BricolageGrotesque.ttf'),{'wght':weight,'wdth':85,'opsz':48},inplace=True) for weight in (500,750)}
records=[]
layouts={}

def lettering(text,x,y,size,weight,color):
    font=fonts[weight];glyphs=font.getGlyphSet();cmap=font.getBestCmap();units=font['head'].unitsPerEm;scale=size/units;position=0;pieces=[]
    for letter in text:
        name=cmap[ord(letter)];pen=SVGPathPen(glyphs);glyphs[name].draw(pen);path=pen.getCommands()
        if path:pieces.append(f'<path transform="translate({x+position*scale:.4f} {y}) scale({scale:.7f} {-scale:.7f})" d="{path}"/>')
        position+=font['hmtx'][name][0]
    records.append({'text':text,'x':x,'baseline_y':y,'font_size':size,'weight':weight,'advance_width':position*scale})
    return f'<g fill="{color}">'+''.join(pieces)+'</g>'

for dark in (False,True):
    for mobile in (False,True):
        w,h=(600,420) if mobile else (1000,340);blue='#6B8BFF' if dark else '#294FF7';ground='#101D3C' if dark else '#EDF4FF';ink='#F1F6FF' if dark else '#15203B';name_ink='#101D3C' if dark else '#FFFFFF';records=[]
        content=f'<rect width="{w}" height="{h}" fill="{blue}"/>'
        if mobile:
            content+=lettering('Nazeeh',30,104,86,750,name_ink)+lettering('Abdul-Hadi',30,198,86,750,name_ink)
            content+=f'<rect y="252" width="600" height="168" fill="{ground}"/>'
            content+=lettering('Electrical engineering',30,309,31,500,ink)+lettering('+ physics at Virginia Tech',30,356,31,500,ink)
        else:
            content+=f'<rect x="668" width="332" height="340" fill="{ground}"/>'
            content+=lettering('Nazeeh',40,139,124,750,name_ink)+lettering('Abdul-Hadi',40,267,124,750,name_ink)
            for text,y in [('Electrical',109),('engineering',147),('+ physics',204),('Virginia Tech',267)]:content+=lettering(text,702,y,33,500,ink)
        label='mobile' if mobile else 'wide';theme='dark' if dark else 'light';name=f'cover-{label}-{theme}.svg';desc='Nazeeh Abdul-Hadi. Electrical engineering and physics at Virginia Tech. Original typographic cover; no activity statistics.'
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">Nazeeh Abdul-Hadi</title><desc id="desc">{escape(desc)}</desc>{content}</svg>\n';(HERE/name).write_text(svg)
        for record in records:assert record['x']+record['advance_width']<=w-20,(name,record)
        layouts[name.removesuffix('.svg')]={'width':w,'height':h,'text':records}
(HERE/'cover-layout.json').write_text(json.dumps(layouts,indent=2)+'\n')
print('Four self-contained SVG covers; outlined type, no external resource dependency.')
