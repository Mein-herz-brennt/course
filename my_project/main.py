import sqlite3


# conn = sqlite3.connect("bot.db")
# cursor = conn.cursor()
#
# cursor.execute(f"""CREATE TABLE users_id (id int)""")
# cursor.execute(f"""CREATE TABLE channels (id int)""")
# cursor.execute(f"""CREATE TABLE admins (id int)""")
# cursor.execute(f"""CREATE TABLE user_info (id int, name text,
# lang text, move text, who_r_u text, type_of_help text, location text, loc_reg text, problem text, phone text)""")
# cursor.execute(f"""CREATE
# TABLE searcher (id int, page_num int, page text)""")
# cursor.execute(f"""CREATE TABLE
# search_factory (id int, search_type text, location text, loc_reg text)""")
# cursor.execute(f"""CREATE TABLE
# help_requests (id int, what text, who_r_u text, transport_type text, username text, name text, location text,
# location_reg text, ph_number text, telegram_id int, _help text, problem text, date text)""")
# cursor.execute(f"""CREATE TABLE provide_requests (id int, what text, who_r_u text, transport_type text, username text,
# name text, location text, location_reg text, ph_number text, telegram_id int, _help text, problem text, date text)""")
# cursor.execute(f"""CREATE TABLE car_need_requests (id int, what text, who_r_u text, transport_type text,
# username text, name text, location text, location_reg text, ph_number text, telegram_id int, _help text,
# problem text, date text)""")
# cursor.execute(f"""CREATE TABLE car_have_requests (id int, what text, who_r_u text,
# transport_type text, username text, name text, location text, location_reg text, ph_number text, telegram_id int,
# _help text, problem text, date text)""")


