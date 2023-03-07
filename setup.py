from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder',
    version='1',
    description='Very useful code',
    url='http://github.com/dummy_user/useful',
    author='NikitaDobry27',
    author_email='bazhenov.nikita27@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:final_sort']}
)
