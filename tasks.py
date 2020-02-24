from functools import wraps
from invoke import task

def run_doc(func):
    """Self documenting code?"""
    @wraps(func)
    def new_task(ctx, *args, **kwargs):
        for line in func.__doc__.split("\n"):
            line = line.strip()
            ctx.run(line)
        func(ctx, *args, **kwargs)
    return new_task

@task
@run_doc
def start(ctx):
    """# This activates the virtual environment
    source venv/bin/activate
    """

@task
@run_doc
def stop(ctx):
    """# This deactivates the virtual environment
    source deactivate
    """

@task(pre=[start])
@run_doc
def install(ctx):
    """# This installs the requirements
    pip3 install -r requirements-dashboard.txt
    """

@task(pre=[start])
@run_doc
def down(ctx):
    """# This takes down the app
    pkill gunicorn
    """

@task(pre=[start, install])
@run_doc
def up(ctx):
    """# This brings up the app
    echo Collecting Static Files
    # python3 manage.py collectstatic --no-input

    echo Migrating
    python3 manage.py makemigrations
    python3 manage.py migrate

    echo Starting Gunicorn
    exec gunicorn --config=config/gunicorn.py dashboard.wsgi:application
    """

@task
@run_doc
def help(ctx):
    """# This lists the available methods
    inv --list
    """
