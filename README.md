### Basic E-learning website

##### Setup Instructions
```
git clone git@github.com:FalloutX/learning_site.git the_learning_site
cd the_learning_site
virtualenv venv
source venv/bin/activate
pip install requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Pages

##### Course List Page
![Main Course List Page](http://i.imgur.com/sVFfvYL.png)
##### Course Detail Page
![Course Details Page with list of Steps](http://i.imgur.com/zNrXZBr.png)
##### Step Detail Page
![Step Reading Page](http://i.imgur.com/0rjMhz9.png)
