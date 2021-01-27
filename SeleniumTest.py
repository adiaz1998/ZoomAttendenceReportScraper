from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob
import os
import time

def PyDriveAuthentication(gauth):
    # Load the saved client credentials from the file
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if file is nto found
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh authentication if expired
        gauth.Refresh()
    else:
        # Initialize the saved credentials
        gauth.Authorize()
    # Save credentials to file
    gauth.SaveCredentialsFile("mycreds.txt")

def SendToGoogleDrive(FolderID, drive):
    GoogleSheetFile = ""
    # If the CSVFile contains only 1 file, then execute this command
    if len(os.listdir(os.path.dirname(__file__) + "\CSVFile")) == 1:
        for file in glob.glob('CSVFile/*.csv'):
            GoogleSheetFile = file
    # If the CSV contains more than 1 file, retrieve the most recent file
    else:
        GoogleSheetFile = max(glob.iglob('CSVFile/*.csv'), key=os.path.getctime)
    file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": FolderID}]})
    file1.SetContentFile(GoogleSheetFile)
    file1.Upload()

# The main Selenium script that requires user's inputted username & password to run
def SeleniumScript(username1, password2):
    # Calling the Google Drive Authentication function
    gauth = GoogleAuth()
    PyDriveAuthentication(gauth)

    # Adjusting the options of the ChromeDriver
    chromeOptions = Options()
    chromeOptions.add_experimental_option("prefs",
                                          {"download.default_directory": os.path.dirname(__file__) + "\CSVFile",
                                           "safebrowsing.enabled": "false"})
    driver = webdriver.Chrome(executable_path='Driver/chromedriver.exe', options=chromeOptions)

    driver.get('https://rutgers.zoom.us/')

    driver.find_element_by_link_text("Sign in").click()

    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys("", username1)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("", password2)

    driver.find_element_by_class_name('btn-submit').click()

    driver.find_element_by_css_selector("a[href='https://rutgers.zoom.us/account/report']").click()
    driver.find_element_by_css_selector("a[href='https://rutgers.zoom.us/account/my/report']").click()

    driver.find_element_by_xpath('//*[@id="searchMyForm"]/div/button[1]/img').click()

    driver.find_element_by_xpath('//*[@id="searchMyForm"]/div/button[2]/img').click()

    day = driver.find_element_by_xpath( "//*[@id='ui-datepicker-div']/table/tbody/tr/td[contains(@class,' ui-datepicker-days-cell-over  ui-datepicker-current-day ui-datepicker-today')]").text

    day = int(day)

    driver.find_element_by_xpath('//*[@id="searchMyForm"]/div/button[1]/img').click()

    # If the day in the calendar web app is more than 7, execute this script
    if day > 7:
        newday = day - 7
        newday = str(newday)
        Command1 = "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[contains(text(),'"
        Command2 = "')]"
        FullCommand = Command1 + newday + Command2
        driver.find_element_by_xpath(FullCommand).click()
    # If the day in the calendar web app is less than 7, change the calen9dar to the previous month and execute this
    # script
    else:
        driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[1]/a[1]').click()
        newdate = 20 + day
        newdate = str(newdate)
        Command1 = "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[contains(text(),'"
        Command2 = "')]"
        FullCommand = Command1 + newdate + Command2
        driver.find_element_by_xpath(FullCommand).click()

    # Clicks the Search button
    driver.find_element_by_id("searchMyButton").click()

    # Find and select the last item in that list
    driver.find_element_by_xpath('//*[@id="meeting_list"]/tbody/tr[last()]/td[12]/a').click()

    # Wait a few seconds
    driver.implicitly_wait(10)

    # Click unique users (if available)
    VerifyUniqueUsers = driver.find_element_by_xpath('//*[@id="selectUniqueDiv"][contains(@style,"display: none;")]')
    if VerifyUniqueUsers:
        pass
    else:
        VerifyUniqueUsers.click()

    # Find the button to export the attendance sheet and download it
    driver.find_element_by_xpath("//*[@id='btnExportParticipants']").click()

    drive = GoogleDrive(gauth)

    FolderID = '1xSP296-9AyZ32QONx4zfpv0ScDNOHKAW'

    time.sleep(3)
    SendToGoogleDrive(FolderID, drive)
