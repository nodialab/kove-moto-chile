WA = "56975792659"
IG = "https://www.instagram.com/kove_moto_chile/"
FB = "https://www.facebook.com/kovemotoschile/"

DAK = "2025-Dakar-Rally-WESTx1000-1-%s-scaled.jpg"

MODELS = [
    dict(
        slug="450rr", name="450RR", cat="Sport", short="450RR",
        tagline="Cuatro cilindros. Cero concesiones.",
        lead="La primera deportiva de cuatro cilindros en línea de su categoría llega a Chile con electrónica de pista: quick shifter, control de lanzamiento y suspensión KYB totalmente ajustable.",
        accent="#ff4a2e", price=None, pdf="FICHA_KOVE_450RR_2026.pdf",
        stats=[("70", "HP", "13.000 rpm"), ("39", "N·m", "10.500 rpm"), ("165", "kg", "en orden de marcha"), ("220", "km/h", "velocidad máx.")],
        hero="450RR-white-01.webp",
        colors=[("Blanco perla", "#ecebe8", "450RR-white-01.webp"), ("Negro mate", "#17181a", "450RR-BLACK-01.webp"),
                ("Rojo carrera", "#d3261a", "kove450RR-1.jpg")],
        carousel=["450RR-11-scaled.webp", "450RR-12-scaled.webp", "450RR-13.webp", "DSC4352-scaled.jpg", "DSC4359-scaled.jpg",
                  "SLIDER_450RR_1POR.jpg", "SLIDER_450RR_2POR.jpg", "SLIDER_450RR_3POR.jpg"],
        gallery=["450RR-B.jpg", "450RR-D.jpg", "450RR-E.jpg", "450RR-A.jpg", "kove450RR-2.jpg", "kove450RR-3.jpg", "kove450RR-1.jpg",
                 "450RR-white-03.webp", "450RR-BLACK-05.webp", "450RR-3.jpg", "450RR-8-1.webp", "450RR-8-2.webp"],
        details=[("450RR-10-1.png", "Tablero TFT", "Telemetría de carrera, modos y control de tracción en una sola pantalla."),
                 ("450RR-10-2.png", "Launch control", "Salida perfecta, siempre: el sistema administra la potencia hasta el primer cambio."),
                 ("450RR-10-3.png", "Quick shifter", "Subidas sin embrague y sin cortar el empuje."),
                 ("450RR-4.png", "RAM-AIR", "Admisión dinámica que gana potencia a medida que sube la velocidad.")],
        features=["Control de tracción (TCS) desconectable", "Quick shifter", "Embrague antirrebote", "Control de lanzamiento", "Suspensión KYB totalmente ajustable",
                  "Luces LED con función adaptativa en curvas", "Tablero TFT con telemetría", "Amortiguador de dirección hidráulico", "Admisión RAM-AIR",
                  "Alerones delanteros", "Modos ECO / SPORT", "ABS desconectable"],
        specs=[("Motor", [("Tipo", "Tetracilíndrico, DOHC, 16 válvulas, 4T"), ("Cilindrada", "443 cc"), ("Compresión", "12,9:1"), ("Potencia máx.", "70 HP a 13.000 rpm"),
                          ("Torque máx.", "39 N·m a 10.500 rpm"), ("Embrague", "Multidisco antirrebote en baño de aceite"), ("Refrigeración", "Líquida"),
                          ("Alimentación", "Inyección electrónica BOSCH"), ("Transmisión", "6 velocidades · cadena")]),
               ("Chasis", [("Susp. delantera", "KYB invertida ajustable Ø41 mm"), ("Susp. trasera", "KYB ajustable, cápsula de aire externa"),
                           ("Freno delantero", "Doble disco flotante 300 mm, pinza 4 pistones, ABS"), ("Freno trasero", "Disco 220 mm, 1 pistón, ABS"),
                           ("Neumáticos", "MAXXIS 120/70ZR17 · 160/60ZR17")]),
               ("Dimensiones", [("Largo × ancho × alto", "2015 × 740 × 1090 mm"), ("Distancia entre ejes", "1385 mm"), ("Peso en orden de marcha", "165 kg"), ("Estanque", "14 litros")])],
    ),
    dict(
        slug="450-rally", name="450 Rally", cat="Rally", short="450 Rally",
        tagline="La réplica de rally que sí puedes patentar.",
        lead="Monocilíndrica de 449 cc, 155 kg y estanque de 29 litros. Diseñada con ADN Dakar y homologada para uso urbano: del salar a la Alameda sin cambiar de moto.",
        accent="#18c2c9", price=8460000, pdf="FICHA_KOVE_450Rally_2025.pdf",
        stats=[("41", "HP", "8.500 rpm"), ("35", "N·m", "6.500 rpm"), ("155", "kg", "en orden de marcha"), ("29", "L", "estanque principal + aux.")],
        hero="450rally-blue-1.webp",
        colors=[("Blanco / Turquesa", "#19c3c9", "450rally-blue-1.webp"), ("Blanco / Rojo", "#d3261a", "450rally-red-01-1.webp"),
                ("Blanco / Negro", "#e8e8e8", "450Rally.png"), ("Verde", "#2f9e57", "450RALLY_GREEN.png")],
        carousel=["450RALLY_9-scaled.jpg", "450RALLY*27-scaled.jpg", "450Rally_desert.jpg", DAK % "13-4", DAK % "16-1", DAK % "5-2", "LLL05276-scaled.jpg", "LLL06204-scaled.jpg"],
        gallery=["450rally-blue-02.webp", "450rally-blue-03-1.webp", "450rally-blue-04.webp", "450rally-red-02-1.webp", "450rally-red-03-1.webp", "450rally-red-04-1.webp",
                 "sliders_interior450Rally1.png", "sliders_interior450Rally3.png", "450Rally-EX-RED_A.png", "450Rally_calle_blanca2.png", "450-Rally-Ex-1.webp", DAK % "11-2"],
        details=[],
        features=["Pantalla TFT 5\" horizontal", "3 modos de ABS (desconectable)", "Cubre cárter en fibra de carbono", "Suspensiones YUAN ajustables", "Multi-estanque de combustible",
                  "Carenados de montaje rápido", "Subchasis desmontable", "Frenos TAISKO", "Homologada para uso urbano"],
        specs=[("Motor", [("Tipo", "Monocilíndrico, DOHC, 4 válvulas, 4T"), ("Cilindrada", "449 cc"), ("Compresión", "12,5:1"), ("Potencia máx.", "41 HP a 8.500 rpm"),
                          ("Torque máx.", "35 N·m a 6.500 rpm"), ("Embrague", "Multidisco en baño de aceite"), ("Refrigeración", "Líquida (aceite y refrigerante)"),
                          ("Alimentación", "Inyección electrónica BOSCH"), ("Transmisión", "6 velocidades · cadena")]),
               ("Chasis", [("Susp. delantera", "Horquilla invertida, 305 mm"), ("Susp. trasera", "Monoshock, 300 mm"), ("Freno delantero", "Disco 288 mm, ABS desconectable"),
                           ("Freno trasero", "Disco 240 mm, ABS desconectable"), ("Neumáticos", "90/90-21 · 140/80-18")]),
               ("Dimensiones", [("Largo × ancho × alto", "2190 × 805 × 1420 mm"), ("Altura de asiento", "960 mm"), ("Distancia entre ejes", "1475 mm"),
                                ("Peso en orden de marcha", "155 kg"), ("Estanque", "29 litros (principal + auxiliar)")])],
    ),
    dict(
        slug="510x", name="510X", cat="Adventure", short="510X",
        tagline="Aventura accesible, con equipamiento de moto grande.",
        lead="Bicilíndrica de 498 cc con suspensiones KYB, TFT de 5\", sensores de presión de neumáticos y 820 mm de asiento. La puerta de entrada al mundo ADV, con versión equipada de tres maletas.",
        accent="#3b82f6", price=None, pdf="FICHA_KOVE_510X_2025.pdf",
        stats=[("46,9", "HP", "8.500 rpm"), ("45", "N·m", "7.000 rpm"), ("820", "mm", "altura de asiento"), ("20", "L", "estanque")],
        hero="extra2:mb_xr5__*adventure-azul-montana-xr5-510-2024.png",
        colors=[("Azul", "#2f5bff", "extra2:mb_xr5__*adventure-azul-montana-xr5-510-2024.png"), ("Blanco", "#ecebe8", "extra2:mb_xr5__*adventure-blanco-montana-xr5-510-2024.png"),
                ("Negro", "#17181a", "extra2:mb_xr5__*adventure-negro-montana-xr5-510-2024.png"), ("Rojo · 3 maletas", "#d3261a", "extra2:mb_xr5__*adventure-rojo-montana-xr5-510-maletas.png")],
        carousel=["extra2:mb_xr5__*accion-%d.jpg" % i for i in (11, 3, 16, 17, 1, 18, 6, 4)],
        gallery=["sliders_interior510-1.png", "sliders_interior510-2.png", "sliders_interior510-3.png", "sliders_interior510-4.png", "para_menu_510X.jpg", "para_menu_510X-M.jpg",
                 "interior1_534x358px.jpg", "interior4_534x358px.jpg", "interior5_534x358px.jpg", "interior6_534x358px.jpg", "interior8_534x358px.jpg", "interior10_534x358px.jpg"],
        details=[],
        features=["Pantalla TFT 5\" horizontal", "Modos ECO / SPORT", "3 modos de ABS", "Suspensiones KYB totalmente ajustables", "Neumáticos Metzeler® Tourance®",
                  "Sensor de presión y temperatura de neumáticos", "Frenos Nissin", "Defensas de motor y cubre manos", "Cubre cárter y caballete central", "USB y toma de 12 V",
                  "Comandos retroiluminados"],
        specs=[("Motor", [("Tipo", "Bicilíndrico, DOHC, 8 válvulas, 4T"), ("Cilindrada", "498,4 cc"), ("Compresión", "10,6:1"), ("Potencia máx.", "46,9 HP a 8.500 rpm"),
                          ("Torque máx.", "45 N·m a 7.000 rpm"), ("Embrague", "Multidisco antirrebote en baño de aceite"), ("Refrigeración", "Líquida"),
                          ("Alimentación", "Inyección electrónica BOSCH"), ("Transmisión", "6 velocidades · cadena")]),
               ("Chasis", [("Susp. delantera", "Horquilla invertida KYB"), ("Susp. trasera", "Monoshock KYB"), ("Frenos", "Disco hidráulico delantero y trasero, ABS desconectable"),
                           ("Neumáticos", "110/80-R19 · 150/70-R17 Metzeler® Tourance®")]),
               ("Dimensiones", [("Largo × ancho × alto", "2200 × 935 × 1400 mm"), ("Altura de asiento", "820 mm"), ("Distancia entre ejes", "1479 mm"),
                                ("Peso en orden de marcha", "205 kg"), ("Estanque", "20 litros")])],
    ),
    dict(
        slug="800x-pro", name="800X-PRO", cat="Adventure", short="800X-PRO",
        tagline="95 HP para cruzar el continente.",
        lead="Nueva versión 2026 con tablero TFT de 7\" y Screen Mirroring, conexión Kove App, doble disco delantero, control crucero y amortiguador de dirección FASTace. Disponible también con kit de tres maletas.",
        accent="#e0a526", price=9460000, pdf="FICHA_KOVE_800X-PRO_2026.pdf",
        stats=[("95,2", "HP", "9.000 rpm"), ("80", "N·m", "7.000 rpm"), ("190", "kg", "en orden de marcha"), ("20", "L", "estanque")],
        hero="800X-PRO-White-1.png",
        colors=[("Blanco / Gris", "#e9e9e6", "800X-PRO-White-1.png"), ("Negro", "#1b1b1d", "800x-pro-black-01.png"), ("Verde", "#3f5a47", "kove800X-green.jpg"),
                ("Gris", "#8b8e93", "kove800X-grey.jpg")],
        carousel=["extra:800x-pro.png", "800X-PRO1.jpg", "sliders_interior_800X-PRO_2026A.jpg", "sliders_interior_800X-PRO_2026C.jpg", "800x-touring_fondo4_2026.jpg", "800X-Touring-4.jpg"],
        gallery=["800x-pro-black-02.png", "800x-pro-black-03.png", "800x-pro-black-04.png", "800x-pro-black-05.png", "800x-pro-black-06.png", "800X-PRO-White-2.png",
                 "800X-PRO_2026A-scaled.jpg", "800X-PRO_2026B-scaled.jpg", "800X-PRO_2026Blanca-scaled.jpg", "800X-M.jpg", "800X-M_green.jpg", "800x-pro-1.jpg"],
        details=[],
        features=["Estilo Adventure / Touring", "Control crucero", "Acelerador electrónico", "Quick shifter (up)", "Modos: Rain · Comfort · Sport · Off-road · User",
                  "Tablero TFT 7\" con Screen Mirroring", "Conexión Kove App", "Doble disco de freno delantero", "Amortiguador de dirección FASTace", "Defensas de fábrica y cubre cárter",
                  "Parabrisas y cubre manos"],
        specs=[("Motor", [("Tipo", "Bicilíndrico, DOHC, 8 válvulas, 4T"), ("Cilindrada", "799 cc"), ("Compresión", "13,0:1"), ("Potencia máx.", "95,2 HP a 9.000 rpm"),
                          ("Torque máx.", "80 N·m a 7.000 rpm"), ("Embrague", "Multidisco en baño de aceite"), ("Refrigeración", "Líquida"),
                          ("Alimentación", "Inyección electrónica BOSCH"), ("Transmisión", "6 velocidades · cadena")]),
               ("Chasis", [("Susp. delantera", "Horquilla invertida KYB"), ("Susp. trasera", "Monoshock KYB"), ("Freno delantero", "Doble disco hidráulico, ABS desconectable"),
                           ("Freno trasero", "Disco hidráulico, ABS desconectable"), ("Neumáticos", "90/90-21 · 150/70-R18 Pirelli Scorpion Rally")]),
               ("Dimensiones", [("Largo × ancho × alto", "2250 × 898 × 1410 mm"), ("Distancia entre ejes", "1530 mm"), ("Peso en orden de marcha", "190 kg"), ("Estanque", "20 litros")])],
    ),
    dict(
        slug="800x-rally", name="800X Rally", cat="Rally", short="800X Rally",
        tagline="La más liviana de su segmento. 176 kg, 95 HP.",
        lead="Componentes probados en el Dakar: horquilla de doble cámara con 270 mm de recorrido, frenos TAISKO, ruedas de rally y neumáticos CST Ambro A3. Empuje constante, aceleración inmediata.",
        accent="#f5b700", price=8990000, pdf="FICHA_KOVE_800X-Rally_2025.pdf",
        stats=[("95", "HP", "9.000 rpm"), ("80", "N·m", "7.500 rpm"), ("176", "kg", "en vacío"), ("270", "mm", "recorrido delantero")],
        hero="800x-rally-Golden-01.webp",
        colors=[("Dorado", "#f0b323", "800x-rally-Golden-01.webp"), ("Verde agua", "#2bb8a8", "800x-rally-green-01.webp")],
        carousel=["800X-RALLY-Gold.jpeg", "800X-Rally-1-scaled.webp", "sliders_800X-Rally1.jpg", "sliders_800X-Rally2.jpg", "sliders_800X-Rally3.jpg", "sliders_800X-Rally4.jpg",
                  "sliders_800X-Rally5.jpg", "sliders_800X-Rally6.jpg", "SLIDER_800Rally_1_POR.jpg", "SLIDER_800Rally_2_POR.jpg", "SLIDER_800Rally_3_POR.jpg"],
        gallery=["800x-rally-Golden-02.webp", "800x-rally-Golden-03.webp", "800x-rally-Golden-04.webp", "800x-rally-Golden-05.webp", "800x-rally-green-02.webp",
                 "800x-rally-green-03.webp", "800x-rally-green-04.webp", "800x-rally-green-06.webp", "800X-Rally-2.webp", "800X-Rally-3.webp", "800Rally_A.png", "800Rally_B.png"],
        details=[],
        features=["Tablero TFT 7\" vertical", "Horquilla Ø49 mm de doble cámara", "Frenos TAISKO probados en el Dakar", "Estanque central de 20 L", "Ruedas con especificación de rally",
                  "Neumáticos off-road CST Ambro A3", "Guía de cadena reforzada", "Admisión de aire constante"],
        specs=[("Motor", [("Tipo", "Bicilíndrico vertical, DOHC, 4T"), ("Cilindrada", "799 cc"), ("Diámetro × carrera", "88 × 65,7 mm"), ("Compresión", "13:1"),
                          ("Potencia máx.", "95 HP a 9.000 rpm"), ("Torque máx.", "80 N·m a 7.500 rpm"), ("Refrigeración", "Líquida"), ("Alimentación", "EFI"), ("Velocidad máx.", "180 km/h")]),
               ("Chasis", [("Bastidor", "Diamante con viga de doble ala"), ("Susp. delantera", "Ø49 mm, precarga ajustable · 270 mm"), ("Susp. trasera", "Cilindro de aire externo · 240 mm"),
                           ("Freno delantero", "1 disco, pinza flotante de 2 pistones"), ("Freno trasero", "1 disco, pinza flotante de 1 pistón"), ("Neumáticos", "90/90-21 · 140/80-18")]),
               ("Dimensiones", [("Largo × ancho × alto", "2267 × 810 × 1395 mm"), ("Distancia entre ejes", "1545 mm"), ("Altura de asiento", "890 mm"), ("Peso en vacío", "176 kg"), ("Estanque", "20 litros")])],
    ),
    dict(
        slug="800x-touring", name="800X Touring", cat="Adventure", short="800X Touring",
        tagline="Superaventura de largo aliento.",
        lead="Tablero TFT de 7\" con proyección de móvil, asiento y puños calefactables, control crucero, quick shifter bidireccional, estanque de 22 litros y tres maletas de serie.",
        accent="#7dd3c8", price=9580000, pdf="FICHA_KOVE_800X-TROURING_2026.pdf",
        stats=[("95,2", "HP", "9.000 rpm"), ("80", "N·m", "7.500 rpm"), ("22", "L", "autonomía de viaje"), ("215", "kg", "con tres maletas")],
        hero="800X-TOURING-white-01.webp",
        colors=[("Blanco", "#eeeeea", "800X-TOURING-white-01.webp"), ("Negro", "#1c1c1e", "800X-TOURING-black-01.webp")],
        carousel=["800X-Touring-13-scaled.webp", "800X-Touring-14-scaled.webp", "800X-Touring-12.webp", "800X-Touring-10.webp", "800x-touring_portada_2026.jpg",
                  "800x-touring_fondo_2026.jpg", "800X-Touring-9.webp", "800X-Touring-1.webp"],
        gallery=["800X-TOURING-white-03.webp", "800X-TOURING-white-04.webp", "800X-TOURING-white-06.webp", "800X-TOURING-black-03.webp", "800X-TOURING-black-04.webp",
                 "800X-TOURING-black-02.webp", "800X-Touring-2.jpg", "800X-Touring-3.jpg", "800X-Touring-4.jpg", "800X-Touring-5.png", "800X-Touring-6.png", "800X-Touring-11.webp"],
        details=[("800X-Touring-10-1.webp", "Puños calefactables", "Calor controlado para largas jornadas en la cordillera."),
                 ("800X-Touring-10-2.webp", "Asiento calefactable", "Confort desde el primer kilómetro hasta el último."),
                 ("800X-Touring-11.webp", "TFT 7\" + navegación", "Proyecta tu móvil y conecta con la Kove App."),
                 ("800X-Touring-9-1.webp", "Gestión de aire", "Salida de aire optimizada para mantener la temperatura del motor.")],
        features=["Modos Comfort / Rain / Sport / Off-road", "Doble disco delantero Taisko", "Defensas de fábrica y cubre cárter", "Amortiguador de dirección FASTace",
                  "Tablero TFT 7\" con proyección de móvil", "Asiento y puños calefactables", "Acelerador electrónico y control crucero", "Control de tracción y ABS desconectables",
                  "Quick shifter bidireccional (up/down)", "Monitoreo de presión de neumáticos", "Neumáticos CST Ambro", "Manubrio de diseño touring"],
        specs=[("Motor", [("Tipo", "Bicilíndrico, DOHC, 8 válvulas, 4T"), ("Cilindrada", "799 cc"), ("Compresión", "13,0:1"), ("Potencia máx.", "95,2 HP a 9.000 rpm"),
                          ("Torque máx.", "80 N·m a 7.500 rpm"), ("Embrague", "Multidisco en baño de aceite"), ("Refrigeración", "Líquida"),
                          ("Alimentación", "Inyección electrónica BOSCH"), ("Transmisión", "6 velocidades · cadena")]),
               ("Chasis", [("Susp. delantera", "Horquilla invertida regulable KYB, 210 mm"), ("Susp. trasera", "Monoshock regulable KYB, 210 mm"),
                           ("Freno delantero", "Doble disco, caliper TAISKO, ABS desconectable"), ("Freno trasero", "Disco hidráulico, ABS desconectable"),
                           ("Neumáticos", "110/80-R19 · 150/70-R17 CST")]),
               ("Dimensiones", [("Largo × ancho × alto", "2230 × 930 × 1395 mm"), ("Distancia entre ejes", "1520 mm"), ("Peso en orden de marcha", "215 kg con tres maletas"), ("Estanque", "22 litros")])],
    ),
]

