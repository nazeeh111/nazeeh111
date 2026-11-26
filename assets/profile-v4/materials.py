"""Render compact RGBA sphere textures with fixed studio lighting."""
import base64
import json
import math
import struct
import zlib

COLORS = {
    'Pa': (0.96, 0.29, 0.17),
    'F': (0.89, 0.85, 0.96),
    'Mn': (0.48, 0.23, 0.91),
}

def unit(vec):
    norm = math.sqrt(sum(x * x for x in vec))
    return tuple(x / norm for x in vec)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

LIGHTS = [
    (unit((-0.65, 0.78, 0.73)), (1, 0.86, 0.82), 0.86, 0.9, 30),
    (unit((0.88, 0.34, 0.37)), (0.61, 0.62, 1), 0.25, 0.65, 40),
    (unit((0.31, -0.85, 0.02)), (0.79, 0.49, 0.83), 0.18, 0.25, 20),
]

def png(rows, size):
    def chunk(kind, contents):
        return struct.pack('>I', len(contents)) + kind + contents + struct.pack('>I', zlib.crc32(kind + contents))
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(bytes(rows), 9)) + chunk(b'IEND', b''))

def paint(base, size=108):
    reflected = [(v, rgb, strength, gleam, power, unit((v[0], v[1], v[2]+1)))
                 for v, rgb, strength, gleam, power in LIGHTS]
    rgba = bytearray()
    radius = size / 2 - 1
    for j in range(size):
        rgba.append(0)
        for i in range(size):
            x = (i + .5 - size / 2) / radius
            y = -(j + .5 - size / 2) / radius
            radial = math.hypot(x, y)
            opacity = min(1, max(0, (1 - radial) * radius + .5))
            if opacity == 0:
                rgba.extend([0, 0, 0, 0])
                continue
            n = (x, y, math.sqrt(max(0, 1 - radial * radial)))
            # Linear-light studio shading and broad directional glints.
            albedo = [channel ** 2.2 for channel in base]
            color = [0.011 + channel * 0.12 for channel in albedo]
            for direction, chroma, strength, gleam, power, halfway in reflected:
                diffuse = max(0, dot(n, direction)) * strength
                specular = max(0, dot(n, halfway)) ** power * gleam
                for k in range(3):
                    color[k] += chroma[k] * (albedo[k] * diffuse + specular * .63)
            rim = (1 - n[2]) ** 3 * max(0, n[0] * .29 + n[1] * .17 + .07)
            for k, tint in enumerate((.37, .29, .62)):
                color[k] += rim * tint
            rgba.extend([*(int(255 * min(1, channel) ** (1 / 2.2) + .5) for channel in color), round(opacity * 255)])
    return 'data:image/png;base64,' + base64.b64encode(png(rgba, size)).decode()

print(json.dumps({element:paint(color) for element, color in COLORS.items()}, separators=(',', ':')))
