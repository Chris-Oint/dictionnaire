#!/usr/bin/env python3
"""Build a reproducible candidate inventory; candidates are not validated definitions."""
from __future__ import annotations
import gzip, hashlib, json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path('/home/ubuntu/work/brochure-app/data/brochures_z1.json.gz')
METADATA = Path('/home/ubuntu/work/research/zone1/app-meta.json')
OUT = ROOT / 'data/zone1-passage-inventory.jsonl'
SUMMARY = ROOT / 'data/zone1-passage-inventory-summary.json'

# Broad recall is intentional: every row is a candidate requiring human/source review.
NUM = re.compile(r'\b(?:zéro|zero|numéro\s+un|chiffre\s+un|nombre\s+un|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|quatorze|quinze|seize|dix-sept|dix-huit|dix-neuf|vingt|trente|quarante|cinquante|soixante|cent|mille|premier|première|deuxième|troisième|quatrième|huitième|\d{1,4})\b', re.I)
MEANING = re.compile(r'\b(?:signifi\w*|veut dire|veulent dire|ça veut dire|cela veut dire|le sens de|littéralement|défin\w*|est appelé\w*|désign\w*|représent\w*|symbol\w*|type de|antitype|figure de|préfigur\w*|est l’image|est une image|est le chiffre|est le nombre)\b', re.I)
PATTERNS = {
    'mots_noms': re.compile(r'\b(?:le mot|ce mot|le terme|ce terme|le nom|ce nom|son nom|signification du mot|littéralement)\b', re.I),
    'phrases_adages': re.compile(r'\b(?:proverbe\w*|adage\w*|dicton\w*|expression\w*|idiome\w*|phrase signifie|expression signifie|on dit que|dit le proverbe)\b', re.I),
    'symboles': re.compile(r'\b(?:symbole\w*|symbolis\w*|représent\w*|signifie|figure de|en est l’image|image de|emblème)\b', re.I),
    'types_antitypes': re.compile(r'\b(?:un type de|le type de|est le type|est un type|type de|antitype\w*|préfigur\w*|ombre de|figure de)\b', re.I),
    'paraboles': re.compile(r'\b(?:parabole\w*|parabolique|vierges sages|fils prodigue|bon samaritain|semeur|grain de sénevé|talents)\b', re.I),
    'animaux': re.compile(r'\b(?:lion\w*|agneau\w*|aigle\w*|serpent\w*|dragon\w*|colombe\w*|ours\w*|léopard\w*|bouc\w*|bélier\w*|taureau\w*|cheval\w*|sauterelle\w*|scorpion\w*|renard\w*|loup\w*|brebis\w*|chèvre\w*|poisson\w*|baleine\w*|corbeau\w*|pigeon\w*|bête\w*)\b', re.I),
}

def main():
    metadata = json.loads(METADATA.read_text(encoding='utf-8'))
    by_doc = {int(row['doc_index']): row for row in metadata}
    with gzip.open(CORPUS, 'rt', encoding='utf-8') as f:
        corpus = json.load(f)
    totals = Counter(); docs_seen = set(); rows = 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', encoding='utf-8') as out:
        for doc_index, doc in enumerate(corpus['docs']):
            meta = by_doc.get(doc_index)
            if not meta or doc[0] != meta['code']:
                raise ValueError(f'metadata alignment error at doc_index={doc_index}')
            docs_seen.add(doc_index)
            for paragraph, text in doc[4]:
                categories = []
                if NUM.search(text) and MEANING.search(text): categories.append('nombres')
                if PATTERNS['mots_noms'].search(text) and MEANING.search(text): categories.append('mots_noms')
                if PATTERNS['phrases_adages'].search(text): categories.append('phrases_adages')
                if PATTERNS['symboles'].search(text): categories.append('symboles')
                if PATTERNS['types_antitypes'].search(text): categories.append('types_antitypes')
                if PATTERNS['paraboles'].search(text): categories.append('paraboles')
                if PATTERNS['animaux'].search(text) and (MEANING.search(text) or PATTERNS['types_antitypes'].search(text)):
                    categories.append('animaux')
                if not categories: continue
                anchor = MEANING.search(text)
                if anchor is None:
                    anchor = next((p.search(text) for p in PATTERNS.values() if p.search(text)), None)
                start = max(0, (anchor.start() if anchor else 0) - 100)
                excerpt = text[start:start + 320].strip()
                record = {
                    'etat': 'candidat_a_verifier',
                    'doc_index': doc_index,
                    'app_index': int(meta['app_index']),
                    'code': meta['code'], 'edition': meta['edition'],
                    'brochure': meta['title'], 'date': meta['date'],
                    'paragraphe': int(paragraph),
                    'categories_candidates': categories,
                    'extrait_candidat': ('…' if start else '') + excerpt + ('…' if start + 320 < len(text) else ''),
                    'empreinte_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()
                }
                out.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')
                totals.update(categories); rows += 1
    report = {
        'source': str(CORPUS), 'documents_examines': len(docs_seen),
        'paragraphes_examines': sum(len(doc[4]) for doc in corpus['docs']),
        'paragraphes_candidats_uniques': rows,
        'candidats_par_famille': dict(sorted(totals.items())),
        'statut': 'Candidats automatiques uniquement; aucun candidat ne devient une définition sans vérification source.'
    }
    SUMMARY.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))

if __name__ == '__main__': main()
