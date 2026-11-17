import glob, html, json, os, shutil, sys, time
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from images import im, norm, norm360, ROOT
from data import *
from bgs import HERO_BG

SITE = os.path.join(ROOT, "site")
V = int(time.time())  # cache-buster de css/js
M = {m["slug"]: m for m in MODELS}
esc = html.escape


def clp(n):
    return "$" + f"{n:,}".replace(",", ".")


def img(name, cls="", alt="", R="", full=False, eager=False, attrs=""):
    f, s, (w, h) = im(name)
    src = f if full else s
    return f'<img class="{cls}" src="{R}{src}" width="{w}" height="{h}" alt="{esc(alt)}" {"" if eager else "loading=lazy"} decoding="async" {attrs}>'


def url(name, R="", full=True):
    f, s, _ = im(name)
    return R + (f if full else s)


NAV = [("modelos.html", "Modelos"), ("distribuidores.html", "Distribuidores"), ("mantenciones.html", "Mantenciones"), ("nosotros.html", "Nosotros")]


def head(title, desc, R, body_cls="", extra_head=""):
    return f"""<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0a0c0d">
<link rel="icon" href="{R}{im('icokove2025.jpg')[1]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,500;0,600;0,700;0,800;1,700;1,800&family=JetBrains+Mono:wght@500;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}css/site.css?v={V}">
{extra_head}
</head>
<body class="{body_cls}">
<a class="skip" href="#main">Saltar al contenido</a>
"""


def nav(R, active=""):
    logo = img("LOGO_KOVE_MOTO_CHILE.png", "logo", "Kove Moto Chile", R, eager=True)
    items = "".join(f'<a href="{R}{h}" class="{"on" if h == active else ""}">{t}</a>' for h, t in NAV[:1])
    mega = "".join(
        f'<a href="{R}modelos/{m["slug"]}.html" style="--ac:{m["accent"]}">{img(m["hero"], "", m["name"], R)}<span><b>{m["name"]}</b><i>{m["cat"]}</i></span></a>' for m in MODELS)
    rest = "".join(f'<a href="{R}{h}" class="{"on" if h == active else ""}">{t}</a>' for h, t in NAV[1:])
    return f"""<header class="nav" id="nav">
  <a class="brand" href="{R}index.html" aria-label="Kove Moto Chile — inicio">{logo}</a>
  <nav class="links" id="links" aria-label="Principal">
    <div class="has-mega"><a href="{R}modelos.html" class="{"on" if active == "modelos.html" else ""}">Modelos <svg width="10" height="6" viewBox="0 0 10 6"><path d="m1 1 4 4 4-4" stroke="currentColor" fill="none" stroke-width="1.6"/></svg></a>
      <div class="mega">{mega}</div></div>
    {rest}
    <a class="btn btn-sm cta-nav" href="{R}contacto.html">Cotiza tu Kove</a>
  </nav>
  <button class="burger" id="burger" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
</header>
<main id="main">
"""


def footer(R):
    logo = img("LOGO_KOVE_MOTO_CHILE.png", "logo", "Kove Moto Chile", R)
    ml = "".join(f'<a href="{R}modelos/{m["slug"]}.html">{m["name"]}</a>' for m in MODELS)
    return f"""</main>
<footer class="foot">
  <div class="foot-top">
    <div class="foot-brand">{logo}<p>Importador oficial en Chile: IMOTO S.A.</p></div>
    <div><h4>Modelos</h4>{ml}</div>
    <div><h4>Kove Chile</h4><a href="{R}distribuidores.html">Distribuidores autorizados</a><a href="{R}mantenciones.html">Mantenciones</a><a href="{R}nosotros.html">Nosotros</a><a href="{R}nosotros.html#garantias">Garantías bienes durables</a></div>
    <div><h4>Contacto</h4><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp +56 9 7579 2659</a><a href="{IG}" target="_blank" rel="noopener">Instagram</a><a href="{FB}" target="_blank" rel="noopener">Facebook</a><a href="{R}contacto.html">Formulario de cotización</a></div>
  </div>
  <div class="foot-bot"><span>© 2026 Kove Moto Chile. Sitio desarrollado por Nodialab.app.</span><span>Los datos técnicos pueden variar según mercado. Imágenes referenciales.</span></div>
</footer>
<a class="wa" href="https://wa.me/{WA}?text=Hola%2C%20quiero%20cotizar%20una%20Kove" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.2-1.200l-.3-.2-3 .8.8-2.900-.2-.3A8.200 8.200 0 1 1 12 20.200Zm4.500-6.100c-.2-.1-1.500-.7-1.700-.8-.2-.1-.4-.1-.6.100l-.8 1c-.1.200-.3.200-.5.100-1.400-.7-2.300-1.200-3.200-2.700-.2-.4.200-.4.700-1.300.1-.2 0-.3 0-.5l-.8-1.800c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.100-.7.300-.7.800-1 1.600-.9 2.600.2 1.100.7 2.200 1.800 3.400 1.500 1.700 3 2.500 4.800 2.900 1 .2 2-.1 2.600-.7.300-.3.600-1 .5-1.300 0-.2-.3-.3-.5-.4Z"/></svg></a>
<div class="lb" id="lb" hidden><button class="lb-x" aria-label="Cerrar">×</button><button class="lb-p" aria-label="Anterior">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="Siguiente">›</button></div>
<script src="{R}js/site.js?v={V}" defer></script>
</body></html>
"""


