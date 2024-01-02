from colorama import Fore
from datetime import datetime
import requests, os, time, ctypes

asciiText = """
    █████   ███   █████          █████     █████                        █████     
    ░░███   ░███  ░░███          ░░███     ░░███                        ░░███      
    ░███   ░███   ░███   ██████  ░███████  ░███████    ██████   ██████  ░███ █████
    ░███   ░███   ░███  ███░░███ ░███░░███ ░███░░███  ███░░███ ███░░███ ░███░░███ 
    ░░███  █████  ███  ░███████  ░███ ░███ ░███ ░███ ░███ ░███░███ ░███ ░██████░  
    ░░░█████░█████░   ░███░░░   ░███ ░███ ░███ ░███ ░███ ░███░███ ░███ ░███░░███ 
        ░░███ ░░███     ░░██████  ████████  ████ █████░░██████ ░░██████  ████ █████
        ░░░   ░░░       ░░░░░░  ░░░░░░░░  ░░░░ ░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░ 
                                                                                
                                                                                
                                                                                
    █████████                                                                    
    ███░░░░░███                                                                   
    ░███    ░░░  ████████   ██████   █████████████   █████████████    ██████       
    ░░█████████ ░░███░░███ ░░░░░███ ░░███░░███░░███ ░░███░░███░░███  ░░░░░███      
    ░░░░░░░░███ ░███ ░███  ███████  ░███ ░███ ░███  ░███ ░███ ░███   ███████      
    ███    ░███ ░███ ░███ ███░░███  ░███ ░███ ░███  ░███ ░███ ░███  ███░░███      
    ░░█████████  ░███████ ░░████████ █████░███ █████ █████░███ █████░░████████     
    ░░░░░░░░░   ░███░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░      
                ░███                                                              
                █████                                                             
                ░░░░░                                                              
"""
divider = "===================================================================================="



class WebHook:
    def __init__(self, url: str):
        self.url = url

    def sendRequest(self, message: str):
        requests.post(self.url, json={'content': message})

    def deleteWebhook(self):
        requests.delete(self.url)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():

    now = datetime.now()
    current = now.strftime("%H:%M:%S")

    cls()
    ctypes.windll.kernel32.SetConsoleTitleW('Webhook Spammer')

    print(f"{Fore.CYAN}{asciiText}")
    print(f"{Fore.CYAN}{divider}{Fore.RESET}")
    print(f"\t\t\t\t   {Fore.CYAN}By: {Fore.RESET}L4J")
    print(f"{Fore.CYAN}{divider}{Fore.RESET}")
    url = input(f"{Fore.CYAN}Enter webhook url:{Fore.RESET} ")
    print(f"{Fore.CYAN}{divider}{Fore.RESET}")
    webhook = WebHook(url)

    while True:
        print(f"{Fore.CYAN}{divider}{Fore.RESET}")
        print(f"\n{Fore.CYAN}[{Fore.RESET}1{Fore.CYAN}] Spam Webhook")
        print(f"{Fore.CYAN}[{Fore.RESET}2{Fore.CYAN}] Delete Webhook")
        print(f"{Fore.CYAN}[{Fore.RESET}3{Fore.CYAN}] Exit")
        print(f"{Fore.CYAN}{divider}{Fore.RESET}")
        
        option = int(input(f"\n{Fore.CYAN}>>>{Fore.RESET} "))

        if option > 3:
            cls()
            print(f"[{Fore.RED}ERROR{Fore.RESET}] {Fore.CYAN}Pick A Number between {Fore.RESET}1 {Fore.CYAN}- {Fore.RESET}3\n")
            continue

        match option:
            case 1:
                cls()
                message = input(f"{Fore.CYAN}Enter a message for spamming:{Fore.RESET} ")
                amount = int(input(f"{Fore.CYAN}Enter amount of messages to send:{Fore.RESET} "))
                delay = int(input(f"{Fore.CYAN}Enter delay for message sending:{Fore.RESET} "))

                for i in range(amount + 1):
                    print(f"{Fore.CYAN}[{Fore.RESET}{current}{Fore.CYAN}] Message {Fore.CYAN}[{Fore.RESET}{i}{Fore.CYAN}] sent to Webhook")
                    webhook.sendRequest(message)
                time.sleep(delay)
                
                cls()
                print(f"{Fore.CYAN}Task Done {Fore.RESET}[{Fore.CYAN}{amount}{Fore.RESET}]{Fore.CYAN} messages have been sent to {Fore.RESET}[{Fore.CYAN}{url}{Fore.RESET}]{Fore.CYAN}\n")

            case 2:
                cls()
                print(f"{Fore.CYAN}Webhook {Fore.RESET}{url}{Fore.CYAN} has been deleted")
                webhook.deleteWebhook()

            case 3:
                cls()
                break

if __name__ == "__main__":
    main()
    