class BotDateBaseWork:
    def __init__(self):
        self.conn = sqlite3.connect("bot.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_users_id(self, user_id: int):
        self.cursor.execute(f"INSERT INTO users_id VALUES ('{user_id}')")
        self.conn.commit()

    def det_info_from_users_id(self):
        info = self.cursor.execute(f"""SELECT * FROM users_id""").fetchall()
        return info

    def delete_user_id(self, user_id: int):
        self.cursor.execute(f"""DELETE FROM users_id WHERE id = '{user_id}'""")
        self.conn.commit()

    def add_channel_id(self, channel_id: int):
        self.cursor.execute(f"INSERT INTO channels VALUES ('{channel_id}')")
        self.conn.commit()

    def get_info_from_channels(self):
        info = self.cursor.execute(f"""SELECT * FROM channels""").fetchall()
        return info

    def delete_channel_id(self, channel_id: int):
        self.cursor.execute(f"""DELETE FROM channels WHERE id = '{channel_id}'""")
        self.conn.commit()

    def add_admin_id(self, admin_id: int):
        self.cursor.execute(f"INSERT INTO admins VALUES ('{admin_id}')")
        self.conn.commit()

    def delete_admin_id(self, admin_id: int):
        self.cursor.execute(f"""DELETE FROM admins WHERE id = '{admin_id}'""")
        self.conn.commit()

    def get_info_from_admins(self):
        info = self.cursor.execute(f"""SELECT * FROM admins""").fetchall()
        return info

    def add_new_user_info_id(self, user_id: int):
        self.cursor.execute(f"""INSERT INTO user_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (user_id, "", "", "", "", "", "", "", "", ""))
        self.conn.commit()

    def add_info_into_search_factory_telegram_id(self, sr_id: int):
        self.cursor.execute(f"""INSERT INTO search_factory VALUES (?, ?, ?, ?)""",
                            (sr_id, "", "", ""))
        self.conn.commit()

    def add_info_into_searcher_telegram_id(self, id: int):
        self.cursor.execute(f"""INSERT INTO searcher VALUES (?, ?, ?)""",
                            (id, "", ""))
        self.conn.commit()

    def add_into_help_requests_telegram_id(self, id: int, what="", who_r_u="", transport_type="",
                                           username="",
                                           name="", location="", location_reg="", ph_number="",
                                           telegram_id="",
                                           _help="",
                                           problem="", date=""):
        self.cursor.execute(f"""INSERT INTO help_requests VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (id, what, who_r_u, transport_type, username, name, location, location_reg, ph_number,
                             telegram_id, _help, problem, date))
        self.conn.commit()

    def delete_help_requests(self, id: int):
        self.cursor.execute(f"""DELETE FROM help_requests WHERE id = ?""", (id,))
        self.conn.commit()

    def add_into_provide_requests_telegram_id(self, id: int, what="", who_r_u="", transport_type="",
                                              username="",
                                              name="", location="", location_reg="", ph_number="",
                                              telegram_id="",
                                              _help="",
                                              problem="", date=""):
        self.cursor.execute(f"""INSERT INTO provide_requests VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (id, what, who_r_u, transport_type, username, name, location, location_reg, ph_number,
                             telegram_id, _help, problem, date))
        self.conn.commit()

    def delete_provide_requests(self, id: int):
        self.cursor.execute(f"""DELETE FROM provide_requests WHERE id = ?""", (id,))
        self.conn.commit()

    def add_into_car_need_requests_telegram_id(self, id: int, what="", who_r_u="", transport_type="",
                                               username="",
                                               name="", location="", location_reg="", ph_number="",
                                               telegram_id="",
                                               _help="",
                                               problem="", date=""):
        self.cursor.execute(f"""INSERT INTO car_need_requests VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (id, what, who_r_u, transport_type, username, name, location, location_reg, ph_number,
                             telegram_id, _help, problem, date))
        self.conn.commit()

    def delete_car_need_requests(self, id: int):
        self.cursor.execute(f"""DELETE FROM car_need_requests WHERE id = ?""", (id,))
        self.conn.commit()

    def add_into_car_have_requests_telegram_id(self, id: int, what="", who_r_u="", transport_type="",
                                               username="",
                                               name="", location="", location_reg="", ph_number="",
                                               telegram_id="",
                                               _help="",
                                               problem="", date=""):
        self.cursor.execute(f"""INSERT INTO car_have_requests VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (id, what, who_r_u, transport_type, username, name, location, location_reg, ph_number,
                             telegram_id, _help, problem, date))
        self.conn.commit()

    def delete_car_have_requests(self, id: int):
        self.cursor.execute(f"""DELETE FROM car_have_requests WHERE id = ?""", (id,))
        self.conn.commit()

    def update_searcher_page_num(self, sr_id: int, page_num: int):
        self.cursor.execute(f"""UPDATE searcher SET page_num = ? WHERE id = ?""", (page_num, sr_id))
        self.conn.commit()

    def update_searcher_page(self, sr_id: int, page: str):
        self.cursor.execute(f"""UPDATE searcher SET page = ? WHERE id = ?""", (page, sr_id))
        self.conn.commit()

    def update_user_info_name(self, id: int, name: str):
        self.cursor.execute(f"""UPDATE user_info SET name = ? WHERE id = ?""", (name, id))
        self.conn.commit()

    def update_user_info_lang(self, id: int, lang: str):
        self.cursor.execute(f"""UPDATE user_info SET lang = ? WHERE id = ?""", (lang, id))
        self.conn.commit()

    def update_user_info_move(self, id: int, move: str):
        self.cursor.execute(f"""UPDATE user_info SET move = ? WHERE id = ?""", (move, id))
        self.conn.commit()

    def update_user_info_who_r_u(self, id: int, who_r_u: str):
        self.cursor.execute(f"""UPDATE user_info SET who_r_u = ? WHERE id = ?""", (who_r_u, id))
        self.conn.commit()

    def update_user_info_type_of_help(self, id: int, type_of_help: str):
        self.cursor.execute(f"""UPDATE user_info SET type_of_help = ? WHERE id = ?""", (type_of_help, id))
        self.conn.commit()

    def update_user_info_location(self, id: int, location: str):
        self.cursor.execute(f"""UPDATE user_info SET location = ? WHERE id = ?""", (location, id))
        self.conn.commit()

    def update_user_info_loc_reg(self, id: int, loc_reg: str):
        self.cursor.execute(f"""UPDATE user_info SET loc_reg = ? WHERE id = ?""", (loc_reg, id))
        self.conn.commit()

    def update_user_info_problem(self, id: int, problem: str):
        self.cursor.execute(f"""UPDATE user_info SET problem = ? WHERE id = ?""", (problem, id))
        self.conn.commit()

    def update_user_info_phone(self, id: int, phone: str):
        self.cursor.execute(f"""UPDATE user_info SET phone = ? WHERE id = ?""", (phone, id))
        self.conn.commit()

    def update_search_factory_sr_type(self, sr_id: int, search_type: str):
        self.cursor.execute(f"""UPDATE search_factory SET search_type = ? WHERE id = ?""", (search_type, sr_id))
        self.conn.commit()

    def update_search_factory_location(self, id: int, location: str):
        self.cursor.execute(f"""UPDATE search_factory SET location = ? WHERE id = ?""", (location, id))
        self.conn.commit()

    def update_search_factory_loc_reg(self, id: int, loc_reg: str):
        self.cursor.execute(f"""UPDATE search_factory SET loc_reg = ? WHERE id = ?""", (loc_reg, id))
        self.conn.commit()

    def get_info_from_searcher_by_id_and_page_num(self, id: int, page_num: int):
        searcher = self.cursor.execute(f"""SELECT * FROM searcher WHERE id = ? and page_num = ?""", (id,page_num)).fetchone()
        return searcher[2]

    def get_info_from_search_factory(self, id: int):
        info = self.cursor.execute(f"""SELECT * FROM search_factory WHERE id = ?""", (id,)).fetchone()
        return {"search-type": info[1], "location": info[2], "location_reg": info[3]}

    def get_info_about_user(self, id: int):
        info = self.cursor.execute(f"""SELECT * FROM user_info WHERE id = ?""", (id,)).fetchone()
        return {"language": info[2], "move": info[3], "who_r_u": info[4], "type-of-help": info[5], "location": info[6],
                "location-reg": info[7], "name": info[1], "phone": info[9], "problem": info[8]}

    def get_info_from_help_requests(self):
        req = self.cursor.execute(f"""SELECT * FROM help_requests""").fetchall()
        return [{"id": i[0], "what": i[1], "who_r_u": i[2], "transport_type": i[3], "username": i[4], "name": i[5],
                 "location": i[6], "location_reg": i[7], "ph_number": i[8], "telegram_id": i[9], "_help": i[10],
                 "problem": i[11], "date": i[12]} for i in req]

    def get_info_from_provide_requests(self):
        req = self.cursor.execute(f"""SELECT * FROM provide_requests""").fetchall()
        return [{"id": i[0], "what": i[1], "who_r_u": i[2], "transport_type": i[3], "username": i[4], "name": i[5],
                 "location": i[6], "location_reg": i[7], "ph_number": i[8], "telegram_id": i[9], "_help": i[10],
                 "problem": i[11], "date": i[12]} for i in req]

    def get_info_from_car_need_requests(self):
        req = self.cursor.execute(f"""SELECT * FROM car_need_requests""").fetchall()
        return [{"id": i[0], "what": i[1], "who_r_u": i[2], "transport_type": i[3], "username": i[4], "name": i[5],
                 "location": i[6], "location_reg": i[7], "ph_number": i[8], "telegram_id": i[9], "_help": i[10],
                 "problem": i[11], "date": i[12]} for i in req]

    def get_info_from_car_have_requests(self):
        req = self.cursor.execute(f"""SELECT * FROM car_have_requests""").fetchall()
        return [{"id": i[0], "what": i[1], "who_r_u": i[2], "transport_type": i[3], "username": i[4], "name": i[5],
                 "location": i[6], "location_reg": i[7], "ph_number": i[8], "telegram_id": i[9], "_help": i[10],
                 "problem": i[11], "date": i[12]} for i in req]