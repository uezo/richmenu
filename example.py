""" Usage of RichMenu Manager """
from richmenu import RichMenu, RichMenuManager

# Setup RichMenuManager
channel_access_token = "YOUR_CHANNEL_ACCESS_TOKEN"
rmm = RichMenuManager(channel_access_token)

# Setup RichMenu to register
rm = RichMenu(name="Test menu", chat_bar_text="Open this menu")
rm.add_area(0, 0, 1250, 843, "message", "テキストメッセージ")
rm.add_area(1250, 0, 1250, 843, "uri", "http://imoutobot.com")
rm.add_area(0, 843, 1250, 843, "postback", "data1=from_richmenu&data2=as_postback")
rm.add_area(1250, 843, 1250, 843, "postback", ["data3=from_richmenu_with&data4=message_text", "ポストバックのメッセージ"])

# Register
res = rmm.register(rm, "/path/to/menu.png")
richmenu_id = res["richMenuId"]
print("Registered as " + richmenu_id)

# Apply to user
user_id = "LINE_MID_TO_APPLY"
rmm.apply(user_id, richmenu_id)

# Check
res = rmm.get_applied_menu(user_id)
print(user_id  + ":" + res["richMenuId"])

# # Others
# res = rmm.get_list()
# rmm.download_image(richmenu_id, "/path/to/downloaded_image.png")
# res = rmm.detach(user_id)
# res = rmm.remove(richmenu_id)
# rmm.remove_all()
# res = rmm.get_list()
