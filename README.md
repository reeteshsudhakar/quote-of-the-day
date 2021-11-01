# Quote of the Day
I've recently spent quite a bit of time looking through motivational quotes on my Instagram feed, and I felt inspired to find something that would automate the process and make it so that the quotes would come to me. This project sends you a motivational text to your phone number and/or email from the Affirmations API. 

## Project Setup 
First, run the following in the command line or terminal to set up the requirements: 

`pip install -r requirements.txt`

Next, retrieve `credentials.json` from the Gmail API in order to configure emailed messages, and add it to the folder. 

Next, configure your settings in `info.py` to have the messages sent to your relevant accounts when the script is run: 
```py
phone = '##########' # enter your phone number here 
email = 'example@gmail.com' # enter your email here 

carriers = {
    "verizon": "@vtext.com",
    "att": "@txt.att.net",
    "sprint": "@messaging.sprintpcs.com",
    "tmobile": "@tmomail.net",
    "uscellular": "@email.uscc.net",
    "boost": "@myboostmobile.com",
    "cricket": "@sms.mycricket.com",
    "metroPCS": "@mymetropcs.com",
    "nextel": "@messaging.nextel.com",
    "qwest": "@qwestmp.com"
} # these are the following carriers that this program will support. 

mac = False # determines whether the message should be sent via SMS or iMessage. Set to True for iOS (iMessage), and False for SMS. 
carrier = carriers["att"] # enter your desired carrier here, as written in carriers. 
```
Now, you're ready to run the script! Run the following command: 

`python main.py`

## To-Do List
- [x] Update README.md
- [x] Check Requirements.txt
- [ ] Integrate quotes from [Zen Quotes API](https://zenquotes.io)
- [ ] Update List of Carriers
- [ ] Add RegEx Validation for email and phone numbers.   
