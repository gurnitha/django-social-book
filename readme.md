### BUILDING FULL SOCIAL MEDIA APP USING DJANGO


### ================= 1. BASIC SETUP =====================


#### 1. Creaate venv, install django and create local repository

        new file:   .gitignore
        new file:   readme.md


### ================= 2. CREAET DJANGO PROJECT AND APP ===

#### 2.1 Create django project 'config' and django app 'core'

        E:.
        │   .gitignore
        │   manage.py
        │   readme.md
        │
        ├───config
        │       asgi.py
        │       settings.py
        │       urls.py
        │       wsgi.py
        │       __init__.py
        │
        └───core
            │   admin.py
            │   apps.py
            │   models.py
            │   tests.py
            │   views.py
            │   __init__.py
            │
            └───migrations
                    __init__.py


#### 2.2 Register the app to the project

        modified:   config/settings.py
        modified:   readme.md


### ================= 3. VIEWS, TEMPLATE, URLS ===========


#### 3.1 Create home page

        modified:   config/settings.py
        modified:   config/urls.py
        new file:   core/urls.py
        modified:   core/views.py
        modified:   readme.md
        new file:   templates/book/index.html


#### 3.2 Adding template for the home page

        modified:   readme.md
        modified:   templates/book/index.html


### ================= 4. SETTING UP STATIC AND MEDIA FILES


#### 4.1 Adding static files
        
        modified:   readme.md
        ...
        new file:   static/assets/js/jquery-3.3.1.min.js
        new file:   static/assets/js/simplebar.js
        new file:   static/assets/js/tippy.all.min.js
        new file:   static/assets/js/uikit.js


#### 4.2 Setting up static path

        modified:   config/settings.py
        modified:   readme.md


### ================= 5. USER PROFILE: REGISTRATION, LOGIN AND LOGOUT


#### 5.1 Sign up - Setting up media path

        modified:   config/settings.py
        modified:   config/urls.py
        modified:   readme.md


#### 5.2 Sign up - Adding some more static assets

        modified:   readme.md
        ...
        new file:   static/settings/js/worldHigh.js
        new file:   static/settings/js/worldLow.js
        new file:   static/settings/js/wow.min.js
        new file:   static/video/sonniebaduuk.mp4


#### 5.3 Sign up - Creating Profile model and register it to admin

        modified:   core/admin.py
        new file:   core/migrations/0001_initial.py
        modified:   core/models.py
        modified:   readme.md


#### 5.4 Sign up - User signup - Template, Views and Urls

        modified:   core/urls.py
        modified:   core/views.py
        modified:   readme.md
        new file:   templates/book/signup.html


#### 5.5 Sign up - Authenticate new sign up user

        modified:   core/views.py
        modified:   readme.md
        modified:   templates/book/signup.html


#### 5.6 Sign up - Display messages for new sign up user

        modified:   readme.md
        modified:   templates/book/signup.html


#### 5.7 Sign up - Testing - sign up a new user

        new file:   core/migrations/0002_alter_profile_profileimg.py
        modified:   core/models.py
        modified:   core/views.py
        modified:   templates/book/signup.html


#### 5.8 Modified readme file

        modified:   readme.md


### 5.9 Sign in


#### 5.9.1 Sign in - Creating Sign in page (Templates, Views, Urls)

        modified:   core/urls.py
        modified:   core/views.py
        modified:   readme.md
        new file:   templates/book/signin.html


#### 5.9.2 Sign in - Linking Sign up and Sign in pages

        modified:   readme.md
        modified:   templates/book/signin.html
        modified:   templates/book/signup.html


#### 5.9.3 Sign in - Sign in the user

        modified:   core/views.py
        modified:   readme.md
        modified:   templates/book/signin.html


### 5.10 Sign out


#### 5.10.1 Sign out - Sign out the user

        modified:   core/urls.py
        modified:   core/views.py
        modified:   readme.md
        modified:   templates/book/index.html


### 5.11 Restriction


#### 5.11.1 Restriction - Restriction - User must login to access the home page

        modified:   core/views.py
        modified:   readme.md


#### 5.11.2 Restriction - Making user sign in first before sign out

        modified:   core/views.py
        modified:   readme.md
