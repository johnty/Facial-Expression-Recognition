import setuptools

setuptools.setup(
    name='face-demo',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'tensorflow==1.15.0',
        'python-osc'
    ]
)