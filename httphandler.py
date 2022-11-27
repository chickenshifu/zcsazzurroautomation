import requests
import time
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from config import totalBatteryCapacity, minimumDischargeLevel, priceOfElectricity, denomination, language

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class HttpHandler():
    
    def __init__(self):
        
        self.base_url = 'https://www.zcsazzurroportal.com'

        self.username = os.getenv('ZCSAZZURRO_USR')
        self.password = os.getenv('ZCSAZZURRO_PWD')
        
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")
    
        self.http_session = requests.Session()
        
        print(f"Initialized HttpHandler for Username {bcolors.BOLD}{self.username}{bcolors.ENDC} at {self.current_time}")
        
        
    def init_session(self):
        
        headers = {
            "Host": "www.zcsazzurroportal.com",
            "Sec-Ch-Ua": "Chromium"";""v=""107""," "Not=A?Brand"";""v=""24",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "close",
        }
        
        
        print(f"Trying to initialize session. Calling {self.base_url}...")

        response = self.http_session.get(self.base_url, headers=headers)

        if response.status_code != 200:
            print(f"{bcolors.FAIL}Failed to initialize session.\nPlease ensure provided credentials are correct, manually check {self.base_url} or report issue on www.github.com/chickenshifu.")
        
        else:
            self.cookie = response.cookies.get_dict()['JSESSIONID']
            print(f"{bcolors.OKGREEN}Successfully Initialized HTTP session for Username {bcolors.BOLD}{self.username} (Cookie: {self.cookie}){bcolors.ENDC}")
                    
        time.sleep(3)
        
        
    def login(self):
                
        suffix = '/login'
        
        cookies = {
            'JSESSIONID': self.cookie,
        }
                        
        headers = {
            'Host': 'www.zcsazzurroportal.com',
            # 'Content-Length': '124',
            'Cache-Control': 'max-age=0',
            'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://www.zcsazzurroportal.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.zcsazzurroportal.com/',
            'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close',
        }
        
        data = {
            'parent': '',
            'parent2': '',
            'parent3': '',
            'parent4': '0',
            'parent5': 'EN',
            'parent6': '',
            'parent7': 'base',
            'parent8': '',
            'username': str(self.username),
            'psswd': str(self.password),
        }
        

        response = self.http_session.post(self.base_url+suffix, cookies=cookies, headers=headers, data=data, verify=True)

        if response.status_code != 200:
            print(f"{bcolors.FAIL}Failed to login.\nPlease ensure provided credentials are correct, manually check {self.base_url} or report issue on www.github.com/chickenshifu.")
        
        else:
            print(f"{bcolors.OKGREEN}Successfully logged into user area of zcsazzurroportal for Username {bcolors.BOLD}{self.username}{bcolors.ENDC}")
            
        time.sleep(3)
          
          
    def get_user_id(self):
        
        suffix = '/index.jsp'

        cookies = {
            'JSESSIONID': self.cookie,
        }

        headers = {
            'Host': 'www.zcsazzurroportal.com',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Referer': 'https://www.zcsazzurroportal.com/',
            'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close',
        }

        response = self.http_session.get(self.base_url+suffix, cookies=cookies, headers=headers, verify=True)
        soup = BeautifulSoup(response.text, 'lxml')
        
        try:
            self.user_id = soup.find('input', {'name': 'parent'}).get('value')
            self.user_id = self.user_id.rstrip()
            
            print(f"{bcolors.OKGREEN}Successfully found User ID {bcolors.BOLD}{self.user_id}{bcolors.ENDC}{bcolors.OKGREEN} for Username {bcolors.BOLD}{self.username} (Cookie: {self.cookie}){bcolors.ENDC}")

        except Exception as e:
            print(f"{bcolors.FAIL}Failed to find User ID.\nPlease manually check {self.base_url+suffix} or report issue on www.github.com/chickenshifu.\nException: {str(e)}")

        time.sleep(3)
     
     
    def get_plant_list(self):
        
        suffix = '/getPlantList'
        
        cookies = {
            'JSESSIONID': self.cookie,
        }

        headers = {
            'Host': 'www.zcsazzurroportal.com',
            'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Origin': 'https://www.zcsazzurroportal.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.zcsazzurroportal.com/index.jsp',
            'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close',
        }

        data = {
            'usertype': 'USER',
            'userid': self.user_id,
        }
        
        response = self.http_session.post(self.base_url+suffix, cookies=cookies, headers=headers, data=data, verify=True)
        
        root = ET.fromstring(response.content)
       
        try:
            self.plant_id = root.find('.//plant').attrib['id']
            
            print(f"{bcolors.OKGREEN}Successfully found Plant ID {bcolors.BOLD}{self.plant_id}{bcolors.ENDC}{bcolors.OKGREEN} for User ID {bcolors.BOLD}{self.user_id} (Cookie: {self.cookie}){bcolors.ENDC}")

        except Exception as e:
            print(f"{bcolors.FAIL}Failed to find Plant ID.\nPlease manually check {self.base_url+suffix} or report issue on www.github.com/chickenshifu.\nException: {str(e)}")

        time.sleep(3)


    def get_plant_info(self) -> dict:
        
        suffix = '/getPlantInfoWS'

        headers = {
            'Host': 'www.zcsazzurroportal.com',
            'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Origin': 'https://www.zcsazzurroportal.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.zcsazzurroportal.com/index.jsp',
            'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close',
        }

        data = {
            'plantid': self.plant_id,
            'userid': self.user_id,
            'usertype': 'USER',
            'servizioimpianto': 'base',
        }

        response = self.http_session.post(self.base_url+suffix, headers=headers, data=data, verify=True)

        root = ET.fromstring(response.content)

        soc = root[84].text
        soc = soc.split(":")[1].split(" ")[1]
        soc_float = float(soc)

        dischargePotential = round((totalBatteryCapacity * soc_float/100) - (totalBatteryCapacity * minimumDischargeLevel), 2)
        
        directConsumption = root[63].text 
        totalProduced = root[54].text
        totalConsumption = root[65].text 
        chargedIntoBattery = root[64].text 
        dischargedFromBattery = root[67].text 
        feedIntoGrid = root[62].text
        drawnFromGrid = root[66].text


        if language == 'GER':
            print("\n")
            print(f'{bcolors.UNDERLINE}Aktuelle Daten der Photovoltaikanlage ({bcolors.BOLD}{current_time}):{bcolors.ENDC}')
            print(f'{bcolors.OKGREEN}Produziert: {bcolors.BOLD}{totalProduced} kWh ({round(float(totalProduced) * priceOfElectricity,2)} EUR){bcolors.ENDC}')
            print(f'--- davon Geladen (in die Batterie): {bcolors.BOLD}{chargedIntoBattery} kWh ({round(float(chargedIntoBattery) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- davon Eingespeist (in das Netz): {bcolors.BOLD}{feedIntoGrid} kWh ({round(float(feedIntoGrid) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print("\n")
            print(f'Aktueller SOC: {bcolors.BOLD}{soc} %{bcolors.ENDC} (Minimum liegt bei 20.0 %)')
            print(f'--- Entladepotential bis Minimum: {bcolors.BOLD}{dischargePotential} kWh {bcolors.ENDC}')
            print("\n")
            print(f'{bcolors.WARNING}Gesamtverbrauch: {bcolors.BOLD}{totalConsumption} kWh ({round(float(totalConsumption) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- davon Direktverbrauch (vom Dach): {bcolors.BOLD}{directConsumption} kWh ({round(float(directConsumption) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- davon Entladen (aus der Batterie): {bcolors.BOLD}{dischargedFromBattery} kWh ({round(float(dischargedFromBattery) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- davon Bezogen (aus dem Netz): {bcolors.BOLD}{drawnFromGrid} kWh ({round(float(drawnFromGrid) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')

            print("\n")
            
        else:
            print("\n")
            print(f'{bcolors.UNDERLINE}Current Data of the Photovoltaic plant ({bcolors.BOLD}{current_time}):{bcolors.ENDC}')
            print(f'{bcolors.OKGREEN}Total Produced: {bcolors.BOLD}{totalProduced} kWh ({round(float(totalProduced) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- thereof charged into Battery: {bcolors.BOLD}{chargedIntoBattery} kWh ({round(float(chargedIntoBattery) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- thereof fed into grid: {bcolors.BOLD}{feedIntoGrid} kWh ({round(float(feedIntoGrid) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print("\n")
            print(f'Current SoC: {bcolors.BOLD}{soc} %{bcolors.ENDC} (minimum discharge level: {round(minimumDischargeLevel*100,2)}%)')
            print(f'--- potential until minimum discharge level: {bcolors.BOLD}{dischargePotential} kWh {bcolors.ENDC}')
            print("\n")
            print(f'{bcolors.WARNING}Total Consumption: {bcolors.BOLD}{totalConsumption} kWh ({round(float(totalConsumption) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- thereof direct consumption from your PV plant: {bcolors.BOLD}{directConsumption} kWh ({round(float(directConsumption) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- thereof discharged from battery: {bcolors.BOLD}{dischargedFromBattery} kWh ({round(float(dischargedFromBattery) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print(f'--- thereof drawn from grid: {bcolors.BOLD}{drawnFromGrid} kWh ({round(float(drawnFromGrid) * priceOfElectricity,2)} {denomination}){bcolors.ENDC}')
            print("\n")
        
        results = {
            "totalProduced": totalProduced,
            "chargedIntoBattery": chargedIntoBattery,
            "feedIntoGrid" : feedIntoGrid,
            "totalConsumption": totalConsumption,
            "directConsumption": directConsumption,
            "dischargedFromBattery": dischargedFromBattery,
            "drawnFromGrid": drawnFromGrid
        }
        
        print(results)
        return(results)
    
        
