"""Standard python setup script."""
import setuptools

INSTALL_REQUIRES = [
    'numpy',
    'scipy',
    ]
TEST_REQUIRES = [
    'pytest',
    'coverage',
    'pytest-cov',
    ]

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

with open('LICENSE.md', 'r') as fh:
    LICENSE = fh.read()

setuptools.setup(
    name='single-body-thermal-equil',
    version='0.0.0',
    author='Matthew Vernacchia',
    author_email='mvernacc@mit.edu',
    description='Find the equilibirium temperature of a conductive body with multiple conductive and radiative boundaries.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/mvernacc/single-body-thermal-equilge',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
        },
    keywords='analysis-script engineering thermodynamics',
    license=LICENSE,
    include_package_data=True,
)
