#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages tutoriels/*.html à partir d'un template partagé.

Usage : python3 tool/build_tutorials.py (depuis la racine du repo).
Régénère tous les fichiers sous tutorials/ — à relancer après toute
modification de STUDIOS ou du TEMPLATE ci-dessous, puis committer le diff.
"""

import os

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tutorials")

STUDIOS = [
    {
        "slug": "dessin",
        "name_fr": "Dessin",
        "name_en": "Drawing",
        "desc_fr": "Brosses crayon, encre, feutre, pastel, gravure. Pression du stylet, calques, palm rejection.",
        "desc_en": "Pencil, ink, marker, pastel and engraving brushes. Pen pressure, layers, palm rejection.",
        "icon": '''<path fill="var(--accent)" d="M 10.00 55.04 L 11.29 51.84 L 12.66 48.95 L 14.11 46.36 L 15.64 44.08 L 17.24 42.09 L 18.89 40.39 L 20.59 38.96 L 22.30 37.81 L 24.03 36.89 L 25.75 36.20 L 27.46 35.71 L 29.16 35.40 L 30.85 35.23 L 32.52 35.17 L 34.21 35.22 L 35.90 35.33 L 37.62 35.50 L 39.37 35.71 L 41.15 35.93 L 42.98 36.16 L 44.85 36.40 L 46.75 36.68 L 48.69 36.98 L 50.65 37.30 L 52.64 37.62 L 54.65 37.93 L 56.68 38.21 L 58.74 38.44 L 60.81 38.59 L 62.91 38.61 L 65.01 38.49 L 67.10 38.22 L 69.18 37.79 L 71.22 37.21 L 73.22 36.45 L 75.16 35.54 L 77.03 34.45 L 78.83 33.20 L 80.55 31.79 L 82.21 30.21 L 83.80 28.46 L 85.34 26.53 L 86.84 24.40 L 88.31 22.06 L 89.76 19.50 L 91.19 16.69 L 92.61 13.61 L 94.00 10.24 L 94.00 10.24 L 92.59 13.60 L 91.10 16.64 L 89.54 19.37 L 87.90 21.79 L 86.20 23.91 L 84.45 25.73 L 82.66 27.28 L 80.85 28.55 L 79.03 29.57 L 77.22 30.36 L 75.43 30.94 L 73.65 31.34 L 71.90 31.59 L 70.15 31.71 L 68.42 31.72 L 66.68 31.66 L 64.92 31.53 L 63.15 31.37 L 61.34 31.18 L 59.51 30.98 L 57.63 30.77 L 55.73 30.51 L 53.80 30.21 L 51.85 29.90 L 49.88 29.58 L 47.89 29.26 L 45.88 28.97 L 43.86 28.71 L 41.82 28.53 L 39.77 28.47 L 37.71 28.55 L 35.65 28.76 L 33.62 29.13 L 31.62 29.65 L 29.67 30.32 L 27.78 31.16 L 25.96 32.16 L 24.22 33.32 L 22.56 34.65 L 20.97 36.13 L 19.46 37.77 L 18.00 39.59 L 16.60 41.60 L 15.23 43.80 L 13.88 46.23 L 12.57 48.90 L 11.27 51.83 L 10.00 55.04 Z"/>''',
    },
    {
        "slug": "vectoriel",
        "name_fr": "Vectoriel",
        "name_en": "Vector",
        "desc_fr": "Aplats, silhouettes, logos, pictogrammes. Formes propres et opérations booléennes.",
        "desc_en": "Flats, silhouettes, logos, pictograms. Clean shapes and boolean operations.",
        "icon": '''<line x1="18" y1="47" x2="30" y2="12" stroke="var(--accent)" stroke-width="1" opacity="0.45"/>
          <line x1="84" y1="17" x2="70" y2="52" stroke="var(--accent)" stroke-width="1" opacity="0.45"/>
          <path d="M18 47 C30 12 70 52 84 17" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" fill="none"/>
          <circle cx="18" cy="47" r="3.4" fill="var(--card)" stroke="var(--accent)" stroke-width="1.4"/>
          <circle cx="84" cy="17" r="3.4" fill="var(--card)" stroke="var(--accent)" stroke-width="1.4"/>
          <rect x="27.5" y="9.5" width="5" height="5" fill="var(--accent)"/>
          <rect x="67.5" y="49.5" width="5" height="5" fill="var(--accent)"/>''',
    },
    {
        "slug": "pixel-art",
        "name_fr": "Pixel art",
        "name_en": "Pixel art",
        "desc_fr": "Grille de cellules, outils dédiés, résolution et palette maîtrisées.",
        "desc_en": "Cell grid, dedicated tools, resolution and palette under control.",
        "icon": '''<g fill="var(--accent)">
            <rect x="38" y="8" width="9" height="9"/><rect x="47" y="8" width="9" height="9"/>
            <rect x="29" y="17" width="9" height="9"/><rect x="38" y="17" width="9" height="9" fill-opacity="0.35"/><rect x="47" y="17" width="9" height="9" fill-opacity="0.35"/><rect x="56" y="17" width="9" height="9"/>
            <rect x="29" y="26" width="9" height="9"/><rect x="38" y="26" width="9" height="9"/><rect x="47" y="26" width="9" height="9"/><rect x="56" y="26" width="9" height="9"/>
            <rect x="38" y="35" width="9" height="9"/><rect x="47" y="35" width="9" height="9"/>
            <rect x="29" y="44" width="9" height="9"/><rect x="56" y="44" width="9" height="9"/>
            <rect x="20" y="53" width="9" height="9"/><rect x="65" y="53" width="9" height="9"/>
          </g>''',
    },
    {
        "slug": "generatif",
        "name_fr": "Génératif",
        "name_en": "Generative",
        "desc_fr": "Fractales, motifs, formes procédurales. Une amorce, une graine, une composition.",
        "desc_en": "Fractals, motifs, procedural shapes. A seed, a rule, a composition.",
        "icon": '''<g fill="var(--accent)">
            <path d="M50 6 L58 20 L42 20 Z" fill-opacity="0.85"/>
            <path d="M34 32 L42 20 L26 20 Z" fill-opacity="0.6"/>
            <path d="M66 32 L74 20 L58 20 Z" fill-opacity="0.6"/>
            <path d="M50 32 L58 20 L42 20 Z" fill-opacity="0.35"/>
            <path d="M18 58 L26 46 L10 46 Z" fill-opacity="0.45"/>
            <path d="M50 58 L58 46 L42 46 Z" fill-opacity="0.45"/>
            <path d="M82 58 L90 46 L74 46 Z" fill-opacity="0.45"/>
          </g>''',
    },
    {
        "slug": "montage",
        "name_fr": "Montage",
        "name_en": "Montage",
        "desc_fr": "Assemblage de plans, bande-son, export — la table de montage du carnet.",
        "desc_en": "Assembling clips, soundtrack, export — the notebook's editing bench.",
        "icon": '''<rect x="10" y="26" width="80" height="14" rx="4" fill="var(--accent)" fill-opacity="0.18"/>
          <rect x="14" y="28" width="22" height="10" rx="3" fill="var(--accent)" fill-opacity="0.55"/>
          <rect x="40" y="28" width="18" height="10" rx="3" fill="var(--accent)" fill-opacity="0.75"/>
          <rect x="62" y="28" width="14" height="10" rx="3" fill="var(--accent)"/>
          <line x1="58" y1="14" x2="58" y2="50" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/>
          <path d="M54 14 L62 14 L58 22 Z" fill="var(--accent)"/>''',
    },
    {
        "slug": "animation",
        "name_fr": "Animation",
        "name_en": "Animation",
        "desc_fr": "Image par image, onion skin, FPS variable, rig 2D pour les poses.",
        "desc_en": "Frame by frame, onion skin, variable FPS, 2D rig for posing.",
        "icon": '''<circle cx="30" cy="34" r="17" fill="var(--accent)" fill-opacity="0.16"/>
          <circle cx="42" cy="30" r="17" fill="var(--accent)" fill-opacity="0.38"/>
          <circle cx="56" cy="34" r="17" fill="var(--accent)" fill-opacity="0.92"/>''',
    },
    {
        "slug": "bd",
        "name_fr": "BD",
        "name_en": "Comics",
        "desc_fr": "Planches multi-cases, bulles, onomatopées, lignes de vitesse.",
        "desc_en": "Multi-panel pages, speech bubbles, sound effects, speed lines.",
        "icon": '''<rect x="12" y="8" width="76" height="22" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.8"/>
          <rect x="12" y="36" width="34" height="20" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.8"/>
          <rect x="54" y="36" width="34" height="20" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="var(--accent)" stroke-width="1.8"/>''',
    },
]

TEMPLATE = '''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atelier — {name_fr}</title>
<style>
  :root {{
    color-scheme: light dark;
    --accent: #4F7CA8;
    --accent-ink: #3A5E80;
    --shell: #F3F0EA;
    --on-shell: #2A2724;
    --on-shell-muted: #6B655D;
    --card: #FFFCF7;
    --on-card: #2A2724;
    --card-border: rgba(42,39,36,0.10);
    --canvas: #F7F4EF;
    --focus-ring: #4F7CA8;
  }}

  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --accent: #E27C50;
      --accent-ink: #F0A17C;
      --shell: #3A322C;
      --on-shell: #F2EAE2;
      --on-shell-muted: #C9BFB4;
      --card: #453B33;
      --on-card: #F2EAE2;
      --card-border: rgba(242,234,226,0.12);
      --canvas: #4E443C;
      --focus-ring: #F0A17C;
    }}
  }}

  :root[data-theme="dark"] {{
    --accent: #E27C50;
    --accent-ink: #F0A17C;
    --shell: #3A322C;
    --on-shell: #F2EAE2;
    --on-shell-muted: #C9BFB4;
    --card: #453B33;
    --on-card: #F2EAE2;
    --card-border: rgba(242,234,226,0.12);
    --canvas: #4E443C;
    --focus-ring: #F0A17C;
  }}

  * {{ box-sizing: border-box; }}

  @font-face {{
    font-family: 'Kalam';
    font-weight: 700;
    font-style: normal;
    font-display: swap;
    src: local('Kalam Bold'), local('Kalam-Bold');
  }}

  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    color: var(--on-shell);
    background: var(--shell);
    line-height: 1.6;
  }}

  a {{ color: var(--accent-ink); }}
  a:focus-visible, button:focus-visible {{
    outline: 2px solid var(--focus-ring);
    outline-offset: 2px;
    border-radius: 4px;
  }}

  .page {{
    max-width: 620px;
    margin: 0 auto;
    padding: 2rem 1.25rem 4.5rem;
  }}

  header.top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 2.5rem;
  }}

  .brand {{
    display: flex;
    align-items: center;
    gap: 0.65rem;
    text-decoration: none;
    color: inherit;
  }}

  .brand-mark {{
    width: 68px;
    height: 40.8px;
    flex: none;
  }}

  .brand-name {{
    font-family: 'Kalam', -apple-system, sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
  }}

  .back-link {{
    font-size: 0.88rem;
    color: var(--on-shell-muted);
    text-decoration: none;
  }}
  .back-link:hover {{ color: var(--on-shell); }}

  .studio-hero {{
    background: var(--card);
    color: var(--on-card);
    border: 1px solid var(--card-border);
    border-radius: 16px;
    padding: 2rem 1.75rem;
    box-shadow: 0 8px 22px -12px rgba(0,0,0,0.35), 0 1px 4px rgba(0,0,0,0.10);
    margin-bottom: 2rem;
  }}

  .studio-hero-icon {{
    width: 96px;
    height: 62px;
    margin-bottom: 1rem;
  }}

  h1 {{ font-size: 1.5rem; margin: 0 0 0.4rem; text-wrap: balance; }}
  .lead {{ color: var(--on-shell-muted); margin: 0 0 0; max-width: 52ch; }}

  .status-pill {{
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    padding: 0.3rem 0.7rem;
    border-radius: 999px;
    background: color-mix(in srgb, var(--accent) 16%, transparent);
    color: var(--accent-ink);
    margin-bottom: 1.1rem;
  }}
  .status-pill::before {{
    content: "";
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent);
  }}

  .cta-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
  }}
  .cta {{
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-weight: 600;
    font-size: 0.92rem;
    padding: 0.65rem 1.1rem;
    border-radius: 999px;
    background: var(--accent);
    color: #FFFCF7;
    text-decoration: none;
  }}
  .cta.secondary {{
    background: transparent;
    color: var(--on-shell);
    border: 1px solid var(--card-border);
  }}

  [data-lang-content] {{ display: none; }}
  [data-lang-content].active {{ display: block; }}

  .lang-switch {{
    display: flex;
    gap: 0.4rem;
  }}
  .lang-switch button {{
    font: inherit;
    font-size: 0.82rem;
    padding: 0.32rem 0.7rem;
    border-radius: 999px;
    border: 1px solid var(--card-border);
    background: transparent;
    color: var(--on-shell-muted);
    cursor: pointer;
  }}
  .lang-switch button[aria-current="true"] {{
    background: var(--card);
    color: var(--on-card);
    font-weight: 600;
  }}
</style>
</head>
<body>
<div class="page">

<header class="top">
  <a class="brand" href="../index.html">
    <svg class="brand-mark" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <defs>
        <linearGradient id="brand-mark-gradient" x1="0%" y1="50%" x2="100%" y2="50%">
          <stop offset="0%" stop-color="var(--on-shell)"/>
          <stop offset="100%" stop-color="var(--accent)"/>
        </linearGradient>
      </defs>
      <path fill="url(#brand-mark-gradient)" d="M 16.00 98.40 L 18.58 92.83 L 21.33 87.82 L 24.24 83.35 L 27.32 79.43 L 30.52 76.05 L 33.84 73.17 L 37.24 70.79 L 40.69 68.88 L 44.17 67.40 L 47.66 66.31 L 51.15 65.57 L 54.65 65.12 L 58.15 64.92 L 61.66 64.93 L 65.21 65.11 L 68.79 65.42 L 72.44 65.83 L 76.14 66.29 L 79.93 66.79 L 83.79 67.27 L 87.74 67.78 L 91.75 68.36 L 95.81 68.98 L 99.93 69.62 L 104.10 70.25 L 108.31 70.86 L 112.55 71.41 L 116.83 71.89 L 121.15 72.21 L 125.50 72.28 L 129.86 72.09 L 134.20 71.64 L 138.52 70.91 L 142.78 69.89 L 146.96 68.57 L 151.05 66.95 L 155.03 65.03 L 158.88 62.81 L 162.60 60.28 L 166.20 57.44 L 169.68 54.29 L 173.06 50.81 L 176.35 46.99 L 179.58 42.79 L 182.75 38.18 L 185.88 33.14 L 188.97 27.63 L 192.00 21.60 L 192.00 21.60 L 188.93 27.61 L 185.72 33.04 L 182.35 37.91 L 178.86 42.21 L 175.24 45.96 L 171.54 49.19 L 167.76 51.90 L 163.95 54.13 L 160.12 55.92 L 156.30 57.29 L 152.49 58.29 L 148.70 58.97 L 144.93 59.38 L 141.17 59.56 L 137.42 59.54 L 133.65 59.38 L 129.86 59.11 L 126.03 58.76 L 122.16 58.36 L 118.23 57.96 L 114.25 57.52 L 110.22 56.99 L 106.16 56.41 L 102.07 55.78 L 97.95 55.14 L 93.81 54.51 L 89.65 53.92 L 85.47 53.37 L 81.28 52.97 L 77.07 52.80 L 72.87 52.85 L 68.69 53.15 L 64.55 53.72 L 60.47 54.55 L 56.48 55.66 L 52.60 57.06 L 48.85 58.74 L 45.25 60.72 L 41.79 62.98 L 38.50 65.54 L 35.34 68.39 L 32.32 71.55 L 29.40 75.03 L 26.58 78.87 L 23.84 83.09 L 21.16 87.72 L 18.54 92.81 L 16.00 98.40 Z"/>
    </svg>
    <span class="brand-name">Atelier</span>
  </a>
  <nav class="lang-switch">
    <button type="button" data-set-lang="fr" aria-current="true">Français</button>
    <button type="button" data-set-lang="en" aria-current="false">English</button>
  </nav>
</header>

<div data-lang-content="fr" class="active">
  <a class="back-link" href="../index.html">&larr; Retour aux ressources</a>

  <div class="studio-hero" style="margin-top:1.25rem">
    <svg class="studio-hero-icon" viewBox="0 0 100 64" aria-hidden="true">
      {icon}
    </svg>
    <span class="status-pill">Tutoriel à venir</span>
    <h1>{name_fr}</h1>
    <p class="lead">{desc_fr}</p>
  </div>

  <p class="lead">
    Le tutoriel du studio {name_fr} est en préparation. En attendant, vous
    pouvez explorer l'outil directement dans l'application, ou nous écrire si
    vous avez une question précise.
  </p>

  <div class="cta-row">
    <a class="cta" href="mailto:jeromehouix@gmail.com?subject=Question%20{name_fr}">Poser une question</a>
    <a class="cta secondary" href="../index.html">Voir les autres studios</a>
  </div>
</div>

<div data-lang-content="en">
  <a class="back-link" href="../index.html">&larr; Back to resources</a>

  <div class="studio-hero" style="margin-top:1.25rem">
    <svg class="studio-hero-icon" viewBox="0 0 100 64" aria-hidden="true">
      {icon}
    </svg>
    <span class="status-pill">Tutorial coming soon</span>
    <h1>{name_en}</h1>
    <p class="lead">{desc_en}</p>
  </div>

  <p class="lead">
    The {name_en} studio tutorial is being written. In the meantime, feel
    free to explore the tool directly in the app, or write to us with any
    specific question.
  </p>

  <div class="cta-row">
    <a class="cta" href="mailto:jeromehouix@gmail.com?subject=Question%20{name_en}">Ask a question</a>
    <a class="cta secondary" href="../index.html">See other studios</a>
  </div>
</div>

</div>

<script>
(function () {{
  var LANG_KEY = 'atelier-privacy-lang';
  var buttons = document.querySelectorAll('[data-set-lang]');
  var panels = document.querySelectorAll('[data-lang-content]');

  var TITLES = {{
    fr: document.title,
    en: 'Atelier — {name_en}'
  }};

  function applyLang(lang) {{
    panels.forEach(function (panel) {{
      panel.classList.toggle('active', panel.getAttribute('data-lang-content') === lang);
    }});
    buttons.forEach(function (button) {{
      button.setAttribute('aria-current', String(button.getAttribute('data-set-lang') === lang));
    }});
    document.documentElement.lang = lang;
    document.title = TITLES[lang];
  }}

  buttons.forEach(function (button) {{
    button.addEventListener('click', function () {{
      var lang = button.getAttribute('data-set-lang');
      try {{ localStorage.setItem(LANG_KEY, lang); }} catch (e) {{}}
      applyLang(lang);
    }});
  }});

  var saved = null;
  try {{ saved = localStorage.getItem(LANG_KEY); }} catch (e) {{}}
  if (!saved) {{
    saved = (navigator.language || '').toLowerCase().indexOf('fr') === 0 ? 'fr' : 'en';
  }}
  applyLang(saved);
}})();
</script>

</body>
</html>
'''

os.makedirs(OUT_DIR, exist_ok=True)
for studio in STUDIOS:
    content = TEMPLATE.format(**studio)
    path = os.path.join(OUT_DIR, studio["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)
