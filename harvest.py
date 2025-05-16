import re
import requests
import os

playlist_js_url = "https://www.feynmanlectures.caltech.edu/flptapes.js"

if not os.path.exists("flptapes.js"):
    print("Downloading flptapes.js ...")
    js_headers = {
        'sec-ch-ua-platform': '"macOS"',
        'Referer': 'https://www.feynmanlectures.caltech.edu/flptapes.html',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'DNT': '1',
    }
    resp = requests.get(playlist_js_url, headers=js_headers, verify=False)
    with open("flptapes.js", "w") as f:
        f.write(resp.text)
    print("Saved flptapes.js")

# NEW: Read the JS text from file
with open("flptapes.js", "r") as f:
    js_text = f.read()

# Extract all "m4a" MP4 links
mp4_rel_links = re.findall(r'm4a:\s*[\'"]([^\'"]+\.mp4)[\'"]', js_text)
mp4_links = ["https://www.feynmanlectures.caltech.edu/" + link for link in mp4_rel_links]

print(f"Found {len(mp4_links)} audio files.")

headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://www.feynmanlectures.caltech.edu/flptapes.html',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'DNT': '1',
    'Range': 'bytes=0-'
}

outdir = "feynman_audio"
os.makedirs(outdir, exist_ok=True)

for url in mp4_links:
    fname = os.path.join(outdir, url.split("/")[-1])
    print(f"Downloading {fname} ...")
    resp = requests.get(url, headers=headers, stream=True, verify=False)
    if resp.status_code in (200, 206):
        with open(fname, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Saved {fname}")
    else:
        print(f"Failed to download {fname}: HTTP {resp.status_code}")

print("Done.")