##Python’s re module provides support for working with regular expressions, 
# allowing you to search, match, and manipulate strings efficiently. 

import re

cardNumber = input("Number: ").strip()

##{13} and {14} below means other than the number before, the numbers of rest digits
def get_card_type(cardNumber):
    ##
    amex_pattern = r"^3[47]\d{13}$"
    mastercard_pattern = r"^5[1-5]\d{14}$"
    visa_pattern = r"^4\d{12}(\d{3})?$"
    
    if re.match(amex_pattern, cardNumber):
        print("AMEX")
    elif re.match(mastercard_pattern, cardNumber):
        print("MASTERCARD")
    elif re.match(visa_pattern, cardNumber):
        print("VISA")
    else:
        print("INVALID")

get_card_type(cardNumber)