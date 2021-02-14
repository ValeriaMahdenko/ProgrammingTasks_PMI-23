from Validation import Validation

#Клас ВІДДІЛ:
# ID, title, director_name, phone_number, monthly_budget, yearly_budget, website_url.
el = Validation()


class Department(object):
    def __init__(self, **array):
        for(key, value) in array.items():
            setattr(self, key, array.get(key, value))

    def __str__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + "\n"
        return result

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, val):
        self._ID = el.validate_number(val)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = el.validate_string(val)

    @property
    def director_name(self):
        return self._director

    @director_name.setter
    def director_name(self, val):
        self._director = el.validate_string(val)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, val):
        self._phone_number = el.validate_nomer(val)

    @property
    def monthly_budget(self):
        return self._monthly_budget

    @monthly_budget.setter
    def monthly_budget(self, val):
        self._monthly_budget = el.validate_price(val)

    @property
    def yearly_budget(self):
        return self._yearly_budget

    @yearly_budget.setter
    def yearly_budget(self, val):
        self._yearly_budget = el.validate_price(val)
        el.validate_salary(self.monthly_budget, self.yearly_budget)

    @property
    def website(self):
        return self._website_url

    @website.setter
    def website(self, val):
        self._website_url = el.validate_url(val)


    def input(self):
        K = dict((i, input(i)) for i in dir(self)
                 if not i.startswith("__") and not i.startswith("_") and i != "input")
        for (key, value) in K.items():
            setattr(self, key, K.get(key, value))