DEALERS = [
    ("Santiago Motorcycles", "Av. Padre Hurtado Norte 1454", "Vitacura", "Santiago", "Metropolitana", "(+56 9) 3949 8902", "ventas@h-dsantiago.cl"),
    ("Imoto Lira", "Lira 669", "Santiago Centro", "Santiago", "Metropolitana", "(+56 9) 6907 0930", ""),
    ("Imoto Argomedo", "Argomedo 363", "Santiago Centro", "Santiago", "Metropolitana", "(+56 9) 6689 3025", ""),
    ("Bikestore", "Lira 651", "Santiago Centro", "Santiago", "Metropolitana", "(56 2) 2916 7953", "ventas@bikestore.cl"),
    ("Rino Motos", "Av. Las Condes 8482", "Las Condes", "Santiago", "Metropolitana", "(56 2) 2891 2127", "leandro.gobantes@rinomotos.cl"),
    ("VM Motos", "Vitacura 9360", "Vitacura", "Santiago", "Metropolitana", "(56 2) 2201 6280", "vmmotos@gmail.com"),
    ("Motomanía", "Gran Av. José Miguel Carrera 2550", "San Miguel", "Santiago", "Metropolitana", "(56 2) 2891 1719", "motomania@motomania.cl"),
    ("Tonino Motos", "Balmaceda 1461", "La Serena", "La Serena", "IV Región", "(51) 221 3268", "info@toninomotos.cl"),
    ("Mach Motos", "4 Oriente 1264", "Viña del Mar", "Viña del Mar", "V Región", "(+56 9) 3284 4661", "foviedo@mach.cl"),
    ("Gouet Garage", "Colo Colo 1525", "Concepción", "Concepción", "VIII Región", "(+56 9) 6310 3370", "gouetgarage@gmail.com"),
]

