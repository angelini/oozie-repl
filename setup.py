from codecs import open as codecs_open
from setuptools import setup, find_packages

setup(
    name='oozierepl',
    version='0.0.0',
    description='',
    long_description='',
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'colorama==0.3.7',
        'ipython==4.1.2',
        'requests==2.9.1',
    ],
    extras_require={
        'test': ['pytest'],
    },
    entry_points="""
    [console_scripts]
    oozierepl=oozierepl.scripts.repl:repl
    """
)