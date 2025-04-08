# 文生图模型
#"revised_prompt":"Create an image of a book cover for the epic 'Homer's Odyssey'. Incorporate elements of Greek mythology like a silhouette of Odysseus and his crew, confronting mythical creatures such as Cyclops and Sirens, all against a backdrop of turbulent seas and sinister cliffs. Engrave the title in ancient Greek lettering at the top, implying an ancient parchment's texture. The overall design should seem like a classical, ancient artifact. Color scheme should comprise mainly sepia tones to give it a worn, historical look."

import http.client
import json
import requests

key = "sk-"  # ChatAnywhere API Key
# 生成图像
conn = http.client.HTTPSConnection("api.chatanywhere.tech")
payload = json.dumps({
   "prompt": "奥德赛的弓的特写",
   "n": 1,
   "model": "dall-e-3",
   "size": "1024x1024"
})
headers = {
   'Authorization': f'Bearer {key}',
   'Content-Type': 'application/json'
}
conn.request("POST", "/v1/images/generations", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
response_json = json.loads(data.decode("utf-8"))
image_url = response_json['data'][0]['url']

print(f"生成的图像URL: {image_url}")

# 下载图像
img_data = requests.get(image_url).content

# 保存到本地
with open('image.jpg', 'wb') as f:
    f.write(img_data)
