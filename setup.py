from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name=optoma-projector-rs232,
    version='0.1',
    description=A python class that communicates with Optoma Projector&#39;s over an RS232 serial link,
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    url='https://github.com/jonlidgard/optoma-projector-rs232',
    author='jonlidgard',
    # author_email='jonlidgard@gmail.com',
    license=MIT,
    packages=['optoma-projector-rs232'],
    install_requires=[
        'markdown',
    ],
    include_package_data=True,
    zip_safe=False
)
