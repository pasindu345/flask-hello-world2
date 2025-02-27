from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# TikTok Video Downloader Function
def download_tiktok_video(url):
    api_url = f"https://api.tikmate.app/api/lookup?url={url}"  # Example API
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

# Flask entry point for Vercel
def handler(event, context):
    return app(event, context)
