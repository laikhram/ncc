class User(object):

    def __init__(self, userid, firstname, lastname):
        self.userid = userid
        self.firstname = User.upperCase(firstname)
        self.lastname = User.upperCase(lastname)

    def __str__(self):
        return self.userid + ", " + self.firstname + ", " + self.lastname

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def upperCase(name):
        first_letter = name[:1]
        second_letter = name[1:].lower()
        return first_letter + second_letter

    if __name__ == '__main__':
        print upperCase('LAIKHRAM')