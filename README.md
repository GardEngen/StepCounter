# Step Counter

This project contains a simple Android application for tracking your steps 
and a Python program for plotting a graph of your progress.
When everything is up and running will the Android application update the graf on the fly. 
The application will send your step count progress for each you connect the phone to power.
The graph will automatically show the latest results.

![alt text](images/screenshot.png "Description goes here")

## Getting Started

### Connect your Google Firebase to the application

In order for this to work, you have to create a new Google Firebase project in the [console](https://console.firebase.google.com/).
```
https://console.firebase.google.com/ 
```
The next stap is to connect Firebase and the Andorid application. Click on **Add Firebase to your Android app**. In order to complete this connection you have to provide the unique package name of the Android application. It's located in the build.gradle as applicationId. The package name for this project:
```
com.gardengen.assignment_1
```

Once this is done, you have to download and add the **google-services.json** to the project. This file contains your app configuration. It should be placed in your Andorid app directory.

### Setup Firebase Realtime Database Rules
Since this project is for test purposes only, just set read and write to true. This will allow all useres to read and write data in the database.
Navigate to Database -> RULES and set read/write to true. 
```
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
Now will the database store every new step count sendt from the Android application.

### Setup Python project
The first thing you have to do is to pip install all the project dependencies in your environment. Navigate to the project directory and use the following command:
```
pip install -r requirements.txt
```
In app.py is there config variable used for initializing pyrebase. This is the library used for reading data from Google Firebase. Add your Google Firebase projects credentials like this:
```
config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}
```
Run the python project with this command:
```
python app.py
```
If you have followed all the steps and app.py is running, then you can go to [this](http://127.0.0.1:8050/) site and watch the graph automaticly plot every new step count added to the database.



