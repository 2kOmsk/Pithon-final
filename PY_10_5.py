import chardet
import subprocess 
webs = ['yandex.ru', 'youtube.com']

for site in webs:
    ping_process = subprocess.Popen(['ping', '-c', '4', site], stdout=subprocess.PIPE)
    ping_output, _ = ping_process.communicate()
    encoding = chardet.detect(ping_output)['encoding']
    ping_output = ping_output.decode(encoding)
    print(f"пинг для {site}:\n{ping_output}\n")
