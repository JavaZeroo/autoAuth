import requests
from pathlib import Path
import yaml

class Loginer:
    def __init__(self, config, cache=True, debug=False):
        self.config = config
        self.cache = cache
        self.debug = debug
        if cache:
            self.cache_path = Path(__file__).parent / '.cache'
            self.cache_path.mkdir(exist_ok=True)
            with open(self.cache_path / 'cache_config.yaml', 'w') as f:
                yaml.dump({
                    'username': self.config.username,
                    'password': self.config.password,
                    'domain': self.config.domain,
                }, f)
        else:
            self.cache_path = None

    def login(self,):
        username = self.config.username
        password = self.config.password
        domain = self.config.domain

        payload = {
            'action': 'login',
            'ac_id': '1',
            'user_ip': '',
            'nas_ip': '',
            'user_mac': '',
            'url': '',
            'drop': '0',
            'domain': domain,
            'username': username,
            'password': password,
            'save_me': '1'
        }
        if self.debug:
            print(payload)
        headers = {
            'Host': '172.17.3.10',
            'Connection': 'keep-alive',
            'Content-Length': '129',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://172.17.3.10',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Referer': 'http://172.17.3.10/srun_portal_pc.php?ac_id=1&',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9'
        }

        try:
            s = requests.Session()
            s.get("http://www.baidu.com")
            s.get("http://172.17.3.10/srun_portal_pc.php")

            response = s.post("http://172.17.3.10/srun_portal_pc.php?", data=payload, headers=headers)
            ret = response.content.decode('utf-8')
        except Exception as e:
            print(f"请求失败: {e}")
        
        if self.debug:
            print(ret)
        
        if self.cache:
            with open(self.cache_path / 'response.html', 'w', encoding="utf-8") as f:
                f.write(ret)
        return ret
    
    def prase(self, ret):
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            print("未安装 bs4，不进行解析")
            print(ret)
            return
        soup = BeautifulSoup(ret, 'html.parser')

        # handle with error msg
        for p in soup.find_all('form', )[0].find_all('p'):
            if p.text.startswith('E'):
                print(p.text)
                raise Exception(p.text)
            
        table = soup.find_all('table')[0]
        skip = True
        for row in table.find_all('tr'):
            if skip:
                skip = False
                continue
            row_data = []
            for cell in row.find_all('td'):
                t = cell.get_text(strip=True)
                if t is not None and t != '':
                    row_data.append(t)
            if len(row_data) > 0:
                print("\n".join(row_data))
                print('=============')        