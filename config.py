# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = True

# Define the database - we are working with
# Connect with MongoDB
# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
MONGODB_SETTINGS = {
    'host': 'mongodb+srv://shy79:Huan%40bx64m@cluster0.6os6h.mongodb.net/feedbacks?retryWrites=true&w=majority',
    'connect': False,
}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Upload configs
MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # max file size is 2 MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Upload images
UPLOAD_FOLDER = '/Users/revudev/WorkSpace/myself/training/python/flask/media/uploads/'
