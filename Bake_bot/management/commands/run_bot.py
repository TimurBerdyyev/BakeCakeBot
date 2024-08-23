from django.core.management.base import BaseCommand
from Bake_bot.management.commands.tg_bot import main


class Command(BaseCommand):
    help = "Запускаем бота"

    def handle(self, *args, **options):
        main()