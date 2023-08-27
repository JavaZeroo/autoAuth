class Config():
    def __init__(self, username, password, *args, **kargs) -> None:
        self.username = str(username)
        self.password = str(password)


class yidong(Config):
    def __init__(self, username, password, *args, **kargs) -> None:
        super().__init__(username, password)
        self.domain = '@yidong'
class liantong(Config):
    def __init__(self, username, password, *args, **kargs) -> None:
        super().__init__(username, password)
        self.domain = '@liantong'
class dianxin(Config):
    def __init__(self, username, password, *args, **kargs) -> None:
        super().__init__(username, password)
        self.domain = '@dianxin'
class jiaoyu(Config):
    def __init__(self, username, password, *args, **kargs) -> None:
        super().__init__(username, password)
        self.domain = '@jiaoyu'
        
domain_configs = {
    'yidong': yidong, 
    'liantong': liantong, 
    'dianxin': dianxin, 
    'jiaoyu': jiaoyu,
}