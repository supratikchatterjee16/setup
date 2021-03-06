# Setup Utility

This utility is to make sure about the deployment of the entire setup required for my purpose.

## System setup

Make use of the following softwares(ubuntu only):

### Programming
1. Firefox
2. Python3.8
3. Rust
4. C/C++(GNU)

### DBMS
1. SQLite
2. PostgreSQL
3. MongoDB

### Disk Utils
1. GParted

### Screen capture
1. Kazam
2. Spectacle

## Python setup

It makes use of pip to install everything required by the work environments across multiple projects.
This package makes sure about the Do Not Repeat Yourself logic.

Use the following command to setup python fast.

```shell
sudo apt install python3.8 python3.8-dev python3.8-venv python3.8-dbg
```

### List of python packages

1. Flask
2. Flask-WTF
3. Flask-SQLAlchemy
4. Flask-Migrate
5. Flask-Login
6. Flask-Table
7. urllib3
8. NumPy
9. NLTK
10. Requests
11. JSON
12. OpenCV(held for stable release on python3.8, see https://stackoverflow.com/questions/58892378/how-to-install-opencv-python-in-python-3-8)
13. Dash(is flask compatible)
14. python-psycopg2(Postgres)
15. PostgreSQL, server and client
16. MongoDB
17. PyMongo
18. Compass(MongoDB utility for working with collections and exploring them)
19. VirtualEnv
20. beautifulsoup4
21. lxml(required for BS4 Parsing)
22. feedparser(RSS)
21. SciPy
22. SymPy
23. httplib2
24. PanDas(Dataset loader)

### Post installation installations

Setup NLTK for use.

```python
import nltk
nltk.download('all')
```

Perform sanity checks for all utilities.

```python
# Script pending
```

Create provisions for working with PostgreSQL and MongoDB.
Provisions include creating utilites to auto migrate schemas at any given point of time.
Mogration strategies would be made use of to make sure nothing is ever irreversibly changed.


