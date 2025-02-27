from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def download_tiktok_video(url):
    # Example TikTok API (Replace with your own method)
    api_url = f"https://api.tikmate.app/api/lookup?url={url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return {"video_url": data.get("videoUrl", "No URL found")}
    return {"error": "Failed to download"}

@app.route("/")
def home():
    return "TikTok Video Downloader API is running!"

@app.route("/download", methods=["GET"])
def download():
    tiktok_url = request.args.get("url")
    if not tiktok_url:
        return jsonify({"error": "TikTok URL is required"}), 400
    
    result = download_tiktok_video(tiktok_url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
