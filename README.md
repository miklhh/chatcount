# chatcount
Count messages and characters sent between you and your friends through Facebook Messenger. This tool analysises a facebook JSON data collection file and shows a summary of all messages sent and recieved.

## Example output.
![Example](resources/4.png)

## Usage
Start of by producing a Facebook compilation JSON file from Facebook. While signed in to your Facebook account, do the following:

1. Go to `Settings -> Your Facebook information -> Download your information`.
![Step1](resources/1.png)

2. Select settings: *Date range: __All of my data__*; *Format: __JSON__*; *Media quality: __Medium__*.
![Step2](resources/2.png)

3. Make sure that *Messages* are selected in the list *Your information*.
![Step3](resources/3.png)

4. Click __Create file__ and wait for Facebook to create the compilation file. Once the file is completed you will get a notification through Facebook. Download the generated zipfile and place it in the repository root directory.

5. Invoke the python-script *chatcount.py* with the generated zipfile as commandline argument, example: `./chatcount.py examplename123.zip`. If you are unable to run the script you might have to mark it as executable by invoking `chmox +x chatcount.py`. The result is printed throught standard out.
