import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
    name='soapify',  
    version='1.0.0',
    scripts=['bin/soapify'] ,
    author="tncga",
    author_email="qokberk_akdeniz@hotmail.com",
    description="search on your all spotify playlists",
    long_description=readme(),
    url="https://github.com/tncga/soap",
    packages=["soapify"],
    install_requires=["click", "spotipy"],
    license="MIT",
    keywords="spotify search playlist cli"
 )