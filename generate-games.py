import os, re

base = os.path.dirname(__file__)
with open(os.path.join(base, 'docs/game.html'), 'r', encoding='utf-8') as f:
    template = f.read()

GAME_IDS = [
    'pokepath-td', 'knee-deep', 'twilight-observer', 'death-loop',
    'summon-a-sweetheart', 'contract-demon', '10-minutes-dawn', 'heartstop-tour',
    'cupids-kiss', 'mindmindmind', 'my-husband-stranger', 'sweetest-valentine',
    'honey-dress-up', 'witch-you-want', 'under-the-thorns', 'abo-speed-dating',
    'penultima', 'snow-white-vn', 'evil-witch-cursed', 'gravity-failed-us',
    'silver-thread-deux', 'myosotis', 'stranger-bus-stop', 'purarger-collector',
    'honey-trap-burned', 'guidelicious', 'hauoli', 'intertwine',
    'sweet-valentine-chocolatier', 'lovebyte-demo'
]

for gid in GAME_IDS:
    html = template

    # Fix internal links to root
    html = html.replace('href="index.html"', 'href="/"')

    # Fix related card links
    html = html.replace(
        "location.href='game.html?id=${g.id}'",
        "location.href='/games/'+g.id+'/'"
    )

    # Replace URL param reading with hardcoded ID
    html = html.replace(
        "const params = new URLSearchParams(window.location.search);\nconst gameId = params.get('id');",
        f"const gameId = '{gid}';"
    )

    out_dir = os.path.join(base, 'docs/games', gid)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created: games/{gid}/index.html')

print(f'\nDone! Generated {len(GAME_IDS)} game pages.')
