class Bmw:
    def __init__(self,title,model,weight,nm,max_speed,color):
        self.title = title
        self.model = model
        self.weight = weight
        self.nm = nm
        self.max_speed = max_speed
        self.color = color


    def start_engine(self):
        print(f'{self.title} {self.model} engine started!\n')


    def stop_engine(self):
        print(f'{self.title} {self.model} engine stopped!\n')


    def info(self):
        print(f'Here is all the information about the car:\n'
              f'Название:{self.title}\n'
              f'Модель:{self.model}\n'
              f'Вес:{self.weight}\n'
              f'Нано метр:{self.nm}\n'
              f'Максимальная  скорость:{self.max_speed}\n'
              f'Цвет:{self.color}')

bmw1 = Bmw(title='Bmw',model='M2',weight='1,650 kg',nm='0-200',max_speed='270 per hour',color='blue')

bmw1.info()




class Mercedes:
    def __init__(self,title,model,weight,nm,max_speed,color):
        self.title = title
        self.model = model
        self.weight = weight
        self.nm = nm
        self.max_speed = max_speed
        self.color = color


    def start_engine(self):
        print(f'{self.title} {self.model} engine started!\n')


    def stop_engine(self):
        print(f'{self.title} {self.model} engine stopped!\n')


    def info(self):
        print(f'Here is all the information about the car:\n'
              f'Название:{self.title}\n'
              f'Модель:{self.model}\n'
              f'Вес:{self.weight}\n'
              f'Нано метр:{self.nm}\n'
              f'Максимальная  скорость:{self.max_speed}\n'
              f'Цвет:{self.color}')


mercedes = Mercedes(title='Mercedes',model='s-class',weight='1,560 kg',nm='0-300',max_speed='370 per hour',color='black')


mercedes.stop_engine()