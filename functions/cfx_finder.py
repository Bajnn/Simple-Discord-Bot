# discord.gg/bajn
# discord.gg/bajn
# discord.gg/bajn
# discord.gg/bajn
import requests
def cfx_find(cfxkod: str):
    headers = {
        "User-Agent": "BIG NIGGA DICK",
        "Accept": "TÖNTIGA GRABBAR",
        "Accept-Language": "BIG BENYM",
        "Upgrade-Insecure-Requests": "ON TOP",
    
    }
    url = f"https://servers-frontend.fivem.net/api/servers/single/{cfxkod}"
    response = requests.get(url=url, headers=headers).json()

    data = response.get("Data",  {})
    connected = data.get("connectEndPoints", [])
  

    return "{}".format(*connected)
    
