@echo off

for /f "tokens=3*" %%i in ('reg query "HKEY_CURRENT_USER\SOFTWARE\Tencent\WeChat" /v InstallPath') do (
	set "wechatDir=%%i\"
)

set wechatPath="%wechatDir%WeChat.exe"

:: count变量用来保存要打开的微信的个数, 例：改为3可以启动3个微信
set count=2
for /L %%i in (1, 1,  %count%) do (
	start "" "%wechatPath%"
)