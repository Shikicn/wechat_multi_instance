import winreg
import subprocess

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        self.app_name = "WeChat.exe"
        
    def get_wechat_path(self):
        reg_path = f"SOFTWARE\Tencent\WeChat"
        value_name = "InstallPath"
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ) as key:
                return winreg.QueryValueEx(key, value_name)[0] + f"\{self.app_name}"
        except FileNotFoundError:
            return None          
        
        
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
        
    def open_wechat(self, evt):
        app_path = self.get_wechat_path()
        number = 0
        try:
            number = (int)(self.ui.tk_text_m27qkagn.get(1.0, "end"))
            for i in range(number):
                subprocess.Popen(app_path)
        except ValueError:
            pass        
        