import random
import string
from django.utils import timezone

from .models import Question


#function create a random 7-letter hash, assign the entered URL to this hash, save it into the database, and finally return the hash
def shorten(url):
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Question(original_url=url, hash=random_hash, creation_date=timezone.now())
    mapping.save()
    return random_hash


# load the original URL from the given hash
def load_url(url_hash):
    return Question.objects.get(hash=url_hash)
