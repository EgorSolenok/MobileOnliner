# Testing Mobile Web Project https://onliner.by
**PythonTestAutomationFramework**

**Description**

Test Mobile WEB (Android) Automation Framework of "https://onliner.by" using Python + Appium.



* Framework is based on Page Object Model. 
* Allure reporting.
* Logging to external file.
* Framework can use emulator and real device as well.

The project is being developed during the iTechArt internship.

# How to install it
Make sure you have python3.10 installed on your machine by typing in cmd ``python3 -version`` if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1) Clone the repository to any local path.

``$ git clone https://github.com/EgorSolenok/TestingMobileOnliner.git``

2) Make sure you have  allure command line  by typing in cmd ``allure --version``. If not - you have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3) Make sure you have pipenv  by typing in cmd ``pipenv --version``. If not - you have to install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/  

``$ pip install --user pipenv``

4) Install dependencies:

``$ pipenv install``

5) Make sure you have **adb**:

``$ adb --version ``

Or install it: `` https://developer.android.com/studio/command-line/adb ``

6) Make sure your device(emulated or real) connected to adb by type:

``$ adb devices``

6) Make sure you have **appium** or **Appium Server GUI**:

``$ appium -v `` and run the server:

``$ appium `` 

# How to run it

**For all tests running you should type commands in root directory.**

To run all tests and create report:

``  pipenv run python -m pytest  --tb=line --alluredir=report_data ``

To create **Allure report** and open it - type in cmd being located in the folder path:

``allure serve report_data``

**Logging**

To read logs you should go to logs folder and read files.
