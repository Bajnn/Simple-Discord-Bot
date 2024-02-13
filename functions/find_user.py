import requests

def find_user(discord_id: int):
    url = f"https://discordlookup.mesavirep.xyz/v1/user/{discord_id}"
    response = requests.get(url)

    json_data = response.json()
    created_at = json_data.get("created_at", [])
    global_name = json_data.get("global_name", [])
    avatar = json_data.get("avatar", {})
    banner = json_data.get("banner", {})
    avatar_link = avatar.get("link")
    banner_link = banner.get("link")
    return f"\ncreation_Date:[{created_at}] \nglobal_Name: [{global_name}] \navatar: [{avatar_link}] \nbanner: [{banner_link}]"