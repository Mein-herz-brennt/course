import requests
from bs4 import BeautifulSoup


class All_parser:
    def __init__(self):
        self.parsing = 0

    def second_site(self):
        req = requests.get("https://ua-energy.org/")
        soup = BeautifulSoup(req.text, "lxml")
        article = soup.find_all("div", class_="info")

        for i in article:
            src = "https://ua-energy.org" + i.find("a").get("href")
            nice = requests.get(src)
            soup2 = BeautifulSoup(nice.text, "lxml")
            nice_title = i.find("a").text  # .find("h1", class_="title-article")
            with open("out.txt", "a") as file:
                file.write(nice_title + " -- " + src + "\n", )
            print(nice_title)
            print("___________________________________________________________________")
            nice_p = soup2.find_all('p')

            for j in nice_p:
                nice_text = j.text
                print(nice_text)
            print("********************************************************************")

    # наступний сайт
    def third_site(self):
        o = 0
        req2 = requests.get("http://reform.energy/")
        soup3 = BeautifulSoup(req2.text, "lxml")
        # print(req2.text)
        linker = soup3.find("div", class_="col-lg-11 col-md-11 col-sm-9 col-xs-16 pull-left")
        links = linker.find_all("a")
        for linking in links:
            if o <= 3:
                title = linking.find("h3").text
                o += 1
            else:
                title = linking.find("h4").text
            link = linking.get('href')
            # with open("out.txt", "a") as file:
            #     file.write(title + " -- " + link + "\n", )
            key_pop = requests.get(link)
            soup4 = BeautifulSoup(key_pop.text, 'lxml')
            # print(key_pop.text)
            # print(title)
            # print(link)
            all_text = soup4.find("div", class_="article-description")
            print(title)
            print("__________________________________________________________________________________________________")
            print(all_text.text)
            print("**************************************************************************************************")

    # def fourth_site(self):
    #     headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #                "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
    #                "Alt-Used": "expro.com.ua", "Cache-Control": "max-age=0", "Connection": "keep-alive",
    #                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
    #     req3 = requests.get("https://expro.com.ua/novini", headers)
    #     soup5 = BeautifulSoup(req3.text, "lxml")
    #     nt = soup5.find("div", class_="row general")
    #     print(req3.text)
    def fifth_site(self):
        req3 = requests.get("http://www.nefterynok.info")
        soup5 = BeautifulSoup(req3.text, "lxml")
        tx = soup5.find_all("li", class_="normal")
        tk = soup5.find_all("li", class_="exlusive")
        for t in tx:
            title = t.find("a").text
            hr = "http://www.nefterynok.info" + t.find('a').get("href")
            # print(title + " - " + hr)
            q = requests.get(hr)
            soup6 = BeautifulSoup(q.text, "lxml")
            text_p_all = soup6.find_all("p")
            print(title + " - " + hr)
            print("_______________________________________________________________________________________________")
            for p in text_p_all:
                text_p = p.text
                print(text_p)
            print("*********************************************************************************************")

        for k in tk:
            title2 = k.find("a").text
            hrs = "http://www.nefterynok.info" + k.find("a").get("href")
            q2 = requests.get(hrs)
            soup7 = BeautifulSoup(q2.text, "lxml")
            text_p2_all = soup7.find_all("p")
            print(title2 + " - " + hrs)
            print("_______________________________________________________________________________________________")
            for p2 in text_p2_all:
                text_p2 = p2.text
                print(text_p2)
            print("*********************************************************************************************")

    def sixth_site(self):
        req4 = requests.get("http://reform.energy/vse-novosti-1")
        # print(req4.text)
        soup8 = BeautifulSoup(req4.text, "lxml")
        links_div = soup8.find("div", class_="col-md-11 col-sm-9").find_all("div", class_="row")
        for div in links_div:
            title = div.find("h3").text
            link = div.find("a").get("href")
            print(title)
            print("_____________________________________________________________________________________________")
            # print(link)
            q = requests.get(link)
            text = BeautifulSoup(q.text, "lxml").find("div", class_="article-description").text
            print(text)
            print("**********************************************************************************************")
            # for links in links_a:
            #     link = "https://enkorr.ua" + links.get("href")
            #     title = links.find("p", class_="last-news_item_text").text
            #     print(title)
            #     print(link)
            # all_li = soup8.find_all("li")
            # for li in all_li:
            #     link = li.find("a").get("href")
            #     print(link, len(all_li))

    def seventh_site(self):
        req = requests.get("https://oilpoint.com.ua")
        # with open("nice_parse.html", "w") as file:
        #     file.write(req.text)
        # src = open("nice_parse.html").read()
        soup = BeautifulSoup(req.text, "lxml")
        tags = soup.find("div", class_="wpb_column vc_column_container vc_col-sm-12 vc_hidden-lg vc_hidden-md") \
            .find("div", class_="vc_column-inner").find("div", class_="wpb_wrapper").find_all("div",
                                                                                              class_="mp-content")
        # print(len(tags))
        for tag in tags:
            title = tag.find("a").text
            link = tag.find("a").get("href")
            print(title + " -- " + link)
            print("___________________________________________________________________________________________________")
            q = requests.get(link)
            sp = BeautifulSoup(q.text, "lxml")
            text_tags = sp.find_all("p")
            for txt in text_tags:
                text = txt.text
                print(text)
            print("***************************************************************************************************")

    def ninth_site(self):
        req = requests.get("https://enerhodzherela.com.ua/novyny")
        # with open("nice_parse.html", "w") as file:
        #     file.write(req.text)
        soup = BeautifulSoup(req.text, "lxml")
        tags_news_div = soup.find_all("div", class_="item my-2")
        tag = soup.find_all("a")
        print(len(tag))

        # for t in tag:
        #     link = t.get("href")
        #     print(link)
        for tag in tags_news_div[0:22]:
            title = tag.find('h2').text
            link = tag.find("a").get("href")
            print(title + " -- " + link)
            print("____________________________________________________________________________________")
            q = requests.get(link)
            text_div = BeautifulSoup(q.text, "lxml").find_all("div", style="text-align: justify;")
            for txt in text_div:
                text = txt.text
                print(text)
            print("*************************************************************************************")

    def eleventh_site(self):
        req = requests.get("https://elektrovesti.net")
        soup = BeautifulSoup(req.text, "lxml")
        tag_div = soup.find_all("div", class_="articleBlock")
        count = 0
        for div in tag_div:
            title = div.find("a").text
            link = "https://elektrovesti.net" + div.find("a").get("href")
            count += 1
            print(title + " -- " + link)
            print("__________________________________________________________________________________________________")
            q = requests.get(link)
            sp = BeautifulSoup(q.text, "lxml")
            all_tags_p = sp.find_all("p")
            for tag in all_tags_p:
                text = tag.text
                print(text)
            print("**************************************************************************************************")


