import requests
from pathlib import Path
import yaml
from Config import domain_configs
from Loginer import Loginer

if __name__ == '__main__':
    ymlconfig = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
    config = domain_configs[ymlconfig['domain']](**ymlconfig)
    loginer = Loginer(config)
    res = loginer.login()
    loginer.prase(res)