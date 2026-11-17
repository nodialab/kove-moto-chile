"""Fondos ilustrados (sin moto) para el hero de cada modelo. Usan var(--ac) del tema."""
_O = '<svg viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'

HERO_BG = {
    # Sport: asfalto, franjas de velocidad y 450 en contorno
    "450rr": _O + '''<defs><radialGradient id="g" cx="65%" cy="55%" r="60%"><stop offset="0" stop-color="var(--ac)" stop-opacity=".32"/><stop offset="1" stop-color="var(--ac)" stop-opacity="0"/></radialGradient>
<pattern id="s" width="90" height="90" patternUnits="userSpaceOnUse" patternTransform="rotate(-25)"><rect width="3" height="90" fill="var(--ac)" opacity=".3"/></pattern></defs>
<rect width="1200" height="800" fill="#0b0b0e"/><rect width="1200" height="800" fill="url(#g)"/><rect width="1200" height="800" fill="url(#s)"/>
<text x="1180" y="640" text-anchor="end" font-family="Barlow Condensed" font-weight="800" font-style="italic" font-size="620" fill="none" stroke="var(--ac)" stroke-opacity=".45" stroke-width="3">450</text>
<path d="M0 700 L1200 620 L1200 800 L0 800Z" fill="#050507"/><path d="M0 700 L1200 620" stroke="var(--ac)" stroke-width="4" stroke-dasharray="60 40" opacity=".7"/>''' + '</svg>',
    # Rally: dunas al atardecer
    "450-rally": _O + '''<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c120a"/><stop offset=".55" stop-color="#8a4a1a"/><stop offset="1" stop-color="#e29a4a"/></linearGradient></defs>
<rect width="1200" height="800" fill="url(#g)"/><circle cx="820" cy="430" r="120" fill="#ffd9a0" opacity=".85"/>
<path d="M0 520C200 470 330 560 520 520s300-110 480-60 140 50 200 40V800H0Z" fill="#a8581f"/>
<path d="M0 600C180 540 360 650 560 600s330-90 640-20V800H0Z" fill="#7a3c14"/>
<path d="M0 690C220 640 400 730 640 690s380-70 560-10V800H0Z" fill="#3d1d0a"/>''' + '</svg>',
    # 510X: curvas de nivel
    "510x": _O + '''<rect width="1200" height="800" fill="#dfe8f4"/><g fill="none" stroke="var(--ac)" stroke-width="2" opacity=".35">
''' + "".join(f'<path d="M-40 {y}C160 {y-60} 300 {y+60} 500 {y}S800 {y-70} 1000 {y-20}S1150 {y+20} 1240 {y-10}"/>' for y in range(120, 780, 46)) + '''</g>
<circle cx="900" cy="300" r="260" fill="var(--ac)" opacity=".08"/>''' + '</svg>',
    # 800X-PRO: cordillera oscura con resplandor dorado
    "800x-pro": _O + '''<defs><radialGradient id="g" cx="70%" cy="48%" r="55%"><stop offset="0" stop-color="var(--ac)" stop-opacity=".55"/><stop offset="1" stop-color="var(--ac)" stop-opacity="0"/></radialGradient></defs>
<rect width="1200" height="800" fill="#0a0a0a"/><rect width="1200" height="800" fill="url(#g)"/>
<path d="M0 520L180 400 300 480 470 330 620 470 800 360 960 480 1100 400 1200 470V800H0Z" fill="#1a1916"/>
<path d="M0 620L140 540 300 620 520 500 700 610 900 520 1080 600 1200 560V800H0Z" fill="#100f0d"/>
<path d="M0 720L260 660 520 730 800 650 1200 720V800H0Z" fill="#070707"/>''' + '</svg>',
    # 800X Rally: chevrones de peligro / cronometraje
    "800x-rally": _O + '''<defs><pattern id="s" width="140" height="140" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><rect width="70" height="140" fill="var(--ac)" opacity=".26"/></pattern>
<linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset=".5" stop-color="#0b0b0a" stop-opacity="0"/><stop offset="1" stop-color="#0b0b0a"/></linearGradient></defs>
<rect width="1200" height="800" fill="#12120f"/><rect width="1200" height="800" fill="url(#s)"/>
<text x="1200" y="520" text-anchor="end" font-family="Barlow Condensed" font-weight="800" font-size="420" fill="var(--ac)" opacity=".14">RALLY</text><rect width="1200" height="800" fill="url(#f)"/>''' + '</svg>',
    # Touring: montañas claras y ruta
    "800x-touring": _O + '''<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe7e3"/><stop offset="1" stop-color="#f3f7f6"/></linearGradient></defs>
<rect width="1200" height="800" fill="url(#g)"/><circle cx="900" cy="250" r="90" fill="#fff" opacity=".9"/>
<path d="M0 520L200 330 340 450 520 280 700 460 880 340 1060 470 1200 400V800H0Z" fill="var(--ac)" opacity=".22"/>
<path d="M0 620L180 500 360 600 560 470 760 600 980 500 1200 590V800H0Z" fill="var(--ac)" opacity=".4"/>
<path d="M-20 780C200 640 420 700 620 650s380-170 620-110" fill="none" stroke="#fff" stroke-width="26"/>
<path d="M-20 780C200 640 420 700 620 650s380-170 620-110" fill="none" stroke="var(--ac)" stroke-width="3" stroke-dasharray="26 22"/>''' + '</svg>',
}
