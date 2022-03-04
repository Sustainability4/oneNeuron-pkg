import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# We need to mention the project name, just make sure the project name is unique. 
# user name here has been added as the username for github repository. We decided with this username as we need to access the same in our URLs 
# 
    
PKG_NAME = "oneNeuron_pkg"
USER_NAME = "sustainability4"
PROJECT_NAME = "oneNeuron-pkg"

setuptools.setup(
    name=f"{PKG_NAME}-{USER_NAME}",
    version="0.0.3",
    author=USER_NAME,
    # provide the name of the author 
    author_email="rohan.prospects@gmail.com",
    description="A small package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    # Please make the python requirements liberal in a sense that it does not throw unnecessary errors
    python_requires=">=3.6",
    # install requirements are just a copy paste job from your requirements.txt file
    install_requires=[
        "numpy==1.21.4",
        "pandas==1.3.4",
        "joblib==1.1.0"
    ]
)
