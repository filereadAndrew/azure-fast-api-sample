from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    'connexion==2.13.0',
    'uwsgi==2.0.21',
    'swagger-ui-bundle==0.0.9',
    'kombu==5.3.1',
    'sendgrid',
    'fastapi',
    'unidecode==1.3.4',
    'greenlet>2',
    'uvicorn[standard]',
    'sqlmodel',
    'fastapi-microsoft-identity',
    'uvicorn',
    'python-multipart'
]

CABAL_INSTALL_REQUIRES = [
    'core',
    'components',
]

setup(
    name='azure-fast-api-sample',
    version='1.0.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
