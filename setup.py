from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='Detect',
        version='0.0.7',
        description='Anomaly detection framework for Tractometry',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/chamberm/Detect',
        author='Maxime Chamberland',
        author_email='m.chamberland@tue.nl',
        python_requires='>=3.7',
        license='Apache 2.0',
        packages=find_packages(),
        install_requires=[
            'future',
            'numpy==1.19.2',
            'nibabel>=2.3.0',
            'matplotlib>=2.0',
            'scikit-learn==0.22',
            'scipy>=0.19',
            'dipy>=1.0.0',
            'streamlit>=0.57.2',
            'pandas==1.0.0',
            'xlrd==1.2.0',
            'seaborn==0.9.0',
            'tensorflow==2.4.1',
            'keras==2.4.3',
            'openpyxl'
        ],
        zip_safe=False,
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Operating System :: Unix',
            'Operating System :: MacOS'
        ],
        scripts=[
            'bin/Detect', 'bin/Inspect'
        ],
    )
