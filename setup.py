from setuptools import setup, find_packages

setup(
    name='nginxtest',
    version='0.1.0',
    description='Check your Nginx config',
    url='https://github.com/factorysh/nginx-test',
    install_requires=[
        'crossplane',
    ],
    licence="BSD",
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: 3 terms BSD licenee',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    extras_require={
        'test': ['pytest', 'pytest-cov'],
        'pex': ['pex'],
    },
    entry_points='''
    [console_scripts]
    nginx-cli = nginxtest.cli:main
    ''',
)
