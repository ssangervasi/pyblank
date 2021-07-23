from setuptools import find_packages, setup

setup(
    name="blank",
    version="0.1",
    py_modules=["blank"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points="""
        [console_scripts]
        blank=main:main
    """,
)
