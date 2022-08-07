# SmartBook Prototype
*This is the code for my prototype version of SmartBook. The actual Android app is still currently under development. SmartBook utilizes Google Cloud technology to process handwritten notes in a time efficient manner*
## How to set up the prototype
1) First clone the repository into your own storage. 
2) Get a client_secrets.json file. [This link can help if you don't know how to.](https://help.talend.com/r/en-US/7.2/google-drive/how-to-access-google-drive-using-client-secret-json-file-the)
3) Get a Google Cloud API key. [This link can help you out.](https://cloud.google.com/docs/authentication/api-keys#:~:text=To%20create%20an%20API%20key,displays%20your%20newly%20created%20key.)
4) Put your client_secrets.json file in the directory folder. It should not be within any other folders like the file in the picture below.
![Picture of client_secrets.json](https://imgur.com/BwGqyWe.jpg)
5) Store the filepath of the file containing the Google Cloud API key in an environment variable called GOOGLE_APPLICATION_CREDENTIALS.
6) Open up powershell or cmd in the general directory folder (same folder as where you have client_secrets.json
7) Type in the following command into the command prompt: `py manage.py runserver`. *Note this command might change slightly depending on operating systems. The assumption is that this will work on Windows.*
8) After doing this you should be redirected by google to an authentication screen. Make sure you sign into the Google account that you used to get the API keys or an account you approved for testing purposes.
9) To find your website you can go back to the command line and it should say something like `Starting development server at http://127.0.0.1:8000/` that will give you the address of the prototpe.

## How to use the prototype
### Taking a Picture
!{Picture of taking picture screen](https://imgur.com/vk5sAki.jpg)
Once you get to the website of the prototype, the initial screen you will see is one where you can take a picture with your webcam. On this screen you can take picture of the writing you would like to process. It is recommended for best results to take pictures of notes with a different device and send them to your computer, for camera quality of webcams are shoddy and will lead to errors in processing. Once you taken a picture of if you have a picture already on your computer you can click the "Go to processing" button.
#### Tricks for Photos
*To help in processing do these following things on pictures you want to process.*
-**Title #Title#**
-- Use # on either side of the desired title of your picture to have it be named such when uploaded. For example #Kansas Map.jpg#  would appear as Kansas Map.jpg in Google Drive. The title is found from only the first set of words found within 2 hashtags, so make sure the title is placed near the top of the page.

### Processing Pictures
![Picture of processing pictures screen](https://imgur.com/dYqZqYf.jpg)
Once you have a picture to process you can upload it to this screen and then choose an action to perform on it.
-**Upload as Text:** Converts as much of the picture as it can to text and uploads it to your Google Drive
-

