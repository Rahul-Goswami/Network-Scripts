# import necessary modules
import requests

# Create class for ACI


class CiscoAPIC:
    # Assign attributes corresponding to APICs
    url = 'https://sandboxapicdc.cisco.com/'
    username = 'admin'
    password = '!v3G@!4@Y'

    # Create a method for login to APIC using API
    def login(self):
        login_url = self.url+'api/aaaLogin.json'
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

    # Create a method to obtain list of tenants using API
    def tenantlist(self, cookie):
        api_url = self.url + 'api/node/class/fvTenant.json'
        # Create the request with the cookie as stored from login method
        resp = requests.get(url=api_url, cookies=cookie, verify=False)
        resp_output = resp.json()
        # Create loop to display only the tenant names
        incrementer = 0
        listoftenants = list()
        for iterator in resp_output['imdata']:
            listoftenants.append(resp_output['imdata'][incrementer]['fvTenant']['attributes']['name'])
            # print(resp_output['imdata'][incrementer]['fvTenant']['attributes']['name'])
            incrementer += 1
        print(listoftenants, len(listoftenants))

    # Create a method to obtain the list of interfaces and their admin and operational status of a node
    def intefaceliststatus(self, cookie):
        print("Enter the node number for which you require interface status: ")
        node = input()
        api_url = self.url + 'api/node/class/topology/pod-1/node-' + node + '/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf&rsp-subtree-include=required'
        resp = requests.get(url=api_url, cookies=cookie, verify=False)
        resp_output = resp.json()
        # Create a loop to print the interface name, admin status and operational status
        incrementer = 0
        interfaces = list()
        print("Interface name -> Admin State -> Operational State")
        for iterator in resp_output['imdata']:
            details = list()
            details.append(resp_output['imdata'][incrementer]['l1PhysIf']['attributes']['id'])
            details.append(resp_output['imdata'][incrementer]['l1PhysIf']['attributes']['adminSt'])
            details.append(resp_output['imdata'][incrementer]['l1PhysIf']['children'][0]['ethpmPhysIf']['attributes']['operSt'])
            interfaces.append(details)
            incrementer += 1
        for inc in interfaces:
            print(inc)
            print('\n')
        print(len(interfaces))

# Instantiate a CiscoAPIC object and check for Login response
apic = CiscoAPIC()
# Call login method from CiscoAPIC class to perform login
resp_cookie = apic.login()
# Call tenantList method from CiscoAPIC class to obtain list of tenants
apic.tenantlist(resp_cookie)
# Call interfaceliststatus method from CiscoAPIC class to obtain interface list and status
apic.intefaceliststatus(resp_cookie)
