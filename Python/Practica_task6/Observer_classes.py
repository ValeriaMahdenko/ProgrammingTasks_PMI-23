class Logger:
    @staticmethod
    def write_to_file(li, file_name):
        f = open(file_name, 'a')
        f.write(str(li) + '\n')
        f.close()

    @staticmethod
    def clean_file(file_name):
        open(file_name, 'w').close()

class Observer:

    _list = {}
    def __init__(self):
        self._actions = []

    @staticmethod
    def new(key, _new):
        Observer._list[key] = _new

    def __repr__(self):
        return 'All actions: ' + ','.join(self._actions)

class Event:
    def __init__(self, name, old, new, pos1=None, pos2=None):
        self.name = name
        self.old = old
        self.pos1 = pos1
        self.pos2 = pos2
        self.new = new
        self.new_event()

    def new_event(self):
        el = Observer()
        for i in el.__dict__:
            if self.name in i:
                el._actions[self.name](self)
                break

    def __str__(self):
        if self.pos2 == None:
            return " "+str(self.name) + " on/by position " + str(self.pos1) + "  ->  " + "\t No changed list:" + \
                   str(self.old) + "\t\t New list: " + str(self.new) + " "
        elif self.pos1 == None:
            return " "+str(self.name) + " on/by position [" + str(self.pos2[0]) + "-" + str(self.pos2[1])+"]   ->  " + \
                   "\t No changed list:" + str(self.old) + "\t\t New list: " + str(self.new)
