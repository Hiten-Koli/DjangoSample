from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_init, pre_save, post_delete, post_init, post_save, pre_migrate, post_migrate
from django.core.signals import request_finished, request_started, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("=================")
    print("Logged in signal")
    print(f'Sender: {sender}')
    print(f'Request: {request}')
    print(f'User: {user}')
    print(f'Kwargs: {kwargs}')

#user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("=================")
    print("Logged out signal")
    print(f'Sender: {sender}')
    print(f'Request: {request}')
    print(f'User: {user}')
    print(f'Kwargs: {kwargs}')

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("=================")
    print("Login failed signal")
    print(f'Sender: {sender}')
    print(f'Request: {request}')
    print(f'Credentials: {credentials}')
    print(f'Kwargs: {kwargs}')

@receiver(pre_save, sender = User)
def before_saving(sender, instance, **kwargs):
    print("=================")
    print("PreSave Signal")
    print(f'Sender: {sender}')
    print(f'Instance: {instance}')
    print(f'Kwargs: {kwargs}')

@receiver(post_save, sender = User)
def before_saving(sender, instance, created, **kwargs):
    if created:
        print("=================")
        print("post save Signal....Created New Record ")
        print(f'Sender: {sender}')
        print(f'Instance: {instance}')
        print(f'Created: {created}')
        print(f'Kwargs: {kwargs}')
    else:
        print("=================")
        print("post save Signal....Record Updated")
        print(f'Sender: {sender}')
        print(f'Instance: {instance}')
        print(f'Created: {created}')
        print(f'Kwargs: {kwargs}')

@receiver(pre_delete, sender = User)
def before_deleting(sender, instance, **kwargs):
    print("=================")
    print("before deleting Signal")
    print(f'Sender: {sender}')
    print(f'Instance: {instance}')
    print(f'Kwargs: {kwargs}')

@receiver(post_delete, sender = User)
def after_deleting(sender, instance, **kwargs):
    print("=================")
    print("after deleting Signal")
    print(f'Sender: {sender}')
    print(f'Instance: {instance}')
    print(f'Kwargs: {kwargs}')

@receiver(pre_init, sender = User)
def before_init(sender, *args, **kwargs):
    print("=================")
    print("Before init Signal")
    print(f'Sender: {sender}')
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')

@receiver(post_init, sender = User)
def after_init(sender, *args, **kwargs):
    print("=================")
    print("After init Signal")
    print(f'Sender: {sender}')
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')

@receiver(request_started)
def after_init(sender, environ, **kwargs):
    print("=================")
    print("At beginning of request")
    print(f'Sender: {sender}')
    print(f'Environ: {environ}')
    print(f'Kwargs: {kwargs}')

@receiver(request_finished)
def after_init(sender, **kwargs):
    print("=================")
    print("At End of request")
    print(f'Sender: {sender}')
    print(f'Kwargs: {kwargs}')

@receiver(got_request_exception)
def after_init(sender, request, **kwargs):
    print("=================")
    print("At request Exception")
    print(f'Sender: {sender}')
    print(f'Request: {request}')
    print(f'Kwargs: {kwargs}')

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("=================")
    print("Before Installing App...")
    print(f'Sender: {sender}')
    print(f'App Config: {app_config}')
    print(f'Verbosity: {verbosity}')
    print(f'Interactive: {interactive}')
    print(f'Using: {using}')
    print(f'Plan: {plan}')
    print(f'Apps: {apps}')
    print(f'Kwargs: {kwargs}')


@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("=================")
    print("After Installing App...")
    print(f'Sender: {sender}')
    print(f'App Config: {app_config}')
    print(f'Verbosity: {verbosity}')
    print(f'Interactive: {interactive}')
    print(f'Using: {using}')
    print(f'Plan: {plan}')
    print(f'Apps: {apps}')
    print(f'Kwargs: {kwargs}')


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("=================")
    print("initial connenction to db...")
    print(f'Sender: {sender}')
    print(f'Connection: {connection}')
    print(f'Kwargs: {kwargs}')