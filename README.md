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
<li>
  <ul>Selenium</ul>
  <ul>Tkinter</ul>
  <ul>PyDrive</uL>
