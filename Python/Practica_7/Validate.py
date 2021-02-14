class Validate():
    @staticmethod
    def valid_positive(message):
        while True:
            try:
                el = int(input(message))
                if el < 0:
                    print("Number must be positive! Please, try again")
                    continue
                break
            except ValueError:
                print("Number must be an integer! Please, try again")
                continue
        return el

    @staticmethod
    def valid_response(message):
        while True:
            try:
                res = int(input(message))
                if res <= 0 or res > 9:
                    print("The value is incorrect. Please, try again")
                    continue
                break
            except ValueError:
                print("Number must be an integer! Please, try again")
                continue
        return res

    @staticmethod
    def validate_file(filename):
        try:
            file = open(filename)
            return True
        except IOError as e:
            print("File does not exist")