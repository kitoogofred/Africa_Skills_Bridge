from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def test_assets():
 assert all((ROOT/"assets"/f"figure_{i}.png").stat().st_size>1000 for i in range(10,20))
def test_manifest_if_present():
 p=ROOT/"data"/"release_manifest.json"
 if p.exists():
  d=json.loads(p.read_text());assert isinstance(d,dict) and "version" in d
