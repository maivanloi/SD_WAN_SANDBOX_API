import requests
import json
import sdwan_infor
requests.packages.urllib3.disable_warnings()

j_username = sdwan_infor.j_username
j_password = sdwan_infor.j_password
baseUrl = sdwan_infor.url

def get_cookie():
    url = f"{baseUrl}/j_security_check"
    header = {
        "Content-Type":"application/x-www-form-urlencoded"
    }
    payload = {
        "j_username": j_username,
        "j_password": j_password
    }
    response = requests.request("POST", url, headers=header, data=payload, verify=False)
    cookie = response.headers['Set-Cookie']
    jssID = cookie.split(';')
    return jssID[0]
def get_all_device():
    url = f"{baseUrl}/dataservice/device"
    header = {
        "Cookie": get_cookie()
    }
    response = requests.request("GET", url, headers=header, verify=False)
    all_device = response.json()
    return all_device
def get_list_infor():
    global Device_IP, Hostname, DeviceType, UUID, Status, Version
    Device_IP = []
    Hostname = []
    DeviceType = []
    UUID = []
    Status = []
    Version = []
    response = get_all_device()
    for device in response['data']:
        Device_IP.append(device['deviceId'])
        Hostname.append(device['host-name'])
        DeviceType.append(device['device-type'])
        UUID.append(device['uuid'])
        Status.append(device['status'])
        Version.append(device['version'])

#####################TABLE###################

from rich.console import Console
from rich.table import Table
def building_table():
    get_list_infor()
    console = Console()
    headears = ["DeviceIP", "Hostname", "DeviceType", "UUID", "Status", "Version"]
    table = Table(show_header=True, header_style="Bold", title="SDWAN-API-SANDBOX")
    for header in headears:
        table.add_column(header, justify="center")
    response = get_all_device()
    for i in range(len(response['data'])):
        table.add_row(Device_IP[i], Hostname[i], DeviceType[i], UUID[i], Status[i], Version[i])

    console.print(table)

building_table()



