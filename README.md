### Basic E-learning website

##### Setup Instructions
```
git clone [this_repo] the_learning_site
cd the_learning_site
virtualenv venv
source venv/bin/activate
pip install requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
