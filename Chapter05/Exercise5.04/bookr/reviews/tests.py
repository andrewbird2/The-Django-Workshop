import os
from shutil import rmtree

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


def read_content(path):
    with open(path) as f:
        return f.read()


class Exercise4Test(TestCase):
    def test_django_conf(self):
        """
        Check that `reviews` is in `settings.INSTALLED_APPS`, the static dir is set to <projectdir>/static, and
        STATIC_DIR is set to the static_temp directory.
        """
        self.assertIn('reviews', settings.INSTALLED_APPS)
        self.assertEquals([settings.BASE_DIR + '/static'], settings.STATICFILES_DIRS)
        self.assertEquals(settings.BASE_DIR + '/static_temp', settings.STATIC_ROOT)

    def test_collect_static(self):
        """Test the result of the collectstatic command."""
        static_output_dir = os.path.join(settings.BASE_DIR, 'static_temp')
        call_command('collectstatic', '--noinput')
        self.assertTrue(os.path.isdir(static_output_dir))
        self.assertTrue(os.path.isdir(os.path.join(static_output_dir, 'admin')))
        self.assertTrue(os.path.exists(os.path.join(static_output_dir, 'reviews', 'logo.png')))
        self.assertTrue(os.path.exists(os.path.join(static_output_dir, 'main.css')))
        rmtree(static_output_dir)