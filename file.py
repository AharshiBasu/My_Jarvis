import os
import webbrowser

# os.startfile("C:\\Users\\amitb\\AppData\\Local\\Programs\\Arduino IDE\\Arduino IDE.exe")

# os.startfile("C:\\Users\\amitb\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\BlueJ\\BlueJ.lnk")

# os.startfile("Calc.exe")

#os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")

# os.startfile("NotePad.exe")

# os.startfile("Excel.exe")

# os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

# os.startfile("whatsapp:")

# webbrowser.open("https://classroom.google.com/h")

# webbrowser.open("https://www.amazon.in/?ref=icp_country_us_t1")

# webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

# os.startfile("C:\\Users\\amitb\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Win")

# os.system("start cmd")

# check of os functions

# import os

# print("1. Restart")
# print("2. Sleep")
# print("3. Shutdown")
# print("4. Lock")

# choice = input("Choose: ")

# if choice == "1":
#     os.system("shutdown /r /t 0")
# elif choice == "2":
#     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
# elif choice == "3":
#     os.system("shutdown /s /t 0")
# elif choice == "4":
#     os.system("rundll32.exe user32.dll,LockWorkStation")
# else:
#     print("Invalid choice")

import subprocess

powershell = r'''
Get-Process | Where-Object {
    $_.MainWindowHandle -ne 0 -and
    $_.ProcessName -notin @("Code", "python", "pythonw")
} | ForEach-Object {
    $_.CloseMainWindow() | Out-Null
}
'''

subprocess.run(["powershell", "-NoProfile", "-Command", powershell])
