# Create the initial FQDN: IP dict in step 1
mydict = {
    "server1.testlab.com": "192.168.1.10",
    "server2.testlab.com": "192.168.1.11",
    "server3.testlab.com": "192.168.1.12",
    "server4.testlab.com": "192.168.1.13",
    "server5.testlab.com": "192.168.1.14",
    "server6.testlab.com": "192.168.1.15",
}

# List all FQNs in dict per step 2 
for fqdn in mydict.keys():
    print(fqdn)

#List all IPs in dict per step 3
for ip in mydict.values():
    print(ip)

# List all key/values in dict per step 4
for fqdn, ip in mydict.items():
    print(f"{fqdn}: {ip}")

# Add new values to dict per step 5 
mydict["server7.testlab.com"] = "192.168.1.16"
mydict["server8.testlab.com"] = "192.168.1.17"

#Determine if specific keys are in dict per steps 6 and 7
print("server2.testlab.com in dict") if "server2.testlab.com" in mydict.keys() else print("server2.testlav.com not in dict")
print("server10.testlab.com in dict") if "server10.testlab.com" in mydict.keys() else print("server10.testlab.com not in dict")