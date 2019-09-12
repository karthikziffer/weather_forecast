from setuptools import setup

setup(name='weather_forecast',
      version='0.45',
      description='Location based weather forecast package',
      long_description= 'The pip package provides weather forecasting information based on location or address. Using address, the weather_forecast provides location specific forecast. Currently only one function is included i.e forecast.',
      url='https://github.com/karthikziffer/weather_forecast',
      author='Karthik',
      author_email='karthik.cool1300@gmail.com',
      license='MIT',
      packages=['weather_forecast'],
      install_requires=[
          'geopy',
      ],
      zip_safe=False)