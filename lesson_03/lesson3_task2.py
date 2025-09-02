from smartphone import Smartphone
catalog = [
    Smartphone('Марка_1','Модель_1','Номер_1'),
    Smartphone('Марка_2','Модель_2','Номер_2'),
    Smartphone('Марка_3','Модель_3','Номер_3'),
    Smartphone('Марка_4','Модель_4','Номер_4'),
    Smartphone('Марка_5','Модель_5','Номер_5')
]
for i in catalog:
    print(f'{i.mark} - {i.model}. {i.number}')