import requests

url = "https://backend-simulator-321936462778.us-central1.run.app/download"
output_path = "downloaded_result.zip"

response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"✅ ZIP file saved as {output_path}")
else:
    print(f"❌ Failed to download. Status code: {response.status_code}")
