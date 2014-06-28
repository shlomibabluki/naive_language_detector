from setuptools import setup


setup(
    name='nlp',
    version='0.0.1',
    description='Naive Language Detector',
    maintainer='Shlomi Babluki',
    maintainer_email='shlomi@swayy.co',
    url='https://github.com/SummerHQ/nlp',
    packages=['naive_language_detector'],
    install_requires=[
        'nltk==2.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=True
)