'''
Uses a phone number given by the user to check for any malicious activity
Malicious Phone Number Checker API: https://www.ipqualityscore.com/documentation/phone-number-validation-api/overview

RISK SCORE:
    >= 75 suspicious, previous reputation issues or low risk proxy/VPN
    >= 85 high risk, recent abusive behavior over the past 24-48 hours
    = "high", indicates frequent abusive behavior over the past 24-48 hours
'''
import requests

def format_phone_num(phone_num):    # turns phone number into int
    if isinstance(phone_num, int) == False:
        modified_num = "".join(filter(str.isdigit, phone_num)) # removes non-digit characters
        return modified_num
    else:
        return phone_num

def validate_phone_num_len(phone_num_to_val):  # make sure phone number length is not > 10
    if len(str(phone_num_to_val))-1 > 10:
        print("Not a valid phone number, for best results input a number 10 digits long")
        return False
    return True

def determine_malicious_phone_num(phone_num):
    updated_phone_num = str(format_phone_num(phone_num))
    if validate_phone_num_len(updated_phone_num) != False:
        phone_num = "https://ipqualityscore.com/api/json/phone/Z2SzQ0KYr1WwxPlaSxdysIlXwfX3PcVD/" + updated_phone_num
        response = requests.get(phone_num).json()

        phone_num_info = {
            "Formatted Phone Number": response.get("formatted"),
            "Successful Phone Number Check": response.get("success"),
            "Fraud Score": response.get("fraud_score"),
            "Recent Abuse": response.get("recent_abuse"),
            "Risky": response.get("risky"),
            "Do Not Call List": response.get("do_not_call"),
            "Leaked in Breach or Act of Compromise": response.get("leaked"),
            "Spam Number": response.get("spammer"),
            "Carrier": response.get("carrier"),
            "Prepaid Service Plan": response.get("prepaid"),
            "Line Type": response.get("line_type"),
            "Country": response.get("country"),
            "Region": response.get("region"),
            "City": response.get("city"),
            "Zip code": response.get("zip_code"),
            "Time Zone": response.get("timezone"),
        }
        #print(phone_num_info)
        return "Phone Number: " + phone_num_info["Formatted Phone Number"] + "\nCarrier: " + phone_num_info["Carrier"] + "\nCity: " + phone_num_info["City"] + "\nRegion: " + phone_num_info["Region"] + "\nCountry: " + phone_num_info["Country"] + "\nTime Zone: " + phone_num_info["Time Zone"] + "\nSpam Number: " + str(phone_num_info["Spam Number"]) + "\nLeaked: " + str(phone_num_info["Leaked in Breach or Act of Compromise"]) + "\nRisky: " + str(phone_num_info["Risky"]) + "\nDo Not Call List: " + str(phone_num_info["Do Not Call List"]) + "\nFraud Score: " + str(phone_num_info["Fraud Score"])

#print(determine_malicious_phone_num(13013074602)) # put number here