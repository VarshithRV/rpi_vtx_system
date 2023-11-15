from setuptools import find_packages, setup

package_name = 'rpi_vtx_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='barracuda',
    maintainer_email='vrv278@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = rpi_vtx_system.publisher:main',
                'listener = rpi_vtx_system.subscriber:main',
                'get_RPYA = rpi_vtx_system.getRPYA:main'
        ],
    },
)
