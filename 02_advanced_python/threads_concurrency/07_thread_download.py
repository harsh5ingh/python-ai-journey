import threading
import requests
import time

def downlaod(url):
  print(f"Starting download from{url}")
  resp = requests.get(url)
  print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls = [
  "https://unsplash.com/photos/a-pink-water-lily-in-a-pond-with-lily-pads-jiaWnzem67U"
  "https://unsplash.com/photos/green-trees-near-lake-during-daytime-KvVCDvD1_t0"
  "https://unsplash.com/photos/the-sun-is-setting-over-the-ocean-with-rocks-in-the-foreground-Md_-qx-b0-Q"
]

start = time.time()
threads = []

for url in urls:
  t = threading.Thread(target=downlaod, args=(url, ))
  t.start()
  threads.append(t)


for t in threads:
  t.join()

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")