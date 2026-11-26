const host = document.querySelector('[data-specimen]');
const poster = host?.querySelector('[data-specimen-poster]');
if (host && poster) {
    const controls = host.querySelector('[data-specimen-controls]');
    const cellButton = host.querySelector('[data-specimen-cell]');
    const svg = document.createElementNS(NS, 'svg');
    const title = document.createElementNS(NS, 'title');
    const body = document.createElementNS(NS, 'g');
    const defs = document.createElementNS(NS, 'defs');
    defs.innerHTML = spriteDefinition(MATERIALS);
    svg.setAttribute('width', WIDTH);
    svg.setAttribute('height', HEIGHT);
    svg.setAttribute('viewBox', `0 0 ${WIDTH} ${HEIGHT}`);
    svg.setAttribute('data-specimen-scene', '');
    svg.setAttribute('role', 'img');
    svg.setAttribute('tabindex', '0');
    svg.setAttribute('aria-keyshortcuts', 'ArrowLeft ArrowRight ArrowUp ArrowDown');
    svg.style.touchAction = 'pan-y';
    svg.append(title, defs, body);
    const models = [null, crystal(STRUCTURE, 1), crystal(STRUCTURE, 2)];
    let repeat = 2;
    let [yaw, tilt] = HOME;
    let frame = 0;

    function paint() {
        frame = 0;
        const description = repeat === 1 ? 'PaMnF₆ single cell, eight sites' : 'PaMnF₆ repeated two cells along each lattice vector, 64 sites';
        title.textContent = description;
        svg.setAttribute('aria-label', description + '. Use arrow keys to rotate.');
        body.innerHTML = show(scene(models[repeat], repeat, yaw, tilt));
    }

    function update() {
        if (!frame) frame = requestAnimationFrame(paint);
    }

    function turn(horizontal, vertical) {
        yaw = (yaw + horizontal) % (Math.PI * 2);
        tilt = Math.min(1.42, Math.max(-1.42, tilt + vertical));
        update();
    }

    const directions = {
        left: [-.16, 0], right: [.16, 0], up: [0, .16], down: [0, -.16],
    };
    for (const button of host.querySelectorAll('[data-specimen-turn]')) {
        const direction = directions[button.dataset.specimenTurn];
        if (direction) button.addEventListener('click', () => turn(...direction));
    }
    host.querySelector('[data-specimen-reset]')?.addEventListener('click', () => {
        [yaw, tilt] = HOME;
        update();
    });
    cellButton?.addEventListener('click', () => {
        repeat = repeat === 2 ? 1 : 2;
        cellButton.setAttribute('aria-pressed', String(repeat === 1));
        update();
    });
    svg.addEventListener('keydown', event => {
        if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
        if (!event.key.startsWith('Arrow')) return;
        const direction = directions[event.key.slice(5).toLowerCase()];
        if (!direction) return;
        event.preventDefault();
        turn(...direction);
    });

    let pointer;
    svg.addEventListener('pointerdown', event => {
        if (!event.isPrimary || event.button !== 0) return;
        pointer = { id:event.pointerId, x:event.clientX, y:event.clientY };
        svg.setPointerCapture(event.pointerId);
    });
    svg.addEventListener('pointermove', event => {
        if (event.pointerId !== pointer?.id) return;
        const dx = event.clientX-pointer.x;
        const dy = event.clientY-pointer.y;
        pointer.x = event.clientX;
        pointer.y = event.clientY;
        turn(dx*.010, event.pointerType === 'touch' ? 0 : -dy*.010);
    });
    for (const type of ['pointerup', 'pointercancel', 'lostpointercapture']) {
        svg.addEventListener(type, event => {
            if (pointer?.id === event.pointerId) pointer = undefined;
        });
    }

    paint();
    poster.after(svg);
    poster.hidden = true;
    if (controls) controls.hidden = false;
}