def twelfth_site():
    req = requests.get("https://www.unian.net/economics/energetics")
    soup = BeautifulSoup(req.text, "lxml")
    links = soup.find("div", class_="list-thumbs").find_all("a", class_="list-thumbs__title")
    for l in links:
        title = l.text
        link = l.get("href")
        print(title + " -- " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        all_li = sp.find("div", class_="article-text").find_all("li")
        for p in all_p:
            text = p.text
            print(text)
        for li in all_li:
            txt = li.text
            print(txt)


def thirteenth_site():
    req = requests.get("https://biz.liga.net/tek")
    soup = BeautifulSoup(req.text, "lxml")
    all_div = soup.find_all("div", class_="clearfix")
    for div in all_div[0:19]:
        link = div.find("a").get("href")
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        title = sp.find("h1").text
        print(title)
        print(link)
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def fourteenth_site():
    req = requests.get("https://www.pravda.com.ua/rus/tags/5490438fa2cef")
    soup = BeautifulSoup(req.text, "lxml")
    all_h3 = soup.find_all("h3")
    for h3 in all_h3:
        title = h3.find("a").text
        link = h3.find("a").get("href")
        # print(title + " - " + link)
        if link.startswith("https:") == 0:
            link = "https://www.pravda.com.ua/rus/tags/5490438fa2cef" + link
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def fifteenth_site():
    req = requests.get("https://www.rbc.ua/ukr/energetics")
    soup = BeautifulSoup(req.text, "lxml")
    all_a = soup.find("div", class_="newsline").find_all("a")
    for a in all_a:
        title = a.text
        link = a.get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def seventeenth_site():
    req = requests.get("http://oilreview.kiev.ua")
    soup = BeautifulSoup(req.text, "lxml")
    all_h2 = soup.find_all("h2")
    for h2 in all_h2:
        title = h2.find("a").text
        link = h2.find("a").get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find("div", class_="entry").find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def eighteenth_site():
    req = requests.get("https://glavcom.ua")
    soup = BeautifulSoup(req.text, "lxml")
    all_li = soup.find_all("li", class_="h1000")
    for li in all_li:
        title = li.find("a").text
        link = "https://glavcom.ua" + li.find("a").get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def nineteenth_site():
    req = requests.get("https://www.epravda.com.ua")
    soup = BeautifulSoup(req.text, "lxml")
    all_div = soup.find_all("div", class_="article__title")
    for div in all_div[0:33]:
        title = div.find("span").text
        link = "https://www.epravda.com.ua" + div.find("a").get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_span = sp.find("div", class_="post__text").find_all('span')
        for span in all_span:
            text = span.text
            print(text)


def twentyth_site():
    req = requests.get("https://neftegaz.ru/news/")
    soup = BeautifulSoup(req.text, "lxml")
    all_div = soup.find_all("div", class_="title")
    for div in all_div[0:30]:
        title = div.find("a").text
        link = div.find("a").get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def twenty_first_site():
    req = requests.get("https://mind.ua")
    soup = BeautifulSoup(req.text, "lxml")
    all_a = soup.find("div", class_="b-info-list").find_all("a", class_="b-info-list__link js-info-list__link")
    for a in all_a:
        title = a.text
        link = a.get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find("div", class_="post__text").find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def twenty_second_site():
    req = requests.get("http://mpe.kmu.gov.ua")
    soup = BeautifulSoup(req.text, "lxml")
    all_div = soup.find_all("div", class_="title")
    for div in all_div:
        title = div.find("a").text
        link = "http://mpe.kmu.gov.ua/" + div.find("a").get('href')
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find("div", class_="WordSection1").find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def twenty_third_site():
    req = requests.get("https://www.kmu.gov.ua/")
    soup = BeautifulSoup(req.text, "lxml")
    all_div = soup.find("ul", class_="main-page-news-list").find_all("div", class_="main-item")
    all_div2 = soup.find("ul", class_="main-page-news-list").find_all("div", class_="news-item")
    for div in all_div:
        title = div.find("a").text
        link = "https://www.kmu.gov.ua" + div.find("a").get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)
    for div2 in all_div2:
        title = div2.find("a").text
        link = "https://www.kmu.gov.ua" + div2.find("a").get("href")
        print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        all_p = sp.find_all("p")
        for p in all_p:
            text = p.text
            print(text)


def twenty_fourth_site():
    req = requests.get("https://uhe.gov.ua/media_tsentr/novyny")
    soup = BeautifulSoup(req.text, "lxml")
    all_div = soup.find_all("div", class_="views-row")
    for div in all_div[0:4]:
        link = "https://uhe.gov.ua" + div.find("a").get('href')
        # print(title + " - " + link)
        q = requests.get(link)
        sp = BeautifulSoup(q.text, "lxml")
        # print(link)
        title = sp.find("h1", class_="head_title").text
        print(title + " - " + link)
        txt = sp.find("div", class_="novini__short-text").text
        print(txt)
        all_p = sp.find("div", class_="content").find("div", class_="novini__body").find_all("p")
        for p in all_p:
            text = p.text
            print(text)
        # for p in all_p:
        #     text = p.text
        #     print(text)


if __name__ == '__main__':
    All_parser().ninth_site()
    # print(1)
