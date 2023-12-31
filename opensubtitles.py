import requests
import xmlrpc.client

# API URL and login credentials (replace with your own)
api_url = "https://api.opensubtitles.org/xml-rpc"
username = "your_username"
password = "your_password"
user_agent = "YourAppName/1.0"  # Replace with your application name

# Create XML-RPC client
client = xmlrpc.client.ServerProxy(api_url)

# Login to the API
token = client.LogIn(username, password, "en", user_agent)["token"]

# Example usage: Search for subtitles by movie hash
movie_hash = "1234567890abcdef1234567890abcdef"  # Replace with the actual movie hash
subtitle_list = client.SearchSubtitles(token, [{"sublanguageid": "eng", "moviehash": movie_hash}])

# Print search results
if subtitle_list["data"]:
    for subtitle in subtitle_list["data"]:
        print(f"ID: {subtitle['IDSubtitleFile']}\nLanguage: {subtitle['LanguageName']}\nDownload link: {subtitle['SubDownloadLink']}\n")
else:
    print("No subtitles found.")

# Download a subtitle file (uncomment and replace IDSubtitleFile)
# subtitle_id = 123456789  # Replace with the subtitle ID
# download_result = client.DownloadSubtitles(token, [subtitle_id])
# if download_result["status"] == "200 OK":
#     with open("downloaded_subtitle.zip", "wb") as f:
#         f.write(base64.b64decode(download_result["data"][0]["data"]))
# else:
#     print("Error downloading subtitle:", download_result["status"])
