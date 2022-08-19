# import necessary modules
import requests

# Create class for ACI


class CiscoAPIC:
    # Assign attributes corresponding to APICs
    username = 'RG090077'
    password = 'Haphazard@1234'

    # Create a method for login to APIC using API
    def login(self, url):
        login_url = url+'api/aaaLogin.json'
        login_request_body = {
            "aaaUser": {
                "attributes": {
                    "name": self.username,
                    "pwd": self.password
                }
            }
        }
        # Create a POST request to push Login credentials to APIC, use verify=False if APIC does not use SSL
        resp = requests.post(url=login_url, json=login_request_body, verify=False)
        resp_output = resp.json()
        # print(resp_output)
        cookie = {'APIC-Cookie': resp_output['imdata'][0]['aaaLogin']['attributes']['token']}
        return cookie
