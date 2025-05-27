from address import Address
from mailing import Mailing
address = Address('00000',
                  'Moscow',
                  'Lenina',
                  '43',
                  '8'
                  )
mailing = Mailing(Address('00001',
                  'London',
                  'Marks',
                  '45',
                  '9'),
                  Address(
                '00001',
                  'Minsk',
                  'Gagarina',
                  '76',
                  '4'
                  ),
                  500,
                  'SomeStuff')
print(f'Отправление '
      f'{mailing.track} из {mailing.from_address},'
      f'  в {mailing.to_address} . Стоимость {mailing.cost} рублей.')
