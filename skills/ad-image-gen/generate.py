#!/usr/bin/env python3
"""
Generate a Meta ad image with gpt-image-2 (OpenAI) or Nano Banana Pro (Google Gemini).

Usage:
  python3 generate.py --model gpt-image-2 --prompt "..." --size 1088x1360 --out ad.png [--ref face.jpg]
  python3 generate.py --model nano-banana-pro --prompt "..." --ratio 4:5 --out ad.png [--ref face.jpg]

Keys are read from the environment, then from ~/.claude/ad-profiles/.env (outside this skill folder, never committed):
  OPENAI_API_KEY   for gpt-image-2
  GEMINI_API_KEY   for nano-banana-pro

No third-party packages required (urllib only).
"""
import argparse, base64, json, mimetypes, os, sys, urllib.request, urllib.error
from pathlib import Path

GEMINI_MODELS = {
    "nano-banana-pro": "gemini-3-pro-image",
}

def load_env_file():
    p = Path.home() / ".claude" / "ad-profiles" / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

def need(key):
    v = os.environ.get(key)
    if not v:
        sys.exit(f"Missing {key}. Add it to your shell env or to ~/.claude/ad-profiles/.env")
    return v

def post(url, headers, body, timeout=300):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:800]}")

def openai_generate(prompt, size, out, ref, quality):
    key = need("OPENAI_API_KEY")
    if ref:
        # images.edit with a reference image (multipart)
        boundary = "----adimg"
        parts = []
        def field(name, value):
            parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode())
        field("model", "gpt-image-2"); field("prompt", prompt); field("size", size); field("quality", quality)
        field("input_fidelity", "high")
        data = Path(ref).read_bytes()
        mime = mimetypes.guess_type(ref)[0] or "image/png"
        parts.append((f"--{boundary}\r\nContent-Disposition: form-data; name=\"image[]\"; filename=\"{Path(ref).name}\"\r\nContent-Type: {mime}\r\n\r\n").encode() + data + b"\r\n")
        parts.append(f"--{boundary}--\r\n".encode())
        body = b"".join(parts)
        res = post("https://api.openai.com/v1/images/edits",
                   {"Authorization": f"Bearer {key}", "Content-Type": f"multipart/form-data; boundary={boundary}"}, body)
    else:
        body = json.dumps({"model": "gpt-image-2", "prompt": prompt, "size": size, "quality": quality, "n": 1}).encode()
        res = post("https://api.openai.com/v1/images/generations",
                   {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, body)
    b64 = res["data"][0]["b64_json"]
    Path(out).write_bytes(base64.b64decode(b64))

def gemini_generate(model_key, prompt, ratio, out, ref):
    key = need("GEMINI_API_KEY")
    model = GEMINI_MODELS[model_key]
    parts = [{"text": prompt}]
    if ref:
        data = base64.b64encode(Path(ref).read_bytes()).decode()
        mime = mimetypes.guess_type(ref)[0] or "image/png"
        parts.insert(0, {"inline_data": {"mime_type": mime, "data": data}})
    body = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": ratio}},
    }).encode()
    res = post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
               {"x-goog-api-key": key, "Content-Type": "application/json"}, body)
    for cand in res.get("candidates", []):
        for p in cand.get("content", {}).get("parts", []):
            if "inlineData" in p:
                Path(out).write_bytes(base64.b64decode(p["inlineData"]["data"]))
                return
    sys.exit("No image returned. Response: " + json.dumps(res)[:800])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gpt-image-2", choices=["gpt-image-2", "nano-banana-pro"])
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ref", help="reference image (face or product)")
    ap.add_argument("--size", default="1088x1360", help="gpt-image-2 pixel size, multiples of 16 (4:5 = 1088x1360, 1:1 = 1024x1024, 9:16 = 1088x1920)")
    ap.add_argument("--ratio", default="4:5", help="Nano Banana aspect ratio (1:1, 4:5, 9:16, 16:9)")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    a = ap.parse_args()
    load_env_file()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    if a.model == "gpt-image-2":
        openai_generate(a.prompt, a.size, a.out, a.ref, a.quality)
    else:
        gemini_generate(a.model, a.prompt, a.ratio, a.out, a.ref)
    print(a.out)

if __name__ == "__main__":
    main()
