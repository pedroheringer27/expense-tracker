from setuptools import setup

setup(
    name='expense-tracker',
    version='1.0.0',
    description='A command-line tool to track and manage personal expenses.',
    author='Pedro Heringer',
    py_modules=['cli', 'expense_tracker'],
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'expense-tracker = cli:main',
        ],
    },
)

