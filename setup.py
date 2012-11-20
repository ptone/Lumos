from setuptools import setup, find_packages

pkg_name = "Lumos"
setup(
    name = pkg_name,
    version = __import__(pkg_name.lower()).__version__,
    description='Pure Python implementation of E1.31 DMX over Ethernet',
    #long_description=open('docs/usage.txt').read(),
    author='Preston Holmes',
    author_email='preston@ptone.com',
    url='https://github.com/ptone/lumos',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)

