#!/usr/bin/env python3
"""Verifica la calidad del repositorio. Uso: python3 scripts/verificar.py [--urls]"""
import ast
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

# 4b. Validar sintaxis de bloques ```python en todos los README.md
for f in sorted(glob.glob("**/README.md", recursive=True)):
    t = leer(f)
    bloques = re.findall(r"```python\n(.*?)```", t, re.S)
    for idx, bloque in enumerate(bloques, 1):
        try:
            ast.parse(bloque)
        except SyntaxError:
            errores.append(f"{f}: bloque python con sintaxis inválida (bloque {idx})")

# 5. Comprobaciones endurecidas SOLO para machine-learning/
if os.path.exists("machine-learning"):
    # a) Estructura: carpetas NN-* deben tener contenido; tema -> README, practica, recursos; checkpoint -> README, proyectos/.gitkeep; PROGRESO debe corresponder
    progreso = leer("machine-learning/PROGRESO.md") if os.path.exists("machine-learning/PROGRESO.md") else ""
    for etapa in glob.glob("machine-learning/*/"):
        if not os.path.isdir(etapa):
            continue
        for item in sorted(glob.glob(os.path.join(etapa, "*"))):
            if not os.path.isdir(item):
                continue
            base = os.path.basename(item)
            if re.match(r"^\d{2}-", base):
                if "checkpoint" in base:
                    if not os.path.exists(os.path.join(item, "README.md")):
                        errores.append(f"{os.path.join(item,'README.md')}: falta README para checkpoint")
                    if not os.path.exists(os.path.join(item, "proyectos", ".gitkeep")):
                        errores.append(f"{os.path.join(item,'proyectos','.gitkeep')}: falta .gitkeep para checkpoint")
                else:
                    if not os.path.exists(os.path.join(item, "README.md")):
                        errores.append(f"{os.path.join(item,'README.md')}: falta README para tema")
                    if not os.path.exists(os.path.join(item, "practica.md")):
                        errores.append(f"{os.path.join(item,'practica.md')}: falta practica.md para tema")
                    if not os.path.exists(os.path.join(item, "recursos.md")):
                        errores.append(f"{os.path.join(item,'recursos.md')}: falta recursos.md para tema")
    # PROGRESO entries correspond to folders
    for m in re.finditer(r"^\s*-\s*\[[ xX]\]\s*(.+)$", progreso, re.M):
        entry = m.group(1).strip()
        # try to find matching folder
        found = False
        for item in glob.glob("machine-learning/*/*"):
            if os.path.isdir(item) and entry in os.path.basename(item):
                found = True
                break
            # check subfolders
        if not found:
            # also check deeper
            for item in glob.glob("machine-learning/*/*/*"):
                if os.path.isdir(item) and (entry.replace(' ', '-') in os.path.basename(item).lower() or entry in os.path.basename(item)):
                    found = True
                    break
        if not found and entry:
            avisos.append(f"machine-learning/PROGRESO.md: entrada sin carpeta encontrada '{entry}'")

    # b) Tamaños mínimos
    for f in glob.glob("machine-learning/*/*/README.md", recursive=True):
        if "checkpoint" not in f:
            if os.path.getsize(f) < 2500:
                errores.append(f"{f}: README de teoría menor a 2500 bytes")
    for f in glob.glob("machine-learning/*/*/06-*checkpoint*/README.md", recursive=True):
        pass
    for f in glob.glob("machine-learning/*/*checkpoint*/README.md", recursive=True):
        if os.path.getsize(f) < 1500:
            errores.append(f"{f}: README de checkpoint menor a 1500 bytes")
    for f in glob.glob("machine-learning/*/README.md", recursive=True):
        if f.count('/') == 2:  # etapa README
            if os.path.getsize(f) < 800:
                errores.append(f"{f}: README de etapa menor a 800 bytes")
            t = leer(f)
            etapa_dir = os.path.dirname(f)
            for sub in sorted(glob.glob(os.path.join(etapa_dir, "*"))):
                if os.path.isdir(sub) and re.match(r"^\d{2}-", os.path.basename(sub)):
                    if os.path.basename(sub) not in t:
                        errores.append(f"{f}: debe contener enlace relativo a {os.path.basename(sub)}")

    # c) Secciones numeradas 1-6
    for f in glob.glob("machine-learning/*/*/README.md", recursive=True):
        if "checkpoint" not in f and not re.match(r"machine-learning/.*README\.md$", f.replace('\\','/')) or True:
            pass
    # better: temas no checkpoint
    for f in glob.glob("machine-learning/*/*/README.md", recursive=True):
        if "checkpoint" in f:
            continue
        # skip etapa READMEs
        if f.count(os.sep) == 2 or f.count('/') == 2:
            continue
        t = leer(f)
        for i in range(1, 7):
            if f"## {i}." not in t:
                errores.append(f"{f}: falta sección ## {i}.")

    # d) Duplicados
    practicas = []
    for f in glob.glob("machine-learning/**/practica.md", recursive=True):
        practicas.append((f, leer(f)))
    for i in range(len(practicas)):
        for j in range(i+1, len(practicas)):
            if practicas[i][1] == practicas[j][1]:
                errores.append(f"contenido idéntico entre {practicas[i][0]} y {practicas[j][0]}")
    recursos = []
    for f in glob.glob("machine-learning/**/recursos.md", recursive=True):
        recursos.append((f, leer(f)))
    for i in range(len(recursos)):
        for j in range(i+1, len(recursos)):
            if recursos[i][1] == recursos[j][1]:
                errores.append(f"contenido idéntico entre {recursos[i][0]} y {recursos[j][0]}")
    # README teoría duplicados
    readmes = []
    for f in glob.glob("machine-learning/*/*/README.md", recursive=True):
        if "checkpoint" in f:
            continue
        readmes.append((f, leer(f)))
    for i in range(len(readmes)):
        for j in range(i+1, len(readmes)):
            if readmes[i][1] == readmes[j][1]:
                errores.append(f"contenido idéntico entre {readmes[i][0]} y {readmes[j][0]}")
    # bloques python idénticos
    bloques = []
    for f in glob.glob("machine-learning/**/*.md", recursive=True):
        t = leer(f)
        for b in re.findall(r"```python\n(.*?)```", t, re.S):
            bloques.append((f, b))
    for i in range(len(bloques)):
        for j in range(i+1, len(bloques)):
            if bloques[i][1] == bloques[j][1] and bloques[i][0] != bloques[j][0]:
                errores.append(f"bloque python idéntico en {bloques[i][0]} y {bloques[j][0]}")

    # e) Frases prohibidas
    prohibidas = ["Desarrollar los conocimientos teóricos y prácticos correspondientes", "Consulta la estructura detallada", "con enfoque práctico y aplicación directa", "Define con tus palabras los conceptos clave del tema"]
    for f in glob.glob("machine-learning/**/*.md", recursive=True):
        t = leer(f)
        for p in prohibidas:
            if p in t:
                errores.append(f"{f}: contiene frase prohibida '{p}'")

    # f) LaTeX en fundamentos matemáticos
    for f in glob.glob("machine-learning/02-fundamentos-matematicos/*/README.md", recursive=True):
        if "checkpoint" in f:
            continue
        t = leer(f)
        latex = re.findall(r'\$\$?.*?\$\$?', t, re.S)
        if len(latex) < 3:
            errores.append(f"{f}: menos de 3 expresiones LaTeX")

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