def write(path, s):
    p = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf8").write(s)


def ticker(items):
    t = "".join(f"<span>{i}</span>" for i in items)
    return f'<div class="ticker" aria-hidden="true"><div>{t}{t}</div></div>'


def model_card(m, R, lazy=True):
    price = f'<em>Desde {clp(m["price"])}</em>' if m["price"] else "<em>Consulta precio</em>"
    return f"""<a class="mcard reveal" href="{R}modelos/{m['slug']}.html" data-cat="{m['cat']}" style="--ac:{m['accent']}">
  <span class="mc-cat">{m['cat']}</span>
  {img(m['hero'], 'mc-img', m['name'] + ' Kove', R)}
  <h3>{m['name']}</h3>
  <p>{m['tagline']}</p>
  <ul><li><b>{m['stats'][0][0]}</b> {m['stats'][0][1]}</li><li><b>{m['stats'][1][0]}</b> {m['stats'][1][1]}</li><li><b>{m['stats'][2][0]}</b> {m['stats'][2][1]}</li></ul>
  <div class="mc-foot">{price}<span class="arrow">Ver modelo →</span></div>
</a>"""


def quote_form(R, preselect=""):
    opts = "".join(f'<option {"selected" if m["name"] == preselect else ""}>{m["name"]}</option>' for m in MODELS)
    return f"""<form class="quote" id="quote" data-wa="{WA}">
  <label>Nombre<input name="n" required autocomplete="name" placeholder="Tu nombre"></label>
  <label>Celular<input name="c" inputmode="tel" autocomplete="tel" placeholder="+56 9 ..."></label>
  <label>Modelo<select name="m">{opts}</select></label>
  <label>Ciudad<select name="ci"><option>Santiago</option><option>Viña del Mar</option><option>La Serena</option><option>Concepción</option><option>Otra</option></select></label>
  <button class="btn" type="submit">Cotizar por WhatsApp</button>
  <small>Abre WhatsApp con tu mensaje listo. No guardamos tus datos en este sitio.</small>
</form>"""


