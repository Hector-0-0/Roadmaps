#!/usr/bin/env python3
"""Verifica la calidad del repositorio. Uso: python3 scripts/verificar.py [--urls]"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errores = []
avisos = []


def leer(f):
    with open(f, encoding="utf-8") as fh:
        return fh.read()


# 1. Prácticas: 6 a 8 ejercicios, pista de 6+ palabras, criterio verificable, sin "conceptual"
for f in sorted(glob.glob("**/practica.md", recursive=True)):
    t = leer(f)
    items = [i for i in re.split(r"\n(?=\d+\. \*\*)", t) if re.match(r"\d+\. \*\*", i)]
    if not 6 <= len(items) <= 8:
        errores.append(f"{f}: {len(items)} ejercicios (se piden 6 a 8)")
    for n, i in enumerate(items, 1):
        m = re.search(r"Pista:\s*(.+)", i)
        if not m or len(m.group(1).split()) < 6:
            errores.append(f"{f}: ejercicio {n} con pista ausente o menor a 6 palabras")
        if "Criterio verificable" not in i:
            errores.append(f"{f}: ejercicio {n} sin 'Criterio verificable'")
    if re.search(r"conceptual", t, re.I):
        errores.append(f"{f}: contiene la palabra 'conceptual'")

# 2. Recursos: al menos una URL y al menos 3 recursos
urls = set()
for f in sorted(glob.glob("**/recursos.md", recursive=True)):
    t = leer(f)
    u = re.findall(r"https?://[^\s)\]>\"'`]+", t)
    urls.update(u)
    if not u:
        errores.append(f"{f}: no tiene ninguna URL")
    if len(re.findall(r"^(?:[-*] |\d+\. )", t, flags=re.M)) < 3:
        errores.append(f"{f}: menos de 3 recursos")
    if "verificar enlace" in t:
        avisos.append(f"{f}: {t.count('verificar enlace')} marcas '(verificar enlace)' pendientes")

# 3. Archivos .md pequeños, enlaces relativos rotos y guiones largos
for f in glob.glob("**/*.md", recursive=True):
    if os.path.getsize(f) < 400:
        errores.append(f"{f}: menos de 400 bytes")
    t = leer(f)
    for m in re.finditer(r"\]\(([^)#\s]+)\)", t):
        link = m.group(1)
        if link.startswith(("http", "mailto")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), link))):
            errores.append(f"{f}: enlace roto {link}")
    if f != "AGENTS.md" and ("\u2014" in t or " -- " in t):
        errores.append(f"{f}: contiene guion largo o ' -- '")

# 4. Opcional: comprobar URLs (requiere internet)
if "--urls" in sys.argv:
    for u in sorted(urls):
        r = subprocess.run(
            ["curl", "-sIL", "-m", "15", "-o", "/dev/null", "-w", "%{http_code}", u],
            capture_output=True, text=True)
        if r.stdout.strip() != "200":
            errores.append(f"URL con respuesta {r.stdout.strip() or 'sin respuesta'}: {u}")

for a in avisos:
    print("AVISO:", a)
for e in errores:
    print("ERROR:", e)
print(f"\n{len(errores)} errores, {len(avisos)} avisos")
sys.exit(1 if errores else 0)
