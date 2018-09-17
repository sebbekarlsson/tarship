from setuptools import setup, find_packages


setup(
    name='tarship',
    version='1.0.1',
    install_requires=[
        'paramiko',
        'scp'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tarship = tarship.bin:run'
        ]
    }
)
