"""Check every URL in sources/*.json and write link_status.json."""
import glob, json, re, subprocess, concurrent.futures, pathlib

URL_RE = re.compile(r"^https?://")

def collect():
    urls = {}
    for f in sorted(glob.glob(str(pathlib.Path(__file__).parent / "batch*.json"))):
        for person, rec in json.load(open(f)).items():
            for key, val in rec.items():
                if isinstance(val, str) and URL_RE.match(val):
                    urls.setdefault(val, []).append(f"{person}:{key}")
    return urls

def check(url):
    try:
        out = subprocess.run(
            ["curl", "-sSL", "-o", "/dev/null", "-w", "%{http_code}",
             "--max-time", "25", "--retry", "1",
             "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/125.0 Safari/537.36",
             url],
            capture_output=True, text=True, timeout=60)
        return url, out.stdout.strip() or "ERR"
    except Exception as e:
        return url, f"ERR:{type(e).__name__}"

if __name__ == "__main__":
    urls = collect()
    print(f"checking {len(urls)} unique URLs")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
        for url, code in ex.map(check, urls):
            results[url] = {"status": code, "used_by": urls[url]}
    out = pathlib.Path(__file__).parent / "link_status.json"
    out.write_text(json.dumps(results, indent=1))
    from collections import Counter
    print(Counter(r["status"] for r in results.values()).most_common())
