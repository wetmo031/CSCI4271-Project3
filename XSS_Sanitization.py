import urllib.parse
import re

# this function can be used to determine if user url's are malicous
# how the dev wants to implement this py script is their choice
# the function will mitigate xss attacks through url injection
def contains_javascript_payload(url: str) -> bool:
    # decode url
    decoded_url = urllib.parse.unquote(url)

    # check patterns
    patterns = [
        r"<script.*?>",       # script tag
        r"javascript:",       # js protocol
        r"on\w+\s*=",         # js events
        r"eval\s*\(",         # eval call
        r"alert\s*\(",        # alert call
    ]

    # search patterns
    for pattern in patterns:
        if re.search(pattern, decoded_url, re.IGNORECASE):
            return True

    return False
