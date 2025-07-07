from setuptools import setup, find_packages

setup(
    name='ipl_score_predictor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'scikit-learn',
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'ipl-score-predictor=app:main',
        ],
    },
)