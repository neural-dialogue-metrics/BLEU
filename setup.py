from setuptools import setup

setup(
    name='BLEU',
    version='0.1',
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
    scripts=['bleu_metric.py'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache-v2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic'
    ],
    license='LICENCE.txt',
    long_description=open('README.md').read(),
)
