import requests
from bs4 import BeautifulSoup


# Количество запросов не ограничено
class Behance_parser:
    def __init__(self, url: str):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, "lxml")
        self.appreciation_url = url + "/appreciated"
        self.appreciation_resp = requests.get(self.appreciation_url)
        self.appreciation_soup = BeautifulSoup(self.appreciation_resp.text, "lxml")

    # Получаем имя пользователя
    def get_username(self):
        username = self.soup.find("h1", class_="ProfileCard-userFullName-3jr").text
        return username

    # проверяем есть ли аватар
    def get_user_image_exist(self):
        image = self.soup.find("img", class_="AvatarImage-avatarImage-3uu Avatar-root--Wh")
        if image is None:
            image_exist = False
        else:
            image_exist = True
        return image_exist

    # Получаем дату реестрации акаунта
    def get_user_membership(self):
        membership = self.soup.find("p", class_="UserInfo-memberSince-3K8").text
        return membership.replace('Member Since: ', '')

    # Получаем количество постов пользователя
    def get_project_number(self):
        projects = self.soup.find_all(class_="ProjectCoverNeue-root-166 ContentGrid-gridItem-WHz")
        if projects is None:
            project_count = None
        else:
            project_count = len(projects)
        return project_count

    # проверка поставил ли он лайк посту
    def get_user_applications(self, appreciation_url_apprec: str):
        appreciations = self.appreciation_soup.find_all(class_="Cover-cover-2mr AppreciationCover-cover-11u "
                                                               "ContentGrid-gridItem-WHz")

        if appreciations is None:
            appreciation_list = None
        else:
            appreciation_list = []
            for appreciation in appreciations:
                appreciation_list.append(appreciation.find("a")["href"])
        if appreciation_url_apprec in appreciation_list:
            appreciation = True
        else:
            appreciation = False
        return appreciation


# проверка работоспособности
if __name__ == '__main__':
    behance_name = Behance_parser('https://www.behance.net/vladabramcbefb').get_username()
    print(f"Имя пользователя: {behance_name}")
    behance_apprec = Behance_parser('https://www.behance.net/vladabramcbefb').get_user_applications(
        'https://www.behance.net/gallery/119439049/AESPA-NEXT-LEVEL')
    print(f"Проверка поставил ли он лайк посту: {behance_apprec}")
    behance_ex = Behance_parser('https://www.behance.net/vladabramcbefb').get_user_image_exist()
    print(f"Проверка наличия аватара: {behance_ex}")
    behance_member = Behance_parser('https://www.behance.net/vladabramcbefb').get_user_membership()
    print(f"Дата реєстрації акаунту: {behance_member}")
    behance_number = Behance_parser('https://www.behance.net/vladabramcbefb').get_project_number()
    print(f"Количество постов: {behance_number}")