MAINT = {
    "cols": ["1.000 km · 3 meses", "5.000 km · 6 meses", "10.000 km · 12 meses", "15.000 km · 18 meses", "20.000 km · 24 meses"],
    "rows": [("800X-PRO / 800 Rally / Touring", [134990, 134990, 288990, 134990, 288990]),
             ("450 Rally", [109990, 109990, 144990, 109990, 144990]),
             ("510X", [132990, 132990, 222990, 132990, 222990]),
             ("450RR", [130990, 130990, 130990, 184990, 130990])],
}

HOME_HERO = ["2025-Dakar-Rally-WESTx1000-1-13-4-scaled.jpg", "LLL05235-scaled.jpg", "800x-touring_portada_2026.jpg", "SLIDER_450RR_1POR.jpg", "SLIDER_800Rally_1_POR.jpg"]


# ── Textos verificados: solo fichas PDF oficiales, web kovemotochile.cl y artículo "Campeones en Kove" ──
_OV = {
    "450rr": dict(
        tagline="Tetracilíndrica 443 cc · 70 HP",
        lead="Motor tetracilíndrico DOHC de 16 válvulas, 70 HP a 13.000 rpm y 165 kg en orden de marcha. Suspensiones KYB ajustables, frenos con doble disco flotante de 300 mm y neumáticos MAXXIS.",
        stats=[("70", "HP", "13.000 rpm"), ("39", "N·m", "10.500 rpm"), ("165", "kg", "en orden de marcha"), ("14", "L", "estanque")],
        colors=[("Blanco", "#ecebe8", "450RR-white-01.webp"), ("Negro", "#17181a", "450RR-BLACK-01.webp")],
        features=["Motocicleta de estilo deportivo", "Estabilizador de dirección ajustable", "Quick shifter", "Sistema elevador de potencia", "Alerones delanteros", "Sistema de luces ajustables",
                  "Control de tracción desconectable", "Dos modos de conducción ECO / SPORT", "ABS desconectable"],
        details=[("450RR-10-1.png", "Tablero TFT", ""), ("450RR-10-2.png", "Control de lanzamiento", ""), ("450RR-10-3.png", "Quick shifter", ""), ("450RR-4.png", "Sistema RAM-AIR", "")],
    ),
    "450-rally": dict(
        tagline="Monocilíndrica 449 cc · 41 HP",
        lead="Monocilíndrica de 449 cc, 155 kg en orden de marcha y estanque de 29 litros (principal + auxiliar). Pantalla TFT de 5\", suspensiones YUAN ajustables y homologada para uso urbano.",
    ),
    "510x": dict(
        tagline="Bicilíndrica 498 cc · 46,9 HP",
        lead="Bicilíndrica de 498,4 cc con 46,9 HP, suspensiones KYB, pantalla TFT de 5\", neumáticos Metzeler Tourance y 820 mm de altura de asiento. Versión 510X-M con tres maletas.",
    ),
    "800x-pro": dict(
        tagline="Nueva versión 2026 · 95,2 HP",
        lead="Nueva versión con tablero TFT de 7\" con Screen Mirroring, conexión Kove App, doble disco de freno delantero y amortiguador de dirección FASTace. Disponible en versión estándar y con kit de tres maletas.",
        colors=[("Blanco / Gris", "#e9e9e6", "800X-PRO-White-1.png"), ("Negro", "#1b1b1d", "800x-pro-black-01.png")],
    ),
    "800x-rally": dict(
        tagline="Solo 176 kg, la más liviana del mercado en su segmento",
        lead="Incorpora componentes probados en el Dakar: horquilla delantera de doble cámara con 270 mm de recorrido, frenos TAISKO, ruedas con especificaciones de rally y neumáticos off-road CST Ambro A3.",
        colors=[("Amarillo", "#f0b323", "800x-rally-Golden-01.webp"), ("Turquesa", "#2bb8a8", "800x-rally-green-01.webp")],
    ),
    "800x-touring": dict(
        tagline="Moto de turismo de superaventura",
        lead="Diseñada para ofrecer comodidad en largas distancias, un rendimiento potente y una exploración segura en todo tipo de caminos. Tablero TFT de 7\" con Screen Mirroring y conexión Kove App.",
        stats=[("95,2", "HP", "9.000 rpm"), ("80", "N·m", "7.500 rpm"), ("22", "L", "estanque"), ("215", "kg", "con tres maletas")],
        details=[("800X-Touring-10-1.webp", "Puños calefactables", ""), ("800X-Touring-10-2.webp", "Asiento calefactable", ""), ("800X-Touring-11.webp", "Tablero TFT 7\" con navegación", "")],
        features=["Modos de conducción Comfort / Rain / Sport / Off-road", "Doble disco de freno delantero Taisko", "Defensas de fábrica y cubre cárter", "Amortiguador de dirección FASTace",
                  "Tablero TFT 7\" con navegación y proyección en pantalla de móvil", "Asiento y puños calefactables", "Acelerador electrónico y control crucero",
                  "Control de tracción y ABS desconectables", "Quick shifter bidireccional (up/down)", "Sistema de monitoreo de presión de neumáticos", "Neumáticos CST Ambro",
                  "Manubrio de diseño touring", "Cubre manos Kove"],
    ),
}
for _m in MODELS:
    _m.update(_OV.get(_m["slug"], {}))
    if _m["slug"] != "450-rally":
        _m["price"] = None  # solo el precio de lista del 450 Rally está publicado por Kove Moto Chile (Facebook)
