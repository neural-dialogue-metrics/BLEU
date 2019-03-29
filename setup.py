from setuptools import setup

__version__ = '0.2.3'

setup(
    name='BLEU',
    version=__version__,
    description='implementation of BLEU metrics for machine translation',
    url='https://github.com/neural-dialogue-metrics/BLEU.git',
    author='cgsdfc',
    author_email='cgsdfc@126.com',
    keywords=[
        'NL', 'CL', 'MT',
        'natural language processing',
        'computational linguistics',
        'machine translation',
    ],
    packages=[
        'bleu',
        'bleu.tests',
    ],
    package_data={
        'bleu.tests': ['data/*'],
    },
    scripts=['bleu_metric.py'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache-v2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
    ],
    license='LICENCE.txt',
    long_description=open('README.md').read(),
)
