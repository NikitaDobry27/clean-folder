from setuptools import setup, find_namespace_packages


setup(
    name='clean-folder',
    version='1.0',
    description='Sorts files in the folder',
    url='https://github.com/NikitaDobry27/clean-folder',
    author='Nikita Bazhenov',
    author_email='bazhenov.nikita27@gmail.com',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean-folder.sort:final_sort']}
)