from Validation import Validation


#Клас ВІДДІЛ:
# ID, title, director_name, phone_number, monthly_budget, yearly_budget, website_url.
el = Validation()


class Department(object):
    def __init__(self, user_id, title, director_name, phone_number, monthly_budget, yearly_budget, website_url):
        self.user_id = user_id
        self.title = title
        self.director_name = director_name
        self.phone_number = phone_number
        self.monthly_budget = monthly_budget
        self.yearly_budget = yearly_budget
        self.website_url = website_url

    def __str__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + "\n"
        return result

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, val):
        self._user_id = val

    @property
    def title(self):
        return self._title

    @title.setter
    @Validation.decorator_string
    def title(self, val):
        self._title = val

    @property
    def director_name(self):
        return self._director_name

    @director_name.setter
    @Validation.decorator_string
    def director_name(self, val):
        self._director_name = val

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    @Validation.decorator_nomer
    def phone_number(self, val):
        self._phone_number = val

    @property
    def monthly_budget(self):
        return self._monthly_budget

    @monthly_budget.setter
    @Validation.decorator_price
    def monthly_budget(self, val):
        self._monthly_budget = val

    @property
    def yearly_budget(self):
        return self._yearly_budget

    @yearly_budget.setter
    @Validation.decorator_price
    def yearly_budget(self, val):
        self._yearly_budget = val
        el.validate_salary(self.monthly_budget, self.yearly_budget)

    @property
    def website_url(self):
        return self._website_url

    @website_url.setter
    @Validation.decorator_url
    def website_url(self, val):
        self._website_url = val


    def input(self):
       K = dict((i, input(i)) for i in dir(self)
                     if not i.startswith("__") and not i.startswith("_") and i != "input")
       for (key, value) in K.items():
           setattr(self, key, K.get(key, value))
       return K
