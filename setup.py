from setuptools import setup

setup(name='weather_forecast',
      version='0.1',
      description='Location based weather forecast package',
      url='',
      author='Karthik',
      author_email='karthik.cool1300@gmail.com',
      license='MIT',
      packages=['weather_forecast'],
      install_requires=[
          'geopy',
      ],
      zip_safe=False)