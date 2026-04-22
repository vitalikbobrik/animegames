const fs = require('fs');
const path = require('path');

const gameHtml = fs.readFileSync(path.join(__dirname, 'docs/game.html'), 'utf8');

const GAME_IDS = [
  'pokepath-td', 'knee-deep', 'twilight-observer', 'death-loop',
  'summon-a-sweetheart', 'contract-demon', '10-minutes-dawn', 'heartstop-tour',
  'cupids-kiss', 'mindmindmind', 'my-husband-stranger', 'sweetest-valentine',
  'honey-dress-up', 'witch-you-want', 'under-the-thorns', 'abo-speed-dating',
  'penultima', 'snow-white-vn', 'evil-witch-cursed', 'gravity-failed-us',
  'silver-thread-deux', 'myosotis', 'stranger-bus-stop', 'purarger-collector',
  'honey-trap-burned', 'guidelicious', 'hauoli', 'intertwine',
  'sweet-valentine-chocolatier', 'lovebyte-demo'
];

for (const id of GAME_IDS) {
  let html = gameHtml;

  // Fix internal links to root
  html = html.replace(/href="index\.html"/g, 'href="/"');

  // Fix related card links
  html = html.replace(
    `location.href='game.html?id=\${g.id}'`,
    `location.href='/games/'+g.id+'/'`
  );

  // Replace URL param reading with hardcoded ID
  html = html.replace(
    `const params = new URLSearchParams(window.location.search);\nconst gameId = params.get('id');`,
    `const gameId = '${id}';`
  );

  const dir = path.join(__dirname, 'docs/games', id);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), html, 'utf8');
  console.log(`Created: games/${id}/index.html`);
}

console.log(`\nDone! Generated ${GAME_IDS.length} game pages.`);
