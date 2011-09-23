from setuptools import setup, find_packages

setup(
      name="Blogy",
      version="0.1",
      packages=find_packages(),

      install_requires=['django-taggit',
                        'django-markitup',
                        'pygments',
                        'docutils',
                        ],

      include_package_data = True,
      )

