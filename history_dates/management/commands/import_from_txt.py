from django.core.management.base import BaseCommand
from history_dates.models import HistoricalEvent

class Command(BaseCommand):
    help = 'Imports events from year-eventname txt file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to txt file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        count = 0
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    # Разделяем строку на год и событие
                    year, event_name = line.split(' ', 1)
                    
                    # Создаем запись в базе
                    HistoricalEvent.objects.create(
                        title=event_name,
                        date=year,
                    )
                    count += 1
                    
                except ValueError:
                    self.stdout.write(self.style.ERROR(f'Ошибка в строке: "{line}"'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Ошибка: {e}'))

        self.stdout.write(self.style.SUCCESS(f'Успешно импортировано {count} событий'))