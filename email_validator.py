'''
Uses a phone number given by the user to check for any malicious activity
Malicious Phone Number Checker API: https://www.ipqualityscore.com/documentation/phone-number-validation-api/overview

RISK SCORE:
    >= 75 suspicious, previous reputation issues or low risk proxy/VPN
    >= 85 high risk, recent abusive behavior over the past 24-48 hours
    = "high", indicates frequent abusive behavior over the past 24-48 hours
'''
import requests

def determine_malicious_email(email):
    url_email = "https://ipqualityscore.com/api/json/email/Z2SzQ0KYr1WwxPlaSxdysIlXwfX3PcVD/" + email
    response = requests.get(url_email).json()

    email_info = {
        "Valid": response.get("valid"),
        "Disposable": response.get("disposable"),
        "Timed out": response.get("timed_out"),
        "Deliverability": response.get("deliverability"),
        "Leaked": response.get("leaked"),
        "Catch All": response.get("catch_all"),
        "Suspect": response.get("suspect"),
        "SMTP Score": response.get("smtp_score"),
        "Overall Score": response.get("overall_score"),
        "DNS Valid": response.get("dns_valid"),
        "Honeypot": response.get("honeypot"),
        "Spam Trap Score": response.get("spam_trap_score"),
        "Recent Abuse": response.get("recent_abuse"),
        "Fraud Score": response.get("fraud_score"),
    }
    return "Email Address: " + email + "\nValid: " + str(email_info["Valid"]) + "\nDisposable: " + str(email_info["Disposable"]) + "\nDNS Valid: " + str(email_info["DNS Valid"]) + "\nDeliverability: " + email_info["Deliverability"] + "\nLeaked: " + str(email_info["Leaked"]) + "\nCatch All: " + str(email_info["Catch All"]) + "\nSuspect: " + str(email_info["Suspect"]) + "\nHoneypot: " + str(email_info["Honeypot"]) + "\nRecent Abuse: " + str(email_info["Recent Abuse"]) + "\nSMTP Score: " + str(email_info["SMTP Score"]) + "\nSpam Trap Score: " + email_info["Spam Trap Score"] + "\nFraud Score: " + str(email_info["Fraud Score"]) + "\nOverall Score: " + str(email_info["Overall Score"])

#print(determine_malicious_phone_num(13013074602)) # put number here