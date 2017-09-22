import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lujunxu.settings")
import django
django.setup()
from mysqlpool.models import Author




def save_author():
    c = Author(first_name='baidu',last_name='baiduers',email='lujunxucuc@gmail')
    c.save()

def all_author():
    c = Author.objects.all()
    print c

def get_author():
    c = Author.objects.filter(first_name='baidu')
    print c

def del_author():
    c = Author.objects.filter(first_name="baidu")
    c.delete()


if __name__ == '__main__':
    save_author()
    all_author()
    get_author()
    del_author()