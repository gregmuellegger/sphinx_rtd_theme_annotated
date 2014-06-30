# -*- coding: utf-8 -*-
"""`sphinx_rtd_theme_annotated` lives on `Github`_.

.. _github: https://www.github.com/gregmuellegger/sphinx_rtd_theme_annotated

"""
from setuptools import setup
from sphinx_rtd_theme_annotated import __version__


setup(
    name='sphinx_rtd_theme_annotated',
    version=__version__,
    url='https://github.com/gregmuellegger/sphinx_rtd_theme_annotated/',
    license='MIT',
    author='Gregor Müllegger',
    author_email='gregor@muellegger.de',
    description='Sphinx theme with annotations about documentation quality, based upon the Read The Docs default theme.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_rtd_theme_annotated'],
    package_data={'sphinx_rtd_theme_annotated': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
