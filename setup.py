from setuptools import setup

setup(
    name='VKManager',
    version='0.9.7',
    description='Vault Keys Manager It is a password manager with interface programmed in python with the help of CustomTkinter (CTK) and MySQL.',
    url='https://github.com/14wual/VKManager',
    author='Carlos Padilla Labella',
    author_email='cpadlab@gmail.com',
    license='GPL',
    install_requires=[
        'customtkinter',
        'mysql.connector',
        'pillow',
        'pyperclip',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/14wual/VKManager/issues',
        'Source': 'https://github.com/14wual/VKManager/blob/main/main.py',
    },
)