# Galería por modelo: carpeta extra2 (Kove España / Macbor) con patrón por modelo
EXTRA2 = {"450rr": "es_450rr__*", "450-rally": "es_450-rally-*", "510x": "mb_xr5__*", "800x-pro": "es_800x-pro-2026__*", "800x-rally": "es_800x-rally__*", "800x-touring": "es_800x-gt__*"}
EXCL = ("800X-radiadior", "MOTO-800X-ABS", "depositos.png", "share.jpg", "BANNER", "1918x400", "nueva-moto-adventure-800X-RALLY-2025", "NK-125R", "color", "blanc.png", "negre")

# ── Especificaciones completas (fichas PDF oficiales de Kove Moto Chile) ──
_SEAT = {"450rr": "785 mm", "800x-pro": "875 mm", "800x-touring": "826 mm"}  # no figura en la ficha chilena: dato de la ficha global de Kove (kove-moto.com)
for _m in MODELS:
    _s = dict(_m["specs"][0][1]) if False else None
    _g = {g: r for g, r in _m["specs"]}
    if "Transmisión" in dict(_g["Motor"]):
        _g["Motor"].append(("Arranque", "Eléctrico"))
    if _m["slug"] in _SEAT:
        _d = _g["Dimensiones"]
        _d.insert(1, ("Altura de asiento¹", _SEAT[_m["slug"]]))
        _m["seat_note"] = True
    if _m["slug"] == "800x-rally":
        _g["Chasis"].append(("Instrumentación", 'Pantalla TFT 7" vertical'))

