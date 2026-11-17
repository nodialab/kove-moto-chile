"""Optimiza imágenes a WebP (full 1800px + small 640px). im('archivo') -> ruta web relativa a /img."""
import glob, os, re
from PIL import Image, ImageChops

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "img")
os.makedirs(OUT, exist_ok=True)
_seen = {}


def _find(name):
    order = ("orig", "extra")
    for pre in ("extra4", "extra3", "extra2", "extra"):
        if name.startswith(pre + ":"):
            name, order = name[len(pre) + 1:], (pre,)
    for d in order:
        hits = glob.glob(os.path.join(ROOT, "assets", d, name))
        if hits:
            return hits[0]
    raise FileNotFoundError(name)


def im(name, full=1800):
    key = name
    """Devuelve (full, small, (w,h)). Acepta comodines para nombres con caracteres chinos."""
    if name in _seen:
        return _seen[name]
    src = _find(name)
    slug = re.sub(r"[^a-z0-9]+", "-", os.path.splitext(os.path.basename(src))[0].lower()).strip("-")
    # evita colisiones entre orig y extra con el mismo nombre base
    if "/extra/" in src:
        slug = "x-" + slug
    elif "/extra2/" in src:
        slug = "y-" + slug
    elif "/extra4/" in src:
        slug = "z-" + slug
    f, s = f"img/{slug}.webp", f"img/{slug}-s.webp"
    img = Image.open(src)
    img.load()
    has_a = img.mode in ("RGBA", "LA", "P") and "A" in img.convert("RGBA").getbands()
    img = img.convert("RGBA" if has_a else "RGB")
    size = img.size
    for path, w in ((f, full), (s, 640)):
        dst = os.path.join(ROOT, "site", path)
        if os.path.exists(dst):
            continue
        t = img.copy()
        if t.width > w:
            t = t.resize((w, round(t.height * w / t.width)), Image.LANCZOS)
        t.save(dst, "WEBP", quality=80 if not has_a else 84, method=4)
    _seen[name] = (f, s, size)
    return _seen[name]


def norm(name, W=1800, H=1200):
    """Recorta la moto (canal alfa) y la reencuadra igual en todos los colores: ancho 88%, centrada, apoyada en la misma base."""
    key = "n:" + name
    if key in _seen:
        return _seen[key]
    src = _find(name)
    slug = "n-" + re.sub(r"[^a-z0-9]+", "-", os.path.splitext(os.path.basename(src))[0].lower()).strip("-")
    img = Image.open(src).convert("RGBA")
    bb = img.getchannel("A").point(lambda a: 255 if a > 20 else 0).getbbox()
    if not bb or bb == (0, 0) + img.size:
        return im(name)
    c = img.crop(bb)
    k = min(W * .88 / c.width, H * .78 / c.height)
    w = round(c.width * k)
    c = c.resize((w, round(c.height * k)), Image.LANCZOS)
    out = Image.new("RGBA", (W, H))
    out.paste(c, ((W - w) // 2, round(H * .9) - c.height))
    f, s = f"img/{slug}.webp", f"img/{slug}-s.webp"
    for path, ww in ((f, W), (s, 640)):
        dst = os.path.join(ROOT, "site", path)
        t = out if ww == W else out.resize((ww, round(H * ww / W)), Image.LANCZOS)
        t.save(dst, "WEBP", quality=84, method=4)
    _seen[key] = (f, s, (W, H))
    return _seen[key]


def _rgba(path):
    img = Image.open(path)
    if "A" in img.getbands():
        return img.convert("RGBA")
    img = img.convert("RGB")  # sin alfa: el fondo blanco pasa a transparente
    r, g, b = (img.getchannel(i).point(lambda v: min(255, (255 - v) * 6)) for i in range(3))
    img = img.convert("RGBA")
    img.putalpha(ImageChops.lighter(ImageChops.lighter(r, g), b))
    return img


def norm360(names, key, W=1500, H=1000):
    """Frames de un giro 360 con escala común y base fija. Devuelve lista de rutas web."""
    if key in _seen:
        return _seen[key]
    srcs = [os.path.join(ROOT, "assets", "extra3", n) for n in names]
    ims = [_rgba(p) for p in srcs]
    bbs = [i.getchannel("A").point(lambda a: 255 if a > 20 else 0).getbbox() for i in ims]
    k = min(W * .9 / max(b[2] - b[0] for b in bbs), H * .78 / max(b[3] - b[1] for b in bbs))
    base = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
    out = []
    for n, (i, bb) in enumerate(zip(ims, bbs)):
        c = i.crop(bb)
        c = c.resize((round(c.width * k), round(c.height * k)), Image.LANCZOS)
        cv = Image.new("RGBA", (W, H))
        cv.paste(c, ((W - c.width) // 2, round(H * .9) - c.height))
        p = f"img/f360-{base}-{n + 1}.webp"
        cv.save(os.path.join(ROOT, "site", p), "WEBP", quality=82, method=4)
        out.append(p)
    _seen[key] = out
    return out
