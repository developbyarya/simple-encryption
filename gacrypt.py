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

class GAcrypt(CharData):
    def encrypt(self, string: str) -> str:
        new_str_indx = []
        new_string = []

        for d in string:
            indx = self.FULL.index(d) + 1
            new_str_indx.append([indx - 3, indx + 2])

        for ind in new_str_indx:
            for ind2 in ind:
                if ind2 > 94:
                    ind2n = ind2 - 94
                    ind[ind.index(ind2)] = ind2n
            new_string.extend([self.FULL[ind[0] - 1], self.FULL[ind[1] - 1] ])
        return "".join(new_string)
    
    def decrypt(self, string: str) -> str:
        src_list = []
        counter = 1
        for d in string:
            str_idx = self.FULL.index(d) + 1
            src_list.append(str_idx)

        # merge array into proper format
        counter = 1
        n_src_list = []
        string_scr = ""
        for d in src_list:
            if counter % 2 == 0:
                counter += 1
                continue
            n_src_list.append([d + 3, src_list[src_list.index(d) + 1] - 2 ])
            counter += 1

        for d in n_src_list:
            if d[0] > 94:
                d[0] -= 94
            if d[1] > 94:
                d[1] -= 94
            string_scr += self.get_char_from_index(d[0])
        return string_scr