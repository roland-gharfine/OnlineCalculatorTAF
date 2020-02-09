from selenium import webdriver
import cv2
import base64
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from logger_def import logger
import os


class framework():
    global Logger
    Logger = logger()
    URL = ""
    canvas = None
    canvasWidth = 0
    canvasHeight = 0
    global driver
    path = "C:/Users/user/PycharmProjects/chromedriver.exe"
    driver = webdriver.Chrome(path)

    def __init__(self):
        Logger.Log("Framework initialized")
        driver.maximize_window()
        driver.set_page_load_timeout(60)
        self.URL = "https://www.online-calculator.com/full-screen-calculator/"
        try:
            driver.get(self.URL)
        except TimeoutException as exception:
            driver.quit()
            driver.close()
            Logger.LogError("[WevDriver] Timeout while loading page " + self.URL)
            exit(5)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//a[@aria-label="dismiss cookie message"]').click()
        iframe = driver.find_element_by_id('fullframe')
        driver.switch_to.frame(iframe)
        self.canvas = driver.find_element_by_id('canvas')
        self.canvasWidth = int(self.canvas.get_attribute("width"))
        self.canvasHeight = int(self.canvas.get_attribute("height"))
        Logger.Log("Starting tests")

    def LoadPage(self):
        if(driver.title != "Full Screen Calculator - Online Calculator"):
            driver.get(self.URL)

    def ClickButton(self, button):
        coordinates = self.getButtonCoordinates(button)
        actionChains = ActionChains(driver)
        actionChains.move_to_element(self.canvas).move_by_offset(coordinates[0], coordinates[1]).click().perform()

    def Verify(self, result):
        actionChains = ActionChains(driver)
        actionChains.move_to_element(self.canvas).perform()
        # get the canvas as a PNG base64 string
        canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", self.canvas)

        # decode
        canvas_png = base64.b64decode(canvas_base64)

        # save to a file
        try:
            with open("result.png", 'wb') as f:
                f.write(canvas_png)
        except IOError:
            Logger.LogError("Test result image file not accessible")
        original = cv2.imread("..\\images\\" + result + ".png")
        new = cv2.imread("result.png")
        difference = cv2.subtract(original, new)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            Logger.Log("Test scenario successful.")
            return True
        else:
            Logger.Log("Test failed.")
            return False

    def getButtonCoordinates(self, button):
        """
        Consider that the calculator is a 6 rows by 5 columns matrix and return the offset accordingly
        Note that the element selection starts in the middle of said element
        """
        coordinates = { "1": [-2*self.canvasWidth/5, 1.5*self.canvasHeight/6],
                        "2": [-1*self.canvasWidth/5, 1.5*self.canvasHeight/6],
                        "3": [0, 1.5*self.canvasHeight/6],
                        "4": [-2*self.canvasWidth/5, 0.5*self.canvasHeight/6],
                        "5": [-1*self.canvasWidth/5, 0.5*self.canvasHeight/6],
                        "6": [0, 0.5*self.canvasHeight/6],
                        "7": [-2*self.canvasWidth/5, -0.5*self.canvasHeight/6],
                        "8": [-1*self.canvasWidth/5, -0.5*self.canvasHeight/6],
                        "9": [0, -0.5*self.canvasHeight/6],
                        "0": [-2*self.canvasWidth/5, 2.5*self.canvasHeight/6],
                        "addition": [self.canvasWidth/5, 2.5*self.canvasHeight/6],
                        "subtraction": [self.canvasWidth/5, 1.5*self.canvasHeight/6],
                        "multiplication": [self.canvasWidth/5, -0.5*self.canvasHeight/6],
                        "division": [self.canvasWidth/5, -0.5*self.canvasHeight/6],
                        "dot": [-1*self.canvasWidth/5, 2.5*self.canvasHeight/6],
                        "plus minus": [0, 2.5*self.canvasHeight/6],
                        "equals": [2*self.canvasWidth/5, 2.5*self.canvasHeight/6],
                        "inverse": [2*self.canvasWidth/5, 1.5*self.canvasHeight/6],
                        "percent": [2*self.canvasWidth/5, -0.5*self.canvasHeight/6],
                        "sqrt": [2*self.canvasWidth/5, -0.5*self.canvasHeight/6],
                        "clear": [2*self.canvasWidth/5, -1.5*self.canvasHeight/6],
                        "MC": [-2*self.canvasWidth/5, -1.5*self.canvasHeight/6],
                        "MR": [-1*self.canvasWidth/5, -1.5*self.canvasHeight/6],
                        "M+": [0, -1.5*self.canvasHeight/6],
                        "M-": [self.canvasWidth/5, -1.5*self.canvasHeight/6]
                       }
        if(coordinates[button]):
            return coordinates[button]
        else:
            Logger.LogError("Button " + button + " coordinates unavailable.")
            raise Exception("Button coordinates unavailable!!")

    def TearDown(self):
        os.remove("result.png")
        driver.close()
        driver.quit()
        Logger.Log("TearDown complete")

