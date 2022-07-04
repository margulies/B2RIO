
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
        name ='B2RIO',
        version ='0.0.1',
        author ='Gaston E. Zanitti',
        author_email ='gzanitti@gmail.com',
        url ='https://github.com/gzanitti/B2RIO',
        description ='Brain to Reverse Inference Ontology',
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'b2rio = b2rio.b2rio:run'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        install_requires = requirements,
        zip_safe = False
)