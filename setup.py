from distutils.core import setup
setup(
  name='babylex',
  packages=['babylex'],
  version='0.1',
  description='tiny library for working with amazon lex',
  author='Randall Hunt',
  author_email='randallhunt@gmail.com',
  url='https://github.com/ranman/babylex',
  download_url='https://github.com/ranman/babylex/tarball/0.1',
  keywords=['aws', 'chatbot'],
  classifiers=[],
  install_requires=["boto3"]
)
