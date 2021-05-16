class CharData:
    def __split(string:str) -> list:
        return [char for char in string]
    __abc = __split("abcdefghijklmnopqrstuvwxyz")
    __abcCap = [char.upper() for char in __abc]
    __char = __split('()!~`@#$%^&*_-+={}[]|\:;"')
    __char2 = __split("'<>,.?/")
    __num = __split("0123456789")
    FULL = __abc + __char + __char2 + __num + __abcCap
    def get_index(self, string: str) -> int:
        return self.FULL.index(string) + 1
    def get_char_from_index(self, index:int)-> str:
        return self.FULL[index - 1 ]
    
char = CharData()