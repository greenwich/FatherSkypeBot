FatherSkypeBot
==============

Father skype bot - initially used for fun and job duties. Shared to github because of people requests.

Simple python skype bot.

Requirements:
=============
  * python 2.7 x86 installed
  * pywin32
  * skype4py module
  * pyyaml
  
Installation
============
  
  1. Install skype on the the machine where you will execute Father skype bot from
  2. Install modules from requirements paragraph (TODO: make dependencies resolving script)
  3. Create new folder and clone skype bot files from the (TODO: make installer: py or exe)
  4. Select a chat you want to join and put its id in chat_id setting in config.yaml (to be honest dunno how you will know your chat id without debugging:) TODO: fix it)
  5. Run Father bot
  6. Skype will popup about external application (python.exe) wants to access Skype - allow it ![Popup example](https://c.mql5.com/18/10/Access.png)
  

TODO
====
1. Add doctest tests
2. Interactive menu to allow user to select the chat to join
3. Dependencies resolution script
4. Installer: py or exe
5. Add data mining plugin (for example: detect most popular topics, persons and words). Try to define the chat topic and predict it
6. Simple linguistic analysis ....
7. blah blah
  
