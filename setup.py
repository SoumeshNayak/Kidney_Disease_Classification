import setuptools

with open("README.md",'r',encoding="utf-8") as f:
    ld=f.read()
    
__version__="0.0.0"

REPO_NAME= "Kidney_Disease_Classification"    
AUTHOR_USER_NAME="SoumeshNayak"
SRC_REPO="cnnClassifier"
#AUTHOR_EMAIL: "soumeshnayak2210@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    # author_email=AUTHOR_EMAIL,
    description="A python package for CNN classifier",
    long_description=ld,
    url=f"http://github.com//{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)