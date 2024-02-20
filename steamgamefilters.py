import requests

# 您的Steam API密钥
steam_api_key = "2408F29A1D63072285E3E619A858F571"

# 获取Galgame游戏列表
def get_galgame_list():
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/?key={steam_api_key}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        app_list = data["applist"]["apps"]
        galgame_list = []
        for app in app_list:
            appid = app["appid"]
            app_details_url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
            app_details_response = requests.get(app_details_url)
            if app_details_response.status_code == 200:
                app_details_data = app_details_response.json()
                if app_details_data[str(appid)]["success"]:
                    app_data = app_details_data[str(appid)]["data"]
                    if "genres" in app_data and any(genre["description"].lower() == "sexual content" for genre in app_data["genres"]):
                        galgame_list.append(app_data)
        return galgame_list
    else:
        print("Failed to get Galgame list. Response:", response.text)
        return []

if __name__ == "__main__":
    galgame_list = get_galgame_list()
    for game in galgame_list:
        print(game["name"])
