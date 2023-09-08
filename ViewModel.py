def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class ViewMode():
    def __init__(self):
        self._selected_date = None
        print('初始化')
    def get_selected_date(self):
        return self._selected_date

    def set_selected_date(self, date):
        self._selected_date = date

instance1 = ViewMode()
instance1.set_selected_date(9999)
instance2 = ViewMode()
print(instance2.get_selected_date())

print(instance1 is instance2)
