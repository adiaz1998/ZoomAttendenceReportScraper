# Zoom Attendence Sheet Scraper for ALPFA Rutgers-Newark
GUI application that automates the process of downloading attendance reports from Zoom and uploads them on a shared Google Drive folder.



<p align="center">
<img src="https://i.imgur.com/SnCOGna.png">
</p>

# Description
This desktop application is intended for the use of the executive board of the student organization, ALPFA Rutgers-Newark. It is meant to send attendence reports from virtual events that we have conducted via Zoom to validate who attended them. Participation to our events is crucial as it is one of the factors that contributes to our Point System (each student is awareded a specific amount of points if they participate in one of our events, assuming they're there 75% of its duration).

# Purpose
This application was devleoped because as the VP of IT for ALPFA Rutgers-Newark, it is one of my duties to automate & streamline the processes of my fellow executive board. This project was intended to utilize the Zoom API. However, any usage of the Zoom API from a Rutgers-sponsored Zoom account is prohibited. Therefore, I was forced to create a Selenium script that access the Rutgers-sponsored Zoom website & download attendance reports from the latest meeting we have conducted.

# How Does It Work?
The project uses the following libraries:
  <li>Selenium</li>
  <li>Tkinter</li>
  <li>PyDrive</li>
  <li>glob</li>
  <li>OS</li>
<br>
A selenium script has been encapsulated into a function that utilizes the Chromedriver.exe automation software to access the http://www.rutgers.zoom.us website. The user must input their Rutgers netID and password in a Tkinter GUI, which will be passed on as arguments to the selenium function. If it's the first time the user has accessed the application, they will be redirected to Google where they must authenicate the application to access their Google Drive, as part of PyDrive. Their credentials will be stored in a text file, so the authentication process won't loop. The script will then be executed on ChromeDriver and an attendance report will be downloaded onto the user's Downloads folder. A function has been developed that accesses the recent .CSV file from the Downloads folder using functions from bot the glob & OS libraries where they will be finally uploaded into a folder on Google Drive in which all members of the executive board have access to. 
<br>
<br>Additionally, the python application was converted as an .exe file using PyInstaller 4.1 so that users who do not have Python installed can utilize it. 
