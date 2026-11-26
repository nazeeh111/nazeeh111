'use strict';

// This file also forms the dependency-free browser runtime.
const WIDTH = 720;
const HEIGHT = 510;
const HOME = [3.085, -1.125];
const RADII = { Pa: 0.92, Mn: 0.75, F: 0.57 }; // Display only, in scene units.
const NS = 'http://www.w3.org/2000/svg';

function cartesian(fractional, lattice) {
    return [0, 1, 2].map(axis =>
        fractional.reduce((total, coefficient, index) => total + coefficient * lattice[index][axis], 0));
}

function projection(point, yaw, tilt) {
    const u = Math.cos(yaw) * point[0] - Math.sin(yaw) * point[1];
    const v = Math.sin(yaw) * point[0] + Math.cos(yaw) * point[1];
    return [u, Math.cos(tilt) * point[2] - Math.sin(tilt) * v,
        Math.sin(tilt) * point[2] + Math.cos(tilt) * v];
}

function crystal(structure, repeat) {
    const atoms = [];
    for (let i = 0; i < repeat; ++i) {
        for (let j = 0; j < repeat; ++j) {
            for (let k = 0; k < repeat; ++k) {
                for (const { element, frac } of structure.sites) {
                    atoms.push({element, point: cartesian([frac[0] + i, frac[1] + j, frac[2] + k], structure.lattice)});
                }
            }
        }
    }
    const center = [0, 1, 2].map(axis =>
        (Math.min(...atoms.map(atom => atom.point[axis])) + Math.max(...atoms.map(atom => atom.point[axis]))) / 2);
    const origin = point => point.map((value, axis) => value - center[axis]);
    for (const atom of atoms) atom.point = origin(atom.point);

    // Outer cell edges only. Splitting each line handles atom occlusion in the painter's pass.
    const edges = [];
    const parts = 18;
    for (let axis = 0; axis < 3; ++axis) {
        const other = [0, 1, 2].filter(index => index !== axis);
        for (const sideA of [0, repeat]) {
            for (const sideB of [0, repeat]) {
                const start = [0, 0, 0];
                start[other[0]] = sideA;
                start[other[1]] = sideB;
                for (let part = 0; part < parts; ++part) {
                    start[axis] = part * repeat / parts;
                    const a = origin(cartesian(start, structure.lattice));
                    start[axis] = (part + 1) * repeat / parts;
                    const b = origin(cartesian(start, structure.lattice));
                    edges.push([a, b]);
                }
            }
        }
    }
    return { atoms, edges };
}

function scene(geometry, repeat, yaw, tilt) {
    const rot = point => projection(point, yaw, tilt);
    const points = geometry.atoms.map(({element, point}) => ({kind:'atom', element, p:rot(point)}));
    const shape = geometry.edges.map(pair => {
        const [a, b] = pair.map(rot);
        return {kind:'edge', a, b, z:(a[2]+b[2])/2};
    });
    // Keep a fixed target zoom, backing away only when a rotation would clip the scene.
    const extent = [0, 1].map(axis => Math.max(
        ...shape.flatMap(({a, b}) => [Math.abs(a[axis]), Math.abs(b[axis])]),
        ...points.map(({p, element}) => Math.abs(p[axis]) + RADII[element]),
    ));
    const scale = Math.min(repeat === 1 ? 55 : 35, 330 / extent[0], 229 / extent[1]);
    for (const {element, p} of points) {
        shape.push({kind:'atom', element, p, r:RADII[element]*scale, z:p[2]});
    }
    shape.sort((a, b) => a.z - b.z);
    return {
        shape,
        x: value => WIDTH/2 + scale * value,
        y: value => HEIGHT/2 - scale * value,
    };
}

function spriteDefinition(materials) {
    return Object.entries(materials).map(([element, uri]) =>
        `<image id="sphere-${element}" width="1" height="1" href="${uri}"/>`).join('');
}

function simplify(value) {
    return Math.round(value * 1000) / 1000;
}

function show({shape, x, y}) {
    const coord = (fn, value) => simplify(fn(value));
    return shape.map(item => {
        if (item.kind === 'edge') {
            const a = item.a, b = item.b;
            const opacity = Math.max(.07, Math.min(.31, .13 + item.z * .013));
            return `<path d="M${coord(x,a[0])},${coord(y,a[1])}L${coord(x,b[0])},${coord(y,b[1])}" fill="none" stroke="#b8a7c5" stroke-width="1" stroke-opacity="${simplify(opacity)}" stroke-linecap="round"/>`;
        }
        const {element, p, r, z} = item;
        // Distant sites retain their color identity with a shallow depth cue.
        const brightness = Math.max(.79, Math.min(1, .91 + z * .014));
        const px = simplify(x(p[0])-r), py = simplify(y(p[1])-r);
        return `<use href="#sphere-${element}" data-element="${element}" filter="brightness(${simplify(brightness)})" transform="translate(${px},${py}) scale(${simplify(2*r)})"/>`;
    }).join('');
}

if (typeof module === 'object') {
    module.exports = {WIDTH, HEIGHT, HOME, RADII, cartesian, projection, crystal, scene, spriteDefinition, show};
}
