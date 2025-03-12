import requests

# DeepSeek API 的 URL
api_url = "https://openrouter.ai/api/v1/chat/completions"

# 你的 API 密钥
api_key = "sk-05a16ef52ec14a3eb307f5c80da3ccd7"

# 请求头，包含 API 密钥
headers = {
    "Authorization": f"Bearer sk-05a16ef52ec14a3eb307f5c80da3ccd7",
    "Content-Type": "application/json"
}

# 请求体，根据 API 文档填写
payload = {
    "model": "deepseek-reasoner",
    "messages": [{"role": "user", "content": "你好"}]
}

# 发送 POST 请求
response = requests.post(api_url, headers=headers, json=payload)

# 检查响应状态码
if response.status_code == 200:
    # 解析响应内容
    data = response.json()
    print("Response:", data)
else:
    print(f"Failed to fetch data: {response.status_code}")
    print("Response:", response.text)