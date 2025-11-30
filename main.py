class ClientOrder:
    def __init__(self, name, device_type, browser, sex, age, bill, region):
        self.name = name
        self.device_type = device_type
        self.browser = browser
        self.sex = sex == "male"
        self.age = int(age)
        self.bill = int(bill)
        self.region = region

    def _str_age(self):
        last_digit = self.age % 10
        if last_digit > 4 or last_digit == 0 or (10 < self.age < 15):
            return f"{self.age} лет"
        if last_digit > 1:
            return f"{self.age} года"
        return f"{self.age} год"

    def _str_browser_type(self):
        mobile_device_types = ["mobile", "tablet"]
        str_browser_type = "браузера"
        if self.device_type in mobile_device_types:
            str_browser_type = "мобильного " + str_browser_type

        return str_browser_type

    def __str__(self):
        return (f"Пользователь {self.name} "
                f"{"мужского" if self.sex else "женского"} пола, "
                f"{self._str_age()} "
                f"{"совершил" if self.sex else "совершила"} "
                f"покупку на {self.bill} у.е. "
                f"с {self._str_browser_type()} "
                f"{self.browser}. "
                f"Регион, из которого совершалась покупка: {self.region}.")


with open("result.txt","w",encoding="utf-8") as f_write:
    with open("web_clients_correct.csv", "r", encoding="utf-8") as f_read:
        f_read.readline() #Пропуск первой строки

        for line in f_read:
            #Удаление двойных пробелов
            line = line.replace("  "," ")
            #Починка строки если кавычки
            if line[0] == '"':
                line = line[1:-2].replace('""', '"')  #Замена двойных кавычек на одинарные
            try:
                name, device_type, browser, sex, age, bill, region = line.strip().split(",")
            except Exception as e:
                print("Parse error:", line, e)
            client_order = ClientOrder(name, device_type, browser, sex, age, bill, region)
            res_line = str(client_order)
            f_write.write(res_line + "\n")
            
print("Parsing completed.")