# ───────────────────────────── HOME ─────────────────────────────
def home():
    R = ""
    slides = "".join(f'<div class="slide{" on" if i == 0 else ""}">{img(n, "", "Kove en acción", R, eager=(i == 0), full=True)}</div>' for i, n in enumerate(HOME_HERO))
    dots = "".join(f'<button aria-label="Slide {i + 1}" class="{"on" if i == 0 else ""}"></button>' for i in range(len(HOME_HERO)))
    cards = "".join(model_card(m, R) for m in MODELS)
    terrains = [("Rally", "Rally", "450 Rally y 800X Rally, con componentes probados en el Dakar.", "800x-rally", "800X-RALLY-Gold.jpeg"),
                ("Adventure", "Adventure", "510X, 800X-PRO y 800X Touring.", "800x-touring", "800X-Touring-13-scaled.webp"),
                ("Sport", "Sport", "450RR: tetracilíndrica de 70 HP a 13.000 rpm.", "450rr", "DSC4359-scaled.jpg")]
    tiles = "".join(f"""<a class="tile reveal" href="modelos.html?cat={c}" style="--ac:{M[s]['accent']}">{img(p, '', t, R)}<div><span>{c}</span><h3>{t}</h3><p>{d}</p><b>Ver modelos →</b></div></a>"""
                    for t, c, d, s, p in terrains)
    cred = [("2017", "Nace KOVE MOTO en Chongqing, China."), ("Dakar", "Una Kove ya ganó una etapa del Dakar."), ("Mundial", "Primera moto china campeona mundial de velocidad."),
            ("Six Days", "Presencia con motos de rally en los Six Days de Enduro."), ("Europeo", "Dos títulos en el Campeonato Europeo de Rally.")]
    cr = "".join(f'<li class="reveal"><b>{a}</b><span>{b}</span></li>' for a, b in cred)
    gal = "".join(f'<a href="modelos/{m["slug"]}.html#galeria" style="--ac:{m["accent"]}">{img(m["gallery"][0], "", m["name"], R)}<span>{m["name"]}<i>Ver galería →</i></span></a>' for m in MODELS)
    s = head("Kove Moto Chile — Importador oficial IMOTO", "Motos Kove en Chile: 450RR, 450 Rally, 510X, 800X-PRO, 800X Rally y 800X Touring. Fichas técnicas, distribuidores y cotización.", R, "home")
    s += nav(R)
    s += f"""
<section class="hero-home">
  <div class="slides" id="slides">{slides}</div>
  <div class="hero-shade"></div>
  <div class="hero-copy">
    <p class="chip">Importador oficial · IMOTO S.A.</p>
    <h1>Kove llega<br>a <em>Chile</em>.</h1>
    <p class="sub">Rally, Adventure y Sport. Seis modelos 2026 y distribuidores autorizados en Santiago, La Serena, Viña del Mar y Concepción.</p>
    <div class="cta-row"><a class="btn" href="modelos.html">Explorar modelos</a><a class="btn btn-ghost" href="#financiamiento">24 cuotas sin interés</a></div>
  </div>
  <div class="hero-dots" id="dots">{dots}</div>
  <a class="scroll" href="#modelos" aria-label="Bajar">Scroll</a>
</section>
{ticker(["Ganadora de etapa en el Dakar", "Primera moto china campeona mundial de velocidad", "Más de 20.000 unidades vendidas (2021)", "Distribuidores en Santiago · La Serena · Viña · Concepción", "Hasta 95 HP", "Mantención oficial"])}
<section class="models" id="modelos">
  <div class="sec-head"><h2>Elige tu Kove</h2></div>
  <div class="rail" data-rail>{cards}</div>
  <div class="rail-hint">Desliza →</div>
</section>
<section class="terrains"><div class="sec-head"><h2>¿Dónde vas a rodar?</h2></div><div class="tiles">{tiles}</div></section>
<section class="cred">
  <div class="cred-photo">{img("LLL05102-scaled.jpg", "", "Piloto Kove en el Dakar", R)}</div>
  <div class="cred-copy"><h2>Ganar en el mundo,<br>y ahora en tu ruta.</h2><ul>{cr}</ul><a class="btn btn-ghost" href="nosotros.html">Conoce la marca</a></div>
</section>
<section class="finance" id="financiamiento">
  <div><h2>Tu moto en <em>24 cuotas</em> sin interés</h2><p>Con tarjetas de crédito Santander. Ejemplo: Kove 450 Rally, 24 cuotas de $352.500 sobre precio de lista $8.460.000. Consulta condiciones vigentes con tu distribuidor.</p><a class="btn" href="contacto.html?m=450%20Rally">Cotizar 450 Rally</a></div>
  {img("450rally-blue-1.webp", "fin-img", "Kove 450 Rally", R)}
</section>
<section class="gal-prev"><div class="sec-head"><h2>Galería por modelo</h2></div><div class="gal-tiles">{gal}</div></section>
<section class="dealers-cta"><div><h2>Distribuidores autorizados</h2><p>Santiago, La Serena, Viña del Mar y Concepción.</p><a class="btn" href="distribuidores.html">Ver distribuidores</a></div><div class="qbox"><h3>Cotiza en un minuto</h3>{quote_form(R)}</div></section>
"""
    s += footer(R)
    write("index.html", s)


