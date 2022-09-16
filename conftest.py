from appium import webdriver


class RemoteDriverCaps:
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "emulator-5554",
        "appPackage": "ge.space.app",
        "appActivity": "com.space.app.app.ui.activity.SPApplicationActivity",
        "ensureWebviewsHavePages": True,
        "nativeWebScreenshot": True,
        "appWaitDuration": 60000,
        "newCommandTimeout": 36000,
        "autoGrantPermissions": True,
        "connectHardwareKeyboard": True

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    driver.implicitly_wait(40)
