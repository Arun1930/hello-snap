from setuptools import setup

setup(
    name='hello_world_snap',
    version='0.1',
    description='say hello',
    url='https://github.com/friedmanss/hello-snap',
    author='Sam Friedman',
    author_email='samuel.s.friedman@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    packages=['datahub', 'datahub.modbus_module'],
    entry_points={
        'console_scripts': ['say-hello=modbus_module.say_hello:main'],
    },
    zip_safe=False)
