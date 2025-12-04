class ClientOrder:
    def __init__(self, name, device_type, browser, sex, age, bill, region):
        self.__name = name
        self.__device_type = device_type
        self.__browser = browser
        self.__sex = sex == "male"
        self.__age = int(age)
        self.__bill = int(bill)
        self.__region = region

    def __str_age(self):
        last_digit = self.__age % 10
        if last_digit > 4 or last_digit == 0 or (10 < self.__age < 15):
            return f"{self.__age} лет"
        if last_digit > 1:
            return f"{self.__age} года"
        return f"{self.__age} год"

    def __str_browser_type(self):
        mobile_device_types = ["mobile", "tablet"]
        str_browser_type = "браузера"
        if self.__device_type in mobile_device_types:
            str_browser_type = "мобильного " + str_browser_type

        return str_browser_type

    def __str__(self):
        return (f"Пользователь {self.__name} "
                f"{"мужского" if self.__sex else "женского"} пола, "
                f"{self.__str_age()} "
                f"{"совершил" if self.__sex else "совершила"} "
                f"покупку на {self.__bill} у.е. "
                f"с {self.__str_browser_type()} "
                f"{self.__browser}. "
                f"Регион, из которого совершалась покупка: {self.__region}.")


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