# ───────────────────────────── MODELOS ─────────────────────────────
def modelos():
    R = ""
    cards = "".join(model_card(m, R) for m in MODELS)
    rows = [("Categoría", lambda m: m["cat"]), ("Cilindrada", lambda m: dict(zip(["Cilindrada"], [dict(m["specs"][0][1])["Cilindrada"]]))["Cilindrada"]),
            ("Potencia", lambda m: dict(m["specs"][0][1])["Potencia máx."]), ("Torque", lambda m: dict(m["specs"][0][1])["Torque máx."]),
            ("Peso", lambda m: dict(m["specs"][2][1]).get("Peso en orden de marcha") or dict(m["specs"][2][1]).get("Peso en vacío")),
            ("Altura de asiento", lambda m: next(v for k, v in m["specs"][2][1] if k.startswith("Altura de asiento")) + (" ¹" if m.get("seat_note") else "")), ("Estanque", lambda m: dict(m["specs"][2][1])["Estanque"]), ("Distancia entre ejes", lambda m: dict(m["specs"][2][1])["Distancia entre ejes"]),
            ("Precio lista ref.", lambda m: clp(m["price"]) if m["price"] else "Consultar")]
    th = "".join(f'<th><a href="modelos/{m["slug"]}.html">{m["name"]}</a></th>' for m in MODELS)
    tb = "".join(f"<tr><th>{lab}</th>{''.join(f'<td>{fn(m)}</td>' for m in MODELS)}</tr>" for lab, fn in rows)
    pdfs = "".join(f'<a class="pdf" href="pdf/{m["pdf"]}" download><span>PDF</span><b>Ficha {m["name"]}</b></a>' for m in MODELS)
    s = head("Modelos 2026 — Kove Moto Chile", "Compara los modelos Kove disponibles en Chile y descarga las fichas técnicas.", R, "page-models")
    s += nav(R, "modelos.html")
    s += f"""
<section class="page-hero"><h1>Modelos <em>2026</em></h1>
<div class="filters" data-filter-group><button class="on" data-f="all">Todos</button><button data-f="Rally">Rally</button><button data-f="Adventure">Adventure</button><button data-f="Sport">Sport</button></div></section>
<section class="grid-models" data-filter-target>{cards}</section>
<section class="compare"><div class="sec-head"><h2>Lado a lado</h2></div>
<div class="tbl-wrap"><table class="cmp"><thead><tr><th></th>{th}</tr></thead><tbody>{tb}</tbody></table></div>
<p class="note">Datos técnicos según fichas oficiales. Precio de lista publicado solo para el 450 Rally. ¹ Altura de asiento tomada de la ficha global de Kove (no figura en la ficha chilena).</p></section>
<section class="pdfs"><div class="sec-head"><h2>Fichas técnicas</h2></div><div class="pdf-grid">{pdfs}</div></section>
"""
    s += footer(R)
    write("modelos.html", s)


# ───────────────────────────── MODELO ─────────────────────────────
HERO_PHOTO = {"450rr": "DSC4359-scaled.jpg", "450-rally": "450Rally_desert.jpg", "800x-pro": "extra:800x-pro.png", "800x-rally": "800X-RALLY-Gold.jpeg", "800x-touring": "800X-Touring-13-scaled.webp"}


F360 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "frames360.json")))


def frames_of(m, cname, R):
    names = F360.get(m["slug"], {}).get(cname)
    return [R + p for p in norm360(names, f"{m['slug']}-{cname}")] if names else []


def hero_for(m, R):
    n, a = m["name"], m["accent"]
    fr = [frames_of(m, c[0], R) for c in m["colors"]]
    f0, _, (w0, h0) = norm(m["colors"][0][2])
    first = fr[0][0] if fr[0] else R + f0
    cut = f'<img class="cut" id="cut" src="{first}" width="{w0}" height="{h0}" alt="Kove {n}" decoding="async" data-frames="{"|".join(fr[0])}" draggable="false">'
    hint = f'<div class="spin-hint" id="spinhint"{"" if fr[0] else " hidden"}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5"/></svg>Arrastra para girar 360°</div>'
    sw = "".join(f'<button class="sw{" on" if i == 0 else ""}" style="--c:{c}" data-swap="{fr[i][0] if fr[i] else R + norm(i_)[0]}" data-frames="{"|".join(fr[i])}" aria-label="{nm}" title="{nm}"></button>' for i, (nm, c, i_) in enumerate(m["colors"]))
    swatches = f'<div class="swatches" role="group" aria-label="Color"><span>Color</span>{sw}<em id="swname">{m["colors"][0][0]}</em></div>'
    price = f'<span class="price">Precio lista ref. <b>{clp(m["price"])}</b></span>' if m["price"] else ""
    cta = f'<div class="cta-row"><a class="btn" href="#cotiza" data-quote="{n}">Cotizar {n}</a><a class="btn btn-ghost" href="../pdf/{m["pdf"]}" download>Ficha técnica PDF</a>{price}</div>'
    return f"""<section class="hero hero-ra"><div class="ra-photo">{HERO_BG[m["slug"]]}</div>
<div class="hero-copy"><p class="chip">{m['cat']}</p><h1>{n}</h1><p class="tag">{m['tagline']}</p><p class="lead">{m['lead']}</p>{swatches}{cta}</div>
<div class="hero-stage">{cut}{hint}</div>
<ol class="roadbook">{''.join(f'<li><span>{i + 1:02d}</span><b>{a_} {b_}</b><i>{c_}</i></li>' for i, (a_, b_, c_) in enumerate(m['stats']))}</ol></section>"""


