try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  #  can't have the entry_points option here.

setup(name='suggestparse',
      version='1.0.0',
      author = "Ahmed T. Youssef",
      author_email="xmonader@gmail.com",
      description='argparse with suggestions',
      long_description='argparse with suggestions for the closest matches for invalid opts',
      py_modules=['suggestparse'],
      url="http://github.com/xmonader/suggestparse",
      license='BSD 3-Clause License',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
       )


