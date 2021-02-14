import unittest
from Memento import *
from task import add_Memento

A_object = Department(**{'ID': '456211',
                         'title': 'github',
                         'director_name': 'Mahdenko',
                         'phone_number': '+380992796411',
                         'monthly_budget': '3600',
                         'yearly_budget': '59200',
                         'website': 'https://github.com'})
B_object = Department(**{'ID': '354122',
                         'title': 'stackoverflow',
                         'director_name': 'Kis',
                         'phone_number': '+380602234789',
                         'monthly_budget': '6478.50',
                         'yearly_budget': '42369',
                         'website': 'https://stackoverflow.com'})
C_object = Department(**{'ID': '479526',
                         'title': 'Snstagram',
                         'director_name': 'Semko',
                         'phone_number': '+380954712632',
                         'monthly_budget': '15500',
                         'yearly_budget': '100000',
                         'website': 'https://www.instagram.com'})

originator = Originator()
caretaker = CareTaker()

class Tests(unittest.TestCase):
    def setUp(self):
        self.list = [A_object, B_object, C_object]   #звичайний список заповнений об'єктами типу Department
        self.element = Composition(*self.list)       #список типу Composition()

    def test_read(self):
        for_read = Composition()
        size = len(for_read)
        for_read.read_txt("Information")
        self.assertEqual(str(self.element), str(for_read))
        self.assertNotEqual(len(for_read), size)


    def test_sort(self):
        copy = self.element.copy()
        self.list = sorted(self.list, key=lambda el: getattr(el, "ID"))
        for i in range(len(self.element)):
            self.assertEqual(str(self.element.sort("ID")[i]), str(self.list[i]))
            self.assertNotEqual(str(self.element.sort("ID")), str(copy))

    def test_deleteID(self):
        id = "354122"
        copy = self.element.copy()
        for i in self.list:
            if int(i.ID) == int(id):
                self.list.remove(i)
        self.element.delete_by_id(id)
        for i in range(len(self.element)):
          self.assertEqual(str(self.element[i]), str(self.list[i]))
        self.assertNotEqual(len(self.element), len(copy))

    def test_add(self):
        copy = self.element.copy()
        new = Department(**{'ID': '45698',
                            'title': 'Element',
                            'director_name': 'Veres',
                            'phone_number': '+380504129654',
                            'monthly_budget': '1000',
                            'yearly_budget': '300000',
                            'website': 'https://rp5.ua'})
        self.element.add(new)
        self.assertEqual(len(self.element), len(copy)+1)
        self.assertNotEqual(len(self.element), len(copy))

    def test_search(self):
        key = "stack"
        for_search = Composition()
        key = key.lower()
        KeY = key.capitalize()
        for i in self.list:
            for j in i.__dict__.values():
                if key in j or KeY in j:
                    for_search.add(i)
                    break
        self.assertEqual(str(self.element.search(key)), str(for_search))

    def test_edit(self):
        new = Department(**{'ID': '45698',
                            'title': 'Element',
                            'director_name': 'Veres',
                            'phone_number': '+380504129654',
                            'monthly_budget': '1000',
                            'yearly_budget': '300000',
                            'website': 'https://rp5.ua'})
        id = "354122"
        self.element.edit_by_id(id, new)
        counter = 0
        old = Department()
        for i in range(len(self.list)):
            if int(self.list[i]._ID) == int(id):
                counter = i
                old = self.list[i]
                self.list.insert(i, new)
                self.list.remove(self.list[i + 1])
        self.assertEqual(str(self.element[counter]), str(self.list[counter]))
        self.assertNotEqual(str(self.element[counter]), str(old))


    def test_undo(self):
        add_Memento(originator, caretaker, self.element)
        self.element.sort("title")
        add_Memento(originator, caretaker, self.element)
        copy = self.element.copy()
        originator.restore(caretaker.undo())
        for i in range(len(self.element)):
            self.assertEqual(str(originator.getNote()[i]), str(self.list[i]))
        self.assertNotEqual(str(originator.getNote()), str(copy))

    def test_redo(self):
        add_Memento(originator, caretaker, self.element)
        self.element.sort("ID")
        add_Memento(originator, caretaker, self.element)
        copy = self.element.copy()
        self.element.sort("director_name")
        add_Memento(originator, caretaker, self.element)
        originator.restore(caretaker.undo())
        originator.restore(caretaker.redo())
        self.list = sorted(self.list, key=lambda el: getattr(el, "director_name"))
        for i in range(len(self.element)):
            self.assertEqual(str(originator.getNote()[i]), str(self.list[i]))
            self.assertNotEqual(str(originator.getNote()[i]), str(copy)[i])

    def test_write(self):
        for_write = Composition()
        for_write.add(A_object)
        for_write.write_txt("Test_write")
        example = Composition()
        example.read_txt("Test_write")
        self.assertNotEqual(str(example), str(A_object))
        self.assertEqual(str(example), str(A_object)+'\n')


unittest.main()
