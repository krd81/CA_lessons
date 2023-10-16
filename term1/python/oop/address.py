class Address:
    def __init__(self, address_list):
        self.address_1 = address_list[0]
        self.address_2 = address_list[1]
        self.address_3 = address_list[2]
        self.suburb = address_list[3]
        self.state = address_list[4]
        self.post_code = address_list[5]


def get_address_info(self):
    return self.address_1, self.address_2, self.address_3, self.suburb, self.state, self.post_code


