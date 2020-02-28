import setuptools

setuptools.setup(
    name="titleweektrend-sean-gao",
    version="0.0.1",
    author="Sean Gao",
    author_email="seangaoxy@gmail.com",
    description="You can use it to get the sum of Google Trends for each word in a news or video title over the past week.",
    long_description=open('README.md').read(),
    url="https://github.com/xga0/titleWeekTrend",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)