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

with open('LICENSE.md', 'r') as fh:
    LICENSE = fh.read()

setuptools.setup(
    name='single-body-thermal-equil',
    version='0.0.0',
    author='Matthew Vernacchia',
    author_email='mvernacc@mit.edu',
    description='Find the equilibirium temperature of a body with multiple conductive and radiative boundaries',
    url='https://github.com/mvernacc/single-body-thermal-equil',
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
