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
- **Title:** #Title#
  - Use # on either side of the desired title of your picture to have it be named such when uploaded. For example #Kansas Map.jpg#  would appear as Kansas Map.jpg in Google Drive. The title is found from only the first set of words found within 2 hashtags, so make sure the title is placed near the top of the page.
- **Folder:** %Folder%
  - This command is similar to the title command, but instead of #, % must be used. For example %Math% will cause the file to be sent to the folder labeled Math in Google Drive. Much like with title, the folder is found from only the first set of words found between 2 percent symbols, so ensure that the folder is placed near the top of the page. 
- **Translate:**  ??lang??
  -Unlike the other 2 commands, to set the language to which you want the document to be translated to, you must place the language between 2 question marks on either side. This is due to the question mark being commonly used in writing. The original document language is not required to be given as SmartBook software can automatically determine the original language. Once again like with the tags for title, and folder. Attempt to put the translate tag near the top of the document. 


### Processing Pictures
![Picture of processing pictures screen](https://imgur.com/dYqZqYf.jpg)
Once you have a picture to process you can upload it to this screen and then choose an action to perform on it.
- **Upload as Text:** Converts as much of the picture as it can to text and uploads it to your Google Drive in the specified folder and title. If no title is provided the filename is used and if no folder is provided the file is put in your general drive.
- **Upload as File:** Uploads the file straight to your Google Drive. If no title is provided the filename is used and if no folder is provided the file is put in your general drive.
- **Upload Translated Text:** Converts the file into text and then translates into the chosen language. The initial language is determined by the app so it does not need to be inputted. If no title is provided the filename is used and if no folder is provided the file is put in your general drive.
- **Read Text Out Loud:** Converts the file into text and then makes an MP3 recording of the text. The MP3 recording can be downloaded but is not uploaded to Google Drive.
- **Read Text Out Loud and Then Upload Recording:** Converts the file into text and then makes an MP3 recording of the text. The MP3 recording can be downloaded and is uploaded to Google Drive. If no title is provided the filename is used and if no folder is provided the file is put in your general drive.
- **Read Translation Out Loud:** Converts the file into text and then translates into the chosen language. The MP3 recording can be downloaded but is not uploaded to Google Drive. 
- **Read Translation Out Loud and Then Upload Recording:** Converts the file into text and then translates into the chosen language. The MP3 recording can be downloaded and is uploaded to Google Drive. If no title is provided the filename is used and if no folder is provided the file is put in your general drive.

## Future Plans
The goal is to incorporate all of the features of the prototype into a smartphone app. This app would make the process even more efficient as a high quality picture could be taken directly with the phone. It would also let the UI be much more pleasent and simple to use.

