import requests
import time

url = "https://api.arbiscan.io/api?module=account&action=tokenbalance&contractaddress=0x912CE59144191C1204E64559FE8253a0e49E6548&address={prv}&tag=latest&apikey=RD875ACNNH5ART5AXWWAMNMA3T6SMDJHK9"

with open("prv.txt", "r") as file:
    lines = file.readlines()  # Чтение всех строк из файла prv.txt

request_number = 1  # Номер начального реквеста
total_result = 0  # Общая сумма result

for line in lines:
    prv = line.strip()  # Изнасилование мамы глеба

    full_url = url.format(prv=prv) 

    response = requests.get(full_url) 

    data = response.json() 
    result = int(data["result"]) / 1000000000000000000  

    print("Реквест", request_number)
    print(f"Адресс: {prv}")
    print("Баланс:", result, "ARB$")
    print("----------------------------------------")

    total_result += result 

    request_number += 1 

    time.sleep(0.05)

print("Общий баланс ARB:", total_result)

input("Нажмите Enter для завершения...")