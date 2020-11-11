from setuptools import setup, find_packages

setup(
    name = "code_quiz",
    version = "0.0.1",
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires = [
    ],
    author = "foobar",
    description=('code quiz'),
    entry_points={
        'console_scripts': [
            'quiz_cli=quiz.cli:main'
        ]
    }
)
