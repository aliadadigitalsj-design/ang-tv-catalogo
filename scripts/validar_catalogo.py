import json
from pathlib import Path

path = Path("catalog.json")
data = json.loads(path.read_text(encoding="utf-8"))
if not isinstance(data, list):
    raise SystemExit("ERROR: catalog.json debe contener una lista JSON")
seen = set()
for item in data:
    if not isinstance(item, dict):
        raise SystemExit("ERROR: cada elemento del catálogo debe ser un objeto")
    key = item.get("id") or item.get("name") or item.get("title")
    if not key:
        raise SystemExit("ERROR: hay un elemento sin id, name ni title")
    if key in seen:
        raise SystemExit(f"ERROR: identificador duplicado: {key}")
    seen.add(key)
    url = item.get("url")
    if url and not str(url).startswith(("https://", "http://")):
        raise SystemExit(f"ERROR: URL no válida en {key}")
print(f"Catálogo ANG.TV correcto: {len(data)} elemento(s). No se eliminó ni modificó ningún contenido.")