def big_first(ps):
    """Las celdas grandes de la grilla (1.ª, 8.ª, 15.ª…) reciben solo fotos de ≥1400 px; las pequeñas quedan en celdas chicas."""
    hi = [p for p in ps if im(p)[2][0] >= 1400]
    lo = [p for p in ps if im(p)[2][0] < 1400]
    out = []
    while hi or lo:
        out.append(hi.pop(0) if (len(out) % 7 == 0 and hi) or not lo else lo.pop(0))
    return out


def galeria_sec(m, n, R):
    tabs = [("Fotos", m["gallery"])]
    d = detail_imgs(m)
    if d:
        tabs.append(("Detalle", d))
    btns = "".join(f'<button class="{"on" if i == 0 else ""}" data-t="{i}">{t}</button>' for i, (t, _) in enumerate(tabs))
    panels = "".join(f'<div class="gi-grid" data-lightbox data-panel="{i}"{"" if i == 0 else " hidden"}>' + "".join(
        f'<a class="gi" href="{url(p, R)}" data-full="{url(p, R)}" data-cap="{n}">{img(p, "", n + " Kove", R)}</a>' for p in big_first(ps)) + "</div>" for i, (_, ps) in enumerate(tabs))
    return f'<section class="gallery-grid" id="galeria"><div class="sec-head"><h2>Galería {n}</h2><div class="tabs" data-tabs>{btns}</div></div>{panels}</section>'


def detail_imgs(m):
    pat = EXTRA2.get(m["slug"])
    if not pat:
        return []
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "assets", "extra2", pat.replace("es_450-rally-*", "es_450-rally-2026__*")))):
        b = os.path.basename(f)
        if any(x in b for x in EXCL) or os.path.getsize(f) < 20000 or "extra2:" + b in m["carousel"] + m["gallery"]:
            continue
        try:
            Image.open(f).load()
        except Exception:
            continue
        out.append("extra2:" + b)
    return out[:16]


