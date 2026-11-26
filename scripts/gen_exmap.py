#!/usr/bin/env python3
"""Gera exmap.json: nome do exercício (como o Hevy exporta) -> [categoria FIT, código do exercício].

Uso:  pip install fit-tool && python3 scripts/gen_exmap.py
"""
import json, re
import fit_tool.profile.profile_type as P

cats = {m.name: m.value for m in P.ExerciseCategory}
out = {}
for n in sorted(dir(P)):
    if not n.endswith('ExerciseName'):
        continue
    cat = re.sub(r'(?<!^)(?=[A-Z])', '_', n[:-len('ExerciseName')]).upper()
    if cat in cats:
        for m in getattr(P, n):
            out.setdefault(m.name, [cats[cat], m.value])
out['FACE_PULL'] = [cats['ROW'], 5]  # o nome existe em várias categorias; ROW é a mais coerente
json.dump(out, open('exmap.json', 'w'), separators=(',', ':'))
print(len(out), 'exercícios gravados em exmap.json')
