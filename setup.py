from setuptools import setup, find_packages

setup(
    name = 'pygments-style-tomorrow',
    version = '0.1',
    description = 'Pygments style plugin of Tomorrow',
    license = 'BSD',

    author = 'Cristian Prieto',
    author_email = 'me@cprieto.com',

    url = 'https://github.com/cprieto/pygments-style-tomorrow',

    packages = ['pygments_style_tomorrow'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      tomorrow = pygments_style_tomorrow:TomorrowStyle''',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)