def model_page(m):
    R = "../"
    n = m["name"]
    slides = "".join(f'<figure class="car-slide"><a href="{url(p, R)}" data-full="{url(p, R)}" data-cap="{n}">{img(p, "", n + " Kove", R)}</a></figure>' for p in m["carousel"])
    dots = "".join(f'<button aria-label="Ir a {i + 1}"></button>' for i in range(len(m["carousel"])))
    gal = "".join(f'<a class="gi" href="{url(p, R)}" data-full="{url(p, R)}" data-cap="{n}">{img(p, "", n + " Kove", R)}</a>' for p in m["gallery"])
    feats = "".join(f"<li>{f}</li>" for f in m["features"])
    det = ""
    if m["details"]:
        det = '<section class="details"><div class="sec-head"><h2>En detalle</h2></div><div class="det-grid">' + "".join(
            f'<article class="reveal">{img(p, "", t, R)}<h3>{t}</h3><p>{d}</p></article>' for p, t, d in m["details"]) + "</div></section>"
    specs = "".join(f'<div class="spec-col"><h3>{g}</h3><dl>' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl></div>" for g, rows in m["specs"])
    seat = " ¹ La altura de asiento no figura en la ficha chilena; es el dato de la ficha global de Kove." if m.get("seat_note") else ""
    others = "".join(model_card(o, R) for o in MODELS if o["slug"] != m["slug"])
    others = others.replace('href="../modelos/', 'href="')
    s = head(f"Kove {n} — Ficha técnica, fotos y precio | Kove Moto Chile", m["lead"][:155], R, f"model t-ra t-{m['slug']}", f'<style>:root{{--ac:{m["accent"]}}}</style>')
    s += nav(R).replace(f'href="{R}contacto.html">Cotiza tu Kove', f'href="#cotiza" data-quote="{m["name"]}">Cotiza tu Kove')
    s += hero_for(m, R)
    s += f"""
<section class="gallery-car"><div class="sec-head"><h2>{n} en acción</h2></div>
<div class="carousel" data-carousel data-lightbox><div class="car-track">{slides}</div>
<button class="car-prev" aria-label="Anterior">‹</button><button class="car-next" aria-label="Siguiente">›</button><div class="car-dots">{dots}</div></div></section>
<section class="features"><div class="sec-head"><h2>Lo que trae de serie</h2></div><ul class="feat-list">{feats}</ul></section>
{det}
{galeria_sec(m, n, R)}
<section class="specs"><div class="sec-head"><h2>Especificaciones</h2><a class="btn btn-ghost" href="../pdf/{m['pdf']}" download>Descargar PDF oficial</a></div><div class="spec-cols">{specs}</div>
<p class="note">Los datos técnicos pueden modificarse según requisitos de producción y del mercado. Imágenes referenciales.{seat}</p></section>
<section class="more"><div class="sec-head"><h2>Otros modelos Kove</h2></div><div class="rail" data-rail>{others}</div></section>
<section class="dealers-cta" id="cotiza"><div class="cta-bike"><h2>Quiero una {n}</h2><p>Completa tus datos y se abre WhatsApp con tu mensaje listo.</p><img src="{R}{norm(m["colors"][0][2])[0]}" alt="Kove {n}" loading="lazy" decoding="async"></div><div class="qbox">{quote_form(R, n)}</div></section>
"""
    s += footer(R)
    write(f"modelos/{m['slug']}.html", s)


# ───────────────────────────── OTRAS ─────────────────────────────
def distribuidores():
    R = ""
    regs = ["Todas"] + sorted({d[4] for d in DEALERS}, key=lambda x: (x != "Metropolitana", x))
    f = "".join(f'<button class="{"on" if r == "Todas" else ""}" data-f="{r}">{r}</button>' for r in regs)
    cards = "".join(f"""<article class="dealer reveal" data-cat="{d[4]}"><h3>{d[0]}</h3><p>{d[1]}<br>{d[2]}, {d[3]}</p><span class="reg">{d[4]}</span>
<div><a href="tel:{''.join(c for c in d[5] if c.isdigit() or c == '+')}">{d[5]}</a>{f'<a href="mailto:{d[6]}">{d[6]}</a>' if d[6] else ''}<a class="map" target="_blank" rel="noopener" href="https://www.google.com/maps/search/{esc((d[0] + ' ' + d[1] + ' ' + d[2]).replace(' ', '+'))}">Cómo llegar →</a></div></article>""" for d in DEALERS)
    s = head("Distribuidores autorizados — Kove Moto Chile", "Encuentra tu distribuidor Kove en Santiago, La Serena, Viña del Mar y Concepción.", R, "page-dealers")
    s += nav(R, "distribuidores.html")
    s += f'<section class="page-hero"><h1>Cerca de ti,<br><em>de punta a punta.</em></h1><div class="filters" data-filter-group>{f}</div></section><section class="dealer-grid" data-filter-target>{cards}</section>'
    s += footer(R)
    write("distribuidores.html", s)


def mantenciones():
    R = ""
    th = "".join(f"<th>{c}</th>" for c in MAINT["cols"])
    tb = "".join(f"<tr><th>{n}</th>{''.join(f'<td>{clp(v)}</td>' for v in vals)}</tr>" for n, vals in MAINT["rows"])
    s = head("Mantenciones — Kove Moto Chile", "Valores de mantención por tiempo y kilometraje para motos Kove en Chile.", R, "page-maint")
    s += nav(R, "mantenciones.html")
    s += f"""<section class="page-hero"><h1>Mantención<br><em>transparente.</em></h1><p class="lead">Valores referenciales por tiempo de uso y kilometraje (publicación diciembre 2025).</p></section>
<section class="compare"><div class="tbl-wrap"><table class="cmp"><thead><tr><th>Modelo</th>{th}</tr></thead><tbody>{tb}</tbody></table></div><p class="note">Valores en pesos chilenos. Confirma vigencia y detalle con tu distribuidor autorizado.</p></section>
<section class="oil"><div>{img("FUCHS-Silkolene.png", "", "Fuchs Silkolene")}</div><p>Lubricante oficial Kove: <b>Fuchs Silkolene</b>.</p><a class="btn" href="distribuidores.html">Buscar distribuidor</a></section>"""
    s += footer(R)
    write("mantenciones.html", s)


def nosotros():
    R = ""
    s = head("Nosotros — Kove Moto Chile", "Historia de KOVE MOTO, logros globales, campeones en Chile y garantías para bienes durables.", R, "page-about")
    s += nav(R, "nosotros.html")
    s += f"""<section class="page-hero"><h1>De Chongqing<br>al <em>Dakar.</em></h1><p class="lead">KOVE MOTO, fundada en 2017, diseña, fabrica y vende motocicletas deportivas de alto rendimiento y gran cilindrada, con foco en innovación y competencia.</p></section>
<section class="about-grid">
 <article class="reveal"><h3>Logros y presencia global</h3><p>En 2021 superó las 20.000 unidades vendidas con un crecimiento anual promedio del 40%. Hoy exporta más de 5.000 unidades. En España se comercializa como Macbor Montana XR5 y en la República Checa como Jawa RVM 500.</p></article>
 <article class="reveal"><h3>Poder y tecnología</h3><p>Cuarta marca china en ventas de motos sobre 300 cc. Su 500X ADV lidera la producción nacional de ADV. Fábricas en Chongqing y Chengdu y un equipo de diseño de 113 personas.</p></article>
 <article class="reveal"><h3>Visión futura</h3><p>Seguirá invirtiendo en investigación, desarrollo y diseño para reforzar su imagen de marca tecnológica y de alto rendimiento.</p></article></section>
<section class="champs"><div class="champs-photo">{img("2025-Dakar-Rally-WESTx1000-1-15-3-scaled.jpg", "", "Dakar")}</div><div class="champs-copy"><h2>Los que ya la probaron en Chile</h2>
<p>Kove llegó oficialmente de la mano de Importadora IMOTO S.A. Entre quienes conocen la marca están el dakariano <b>Daniel Gouet</b> (450 Rally), el rallysta <b>Axel Heilenkötter</b> y el endurista <b>Hernán Delfino</b>.</p>
<p>La línea chilena incluye la 450RR de cuatro cilindros, las adventure 510X y 800X-PRO (también con kit de tres maletas) y las rally 450 Rally y 800X Rally.</p></div></section>
<section class="legal" id="garantias"><h2>Garantías para bienes durables</h2><p>En cumplimiento de la Ley 19.496, se informa que una motocicleta es un bien durable compuesto por componentes complejos, cada uno con su propia vida útil. La duración depende de las condiciones de uso y kilómetros recorridos, la carga, el camino por el que se circula y el cumplimiento del plan de mantenimiento periódico recomendado por la marca.</p><p>Consulta los términos completos con tu distribuidor autorizado.</p></section>"""
    s += footer(R)
    write("nosotros.html", s)


def contacto():
    R = ""
    s = head("Contacto y cotización — Kove Moto Chile", "Cotiza tu Kove por WhatsApp o contacta a un distribuidor autorizado.", R, "page-contact")
    s += nav(R, "contacto.html")
    s += f"""<section class="page-hero"><h1>Hablemos de<br><em>tu próxima Kove.</em></h1></section>
<section class="dealers-cta contact"><div><h2>Cotiza por WhatsApp</h2><p>Cuéntanos qué modelo te interesa y en qué ciudad estás. </p><p><a href="https://wa.me/{WA}" target="_blank" rel="noopener">+56 9 7579 2659</a><br><a href="{IG}" target="_blank" rel="noopener">@kove_moto_chile</a></p></div><div class="qbox">{quote_form(R)}</div></section>"""
    s += footer(R)
    write("contacto.html", s)


if __name__ == "__main__":
    for d in ("pdf",):
        os.makedirs(os.path.join(SITE, d), exist_ok=True)
        for f in os.listdir(os.path.join(ROOT, "assets", "pdf")):
            shutil.copy(os.path.join(ROOT, "assets", "pdf", f), os.path.join(SITE, d, f))
    home(); modelos(); distribuidores(); mantenciones(); nosotros(); contacto()
    for m in MODELS:
        model_page(m)
    print("ok", len(os.listdir(os.path.join(SITE, "img"))), "imgs")
