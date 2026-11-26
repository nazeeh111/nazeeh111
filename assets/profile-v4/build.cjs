'use strict';
const fs = require('node:fs');
const {execFileSync} = require('node:child_process');
const geometry = require('./geometry.cjs');
const structure = require('./figure-data.json').initial_structure;
const materials = execFileSync('python3', ['materials.py'], {encoding:'utf8'}).trim();
const source = fs.readFileSync('geometry.cjs','utf8');
const interaction = fs.readFileSync('interaction.src.js','utf8');
fs.writeFileSync('pamnf6.js', '{\n' + source +
    '\nconst STRUCTURE = ' + JSON.stringify(structure) +
    ';\nconst MATERIALS = ' + materials + ';\n' + interaction + '\n}\n');
const {WIDTH, HEIGHT, HOME, crystal, scene, spriteDefinition, show} = geometry;
const scale = 2;
fs.writeFileSync('pamnf6.svg', `<svg xmlns="http://www.w3.org/2000/svg" width="${WIDTH}" height="${HEIGHT}" viewBox="0 0 ${WIDTH} ${HEIGHT}"><title>PaMnF₆ orthographic specimen</title><desc>64 sites from eight periodic copies of the recorded lattice; display radii are illustrative.</desc><defs>${spriteDefinition(JSON.parse(materials))}</defs><g>${show(scene(crystal(structure, scale), scale, ...HOME))}</g></svg>\n`);
