from setuptools import find_packages, setup

package_name = 'gripper_core'

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
    maintainer='ubuntu',
    maintainer_email='kalanaratnayake95@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'modbus_server = gripper_core.modbus_server:main',
            'destination_publisher = gripper_core.destination_publisher:main',
            'tcp_publisher = gripper_core.tcp_publisher:main'
        ],
    },
)
