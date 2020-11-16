<<<<<<< HEAD
#!/home/daisy/Desktop/Realestate-house-grp7/Realestate-house-grp7/virtual/bin/python
=======
#!/home/moringa/Desktop/moringa-school-projects/Realestate-house-grp7/virtual/bin/python3
>>>>>>> dd0a1cd275881e27a4f4c3ed60cf8e353476e8fb
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
