# Security-Bot
A discord bot that will have some of the functionalities of an antivirus and more

-----------------------------------------------------------------------------------------------------

THIS BOT DOES NOT SAVE ANY INFORMATION OTHER THAN WHAT IS PUT INTO PASSWORD MANAGER
    - Password manager has yet to be implemented

Information Checkers:
This bot uses information retrieved by API, we did not include any
information that we felt was too sensitive

-----------------------------------------------------------------------------------------------------

Bot Commands:
/checkfile <attatchment> - Attatch a file with the command to check for potential threats
/decode32 <message> - Decrypts a message in base32
/decode64 <message> - Decrypts a message in base64
/emailchecker <email> - Checks for validity, malicious/spam history, and more
/encode32 <message> - Encrypts a message in base32
/encode64 <message> - Encrypts a message in base64
/gethash <hash> - Get information about a hash
/iptoloc <ip address> - Find information about an IP address
/linkchecker <link/url> - Checks link for validity, malicious/spam history, and more
/linkshortener <link/url> - Shortens a given link
/passwordgen <length of password> - Generates a random password of given length
/phonenumchecker <phone number> - Checks phone number for validity, malicious/spam history, and more

-----------------------------------------------------------------------------------------------------

Must Install:
Hikari | Command: py -3 -m pip install -U hikari
Requests | Command: pip install requests
Hikari-Lightbulb | Command: python -m pip install -U hikari-lightbulb
mySQL Connector | Command: pip install mysql-connector-python

-----------------------------------------------------------------------------------------------------

Links to API's used:

Link Checker: https://www.ipqualityscore.com/documentation/malicious-url-scanner-api/overview
Phone Number Checker: https://www.ipqualityscore.com/documentation/phone-number-validation-api/overview
IP Info: https://ipapi.co/
Get Hash Info: https://freerestapi.herokuapp.com/

Need API Key to View Sites:
Malware File Checker: https://www.virustotal.com/api/v3/files
URL Shortener: https://url-shortener-service.p.rapidapi.com/shorten 
Encrypt Base 32: https://freerestapi.herokuapp.com/api/base32?encode=
Decrypt Base 32: https://freerestapi.herokuapp.com/api/base32?decode=
Encrypt Base 64: https://freerestapi.herokuapp.com/api/base64?encode=
Decrypt Base 64: https://freerestapi.herokuapp.com/api/base64?decode=

-----------------------------------------------------------------------------------------------------