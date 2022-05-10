import re
from pathlib import Path
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

path = Path(__file__).parent / "thino" / "__init__.py"
version = re.search(r'\d[.]\d[.]\d',path.read_text()).group(0) #type: ignore

packages = [
    'thino',
]


extras_require = {
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions',
    ],
}

setup(
    name='thino',
    author='SawshaDev',
    version=version,
    packages=packages,
    license='MIT',
    description='An asynchronous python wrapper around the GitHub API',
    install_requires=requirements,
    python_requires='>=3.8.0',
)