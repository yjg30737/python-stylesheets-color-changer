from setuptools import setup, find_packages

setup(
    name='python-stylesheets-color-changer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Python CSS style sheets color changer',
    url='https://github.com/yjg30737/python-stylesheets-color-changer.git',
    install_requires=[
        'python-color-getter @ git+https://git@github.com/yjg30737/python-color-getter.git@main'
    ]
)