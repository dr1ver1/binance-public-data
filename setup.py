from setuptools import setup, find_packages

setup(
    name='binance-public-data-dr1ver1',
    author='dr1ver1',
    version='0.1.0',
    description = 'Binance: To help users download our public data easily, we have put all Kline, Trade, and AggTrade data for all pairs, month by month, online.',
    url='https://github.com/dr1ver1/binance-public-data',
    packages=find_packages(include=['binanceData', 'binanceData.*', 'Futures_Order_Book_Download', 'Futures_Order_Book_Download.*', 'data', 'data.*']),
    install_requires=[
        'pandas'
    ],
    # setup_requires=['pytest-runner', 'flake8'],
    # tests_require=['pytest'],
    # entry_points={
    #     'console_scripts': ['my-command=exampleproject.example:main']
    # },
    # package_data={'exampleproject': ['data/*.txt']}
)