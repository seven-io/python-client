import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    author='sms77 e.K.',
    author_email='support@sms77.io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    description='A Python wrapper for the Sms77.io SMS gateway.',
    name='sms77api',
    install_requires=['requests'],
    keywords='sms, text2voice, hlr, cnam, mnp',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.4, <4',
    url='https://github.com/seven-io/python-client',
    version='2.0.0',
)
