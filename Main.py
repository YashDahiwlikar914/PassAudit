import math
import requests
import hashlib

def checkBreach(password):
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest.upper()
    prefix, suffix = hash[:5], hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        
    


def policyAnalysis():
    global entropy
    l = int(input("Enter minimum length : "))
    upperCase = str(input("Includes uppercase (Y/N) : ")).lower()
    lowerCase = str(input("Includes lowercase (Y/N) : ")).lower()
    specialChars = str(input("Includes special characters (Y/N) : ")).lower()
    numbers = str(input("Includes numbers (Y/N) : ")).lower()
    expiry = int(input("Password expiry duration (In months) : "))
    checkBreaches = str(input("Are passwords checked against breaches? (Y/N) : ")).lower()
    mfaStatus = str(input("Is MFA Mandatory? (Y/N) : ")).lower()

    n = 0

    if upperCase == "y":
        n += 26
    if lowerCase == "y":
        n += 26
    if specialChars == "y":
        n += 33
    if numbers == "y":
        n += 10

    entropy += l * math.log2(n)

    print("\n<----- Policy Analysis ----->\n")
    score = 0
    if l < 8:
        score += 2
        print("❌ Length criteria too weak!")
    elif 8 <= l < 12:
        score += 3
        print("❗❗❗ Length criteria is fine but still weak!")
    elif 16 > l >= 12:
        score += 5
        print("✅ Length criteria is very strong!")
    else:
        score += 5
        print("✅ Length criteria is at max level! (Could affect user experience)")

    if entropy < 25:
        print("❌ Entropy is very weak!")
    elif 25 <= entropy < 50:
        print("❗❗❗ Entropy is fine but still weak!")
    elif 50 <= entropy < 75:
        score += 1
        print("✅ Entropy is very strong!")
    else:
        score += 1
        print("✅ Entropy is at max level!")

    if upperCase != "y" or lowerCase != "y" or specialChars != "y" or numbers != "y":
        print("❗❗❗ Complete character pool is not being utilized!")
    else:
        score += 2
        print("✅ Complete character pool is being utilized")

    if expiry <= 12:
        print("❗❗❗ Expiry is very frequent!")
    else:
        print("✅ Expiry is within NIST guidelines!")

    if mfaStatus == "y":
        score += 1
        print("✅ MFA is mandatory")
    else:
        print("❗❗❗ MFA is not mandatory!")

    if checkBreaches == "y":
        score += 1
        print("✅ Passwords are being checked aganist breaches")
    else:
        print("❗❗❗ Passwords are not being checked aganist breaches")

    print("\nOverall Policy Score: " + str(score))

    print("\n<----- NIST Recommendations ----->\n")

    print("Password Length be minimum 8 and 15+ recommended\n"
          "Should allow all alphanumeric characters and special characters\n"
          "Check passwords aganist data breaches\n"
          "Allow(or keep mandatory) MFA and use passkeys\n"
          "Avoid security questions\n"
          "Avoid dictionary words and repetition of characters\n")

def passwordRating():
    global entropy
    password = str(input("Enter the password : "))
    l = len(password)

    n = 0
    if any(c.isupper() for c in password): n += 26
    if any(c.islower() for c in password): n += 26
    if any(c.isdigit() for c in password): n += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for c in password): n += 32

    score = 0

    if l < 8:
        pass
    elif 8 <= l < 12:
        score += 3
    elif 16 > l >= 12:
        score += 5
    else:
        score += 5

    if n <= 26:
        pass
    elif 26 < n <= 52:
        score += 1
    elif 52 < n <= 62:
        score += 2
    elif n > 62:
        score += 3

    breachCount = checkBreach(password)

    if breachCount > 0:
        score -= 3
    else:
        score += 2
    
    
    
    
    

print("\n<----- PassAudit Tool ----->\n")

print("Choose task to do -\n"
      "Type 0 to do Policy Analysis\n"
      "Type 1 to do Password Rating\n"
      "Type 2 to do Password Rating(Bulk)\n"
      "Type 3 to do Password Entropy Calculation")
choice = str(input("-> "))

entropy = 0

if choice == '0':
    policyAnalysis()
elif choice == '1':
    passwordRating()
elif choice == '2':
    print("Feature Coming Soon!")
elif choice == '3':
    print("Feature Coming Soon!")
else:
    print("You weren't suppose to do that!")



