from setuptools import setup

setup(
    name='euler',
    version='0.1',
    description='euler',
    url='http://github.com/jmsung/euler',
    author='Jongmin Sung',
    author_email='jongmin.sung@gmail.com',
    install_requires=[
        'docopt',
        'tables',
        'pathlib',
        'ipdb',
    ],
    scripts=['scripts/myfunc.py'],
    include_package_data=True,
)
