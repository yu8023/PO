from selenium.webdriver.common.by import By

"""
    搜索页面
"""
# 搜索按钮
search_button = (By.ID, "com.android.settings:id/search")
# 搜索输入框
search_input = (By.ID, "android:id/search_src_text")
# 搜索框返回按钮
search_return_button = (By.CLASS_NAME, "android.widget.ImageButton")

"""
    短信页面
"""
# 短信页的+号按钮
add_button = (By.ID,"com.android.messaging:id/start_new_conversation_button")
# 收件人
rec_person = (By.ID,"com.android.messaging:id/recipient_text_view")
# 短信内容
input_sms = (By.ID,"com.android.messaging:id/compose_message_text")
# 发送按钮
send_button = (By.ID,"com.android.messaging:id/self_send_icon")

"""
    开发者头条
"""
# 新建文章按钮
dev_add_title = (By.ID,"io.manong.developerdaily:id/tab_bar_plus")
# 选择密码登录
dev_login_pwd = (By.XPATH,"//*[contains(@text,'密码登录')]")
# 手机号码输入
dev_input_phone = (By.ID,"io.manong.developerdaily:id/edt_phone")
# 密码输入
dev_input_pwd = (By.ID,"io.manong.developerdaily:id/edt_password")
# 登录按钮
dev_login_btn = (By.ID,"io.manong.developerdaily:id/btn_login")
"""
    联系人
"""
# 添加按钮
add_p = (By.ID,"com.android.contacts:id/floating_action_button")
# 本地保存
left_button = (By.ID,"com.android.contacts:id/left_button")
# 输入姓名
name_input = (By.XPATH,"//*[contains(@text,'姓名')]")
# 输入电话
phone_input = (By.XPATH,"//*[contains(@text,'电话')]")
# 保存按钮
save_button = (By.ID,"com.android.contacts:id/menu_save")
# 定位用户详情页面编辑按钮
user_edit_btn = (By.ID,"com.android.contacts:id/menu_edit")