from setuptools import setup, find_packages


setup(
    name='tarploy',
    version='1.0',
    install_requires=[
        'paramiko'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tarploy = tarploy.bin:run'
        ]
    }
)
