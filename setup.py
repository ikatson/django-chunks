from distutils.core import setup

setup(name='django-chunks',
      version='0.1.4',
      description='Keyed blocks of content for use in your Django templates',
      author='Clint Ecker',
      author_email='me@clintecker.com',
      url='http://code.google.com/p/django-chunks/',
      install_requires=['django-ckeditor-extras>=0.0.3', 'django-shared'],
      packages=['chunks', 'chunks.templatetags'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