# ── Reemplazo de imágenes de baja resolución por versiones de kovemoto.com (assets/extra4) ──
def _swap(m, key, old, new):
    L = m[key]
    for i, n in enumerate(L):
        if n.endswith(old):
            if new: L[i] = new
            else: L.pop(i)
            return
_M = {m["slug"]: m for m in MODELS}
_E4 = lambda n: "extra4:2026_07_" + n
_swap(_M["800x-touring"], "gallery", "800X-Touring-5.png", _E4("800X-Touring-3.webp"))
_swap(_M["800x-touring"], "gallery", "800X-Touring-6.png", _E4("800X-Touring-2.webp"))
for _n in ("liders_interior_800X-PRO_2026A.jpg", "liders_interior_800X-PRO_2026C.jpg"):
    _swap(_M["800x-pro"], "carousel", _n, None)
_M["800x-pro"]["carousel"].append(_E4("800x-pro-black.jpg"))
for _i in range(1, 7):
    _swap(_M["800x-rally"], "carousel", f"sliders_800X-Rally{_i}.jpg", None)
_M["800x-rally"]["carousel"] += [_E4("800X-RALLY-Gold-3.jpg"), _E4("800X-Rally-2.webp")]
_swap(_M["450-rally"], "gallery", "sliders_interior450Rally1.png", _E4("450-Rally-Re-2.webp"))
_swap(_M["450-rally"], "gallery", "sliders_interior450Rally3.png", None)
