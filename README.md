# Kove Moto Chile — rediseño v1

Sitio estático generado con Python.

```bash
python3 -I build/build.py                      # genera site/
python3 -m http.server 5173 --directory site   # servir en local
```

`build/build.py` necesita `assets/` (imágenes originales y fichas PDF), que no está en el repo por tamaño y por derechos de terceros. Las imágenes provienen de kovemotochile.cl, kovemoto.com, kovemotor.es y macbor.com y son referenciales.
