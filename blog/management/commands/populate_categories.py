from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This is the category data'
    
    def handle(self, *args, **options):
        
        
      categories = ['school','college','hospital','home']
      
      for catogory_name in categories:
          Category.objects.create(name = catogory_name)
          
      self.stdout.write(self.style.SUCCESS("INSERTINg THE DATA"))