from setuptools import setup

setup(
    name='gearman',
    version='0.7.1',
    author='Jiaze Gao',
    author_email='gaojiaze@papayamobile.com',
    description='Elixir - a lightweight declarative layer on top of SqlAlchemy',
    long_description=open('README.md').read(),
    url='https://github.com/peggygao1988/elixir/',
    packages=['elixir'],
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
