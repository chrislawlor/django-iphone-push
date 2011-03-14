from distutils.core import setup

setup(
    name="django-iphone-push",
    version="1.0",
    description="Add iPhone Push notifications to a Django Project quickly and easily",
    author="Lee Packham",
    author_email="lpackham@leenux.org.uk",
    url="http://leepa.github.com/django-iphone-push/",
    packages=['iphone_push', 'iphone_push.migrations'],
    platforms=["any"],
    license="See LICENSE.txt",
)