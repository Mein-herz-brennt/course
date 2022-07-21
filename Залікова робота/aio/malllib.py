import email
import imaplib
import os


# from config import *


class Posht:
    def __init__(self, mail, password):
        self.m = mail
        self.p = password
        # print(1)

    def login_and_download(self):
        # print(2)
        # global filePath, fileName
        global filePath, fileName
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        # print(3)
        mail.login(self.m, self.p)  # https://www.google.com/settings/security/lesssecureapps
        # print('аутентифікацію пройдено успішно')
        mail.list()
        mail.select("inbox")
        # print('підключаємось до папки "вхідні"')

        # Пошук та повернення UID
        result, data = mail.uid('search', None, "ALL")
        inbox_item_list = data[0].split()
        count = len(inbox_item_list)
        # print(4)

        # Завантажуємо тіло електронної пошти
        most_recent = inbox_item_list[count - 1]
        result, email_data = mail.uid('fetch', most_recent, '(RFC822)')
        # print(5)

        # Перетворюмо байтовий літерал у рядок
        raw_email = email_data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email)
        # print(6)

        # записуємо дату останнього повідомлення
        # last_date = f"{email_message['Date']}\n"
        # print(last_date)

        # Наступний цикл for використовується для отримання вмісту електронного листа
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                save_string = str("" + "content" + ".eml")
                myfile = open(save_string, 'w')
                myfile.write(body.decode('utf-8'))
                myfile.close()
            else:
                continue

        # Наступний цикл for використовується для завантаження вкладень, якщо такі є
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            # print(f"Attachment: {fileName}")
            if bool(fileName):
                filePath = os.path.join('', fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                subject = email_message['Subject']
                print('Downloaded "{file}" from email titled "{subject}"'.format(file=fileName, subject=subject,))
        mail.logout()
        return fileName
