from setuptools import setup

setup(
    name = "youdao",
    version = '1.0',
    packages = ['youdao'],
    entry_points =  {
        'console_scripts': [
            'youdao = youdao.youdao:main'
    ]
    })
