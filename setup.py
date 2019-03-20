from setuptools import setup, find_packages, Extension

setup(name='bbo_benchmarks',
      version='1.0',
      description='Black-Box Optimization Benchmarks',
      author='Computational Intelligence Laboratory, Peking University',
      author_email='liyfieng0039@gmail.com',
      license='Apache 2.0',
      packages=['bbo_benchmarks', 'bbo_benchmarks/cec2013', 'bbo_benchmarks/cec2017'],
      #packages=find_packages(),
      ext_modules = [Extension('_cec13',
                               sources=['bbo_benchmarks/cec2013/cec13.i', 'bbo_benchmarks/cec2013/cec13.c'],
                               swig_opts=['-modern', '-I../include']),
                     Extension('_cec17',
                                sources=['bbo_benchmarks/cec2017/cec17.i', 'bbo_benchmarks/cec2017/cec17.c'],
                                swig_opts=['-modern', '-I../include'])],
     )

import zipfile, os

input_data_13_dir = 'bbo_benchmarks/cec2013/input_data.zip'
input_data_17_dir = 'bbo_benchmarks/cec2017/input_data.zip'

data_dir = os.path.expanduser('~/.bbo_benchmark')
if not os.path.exists(data_dir):
    print('creating dir ~/.bbo_benchmark')
    os.makedirs(data_dir)
else:
    print('~/.bbo_benchmark already exists')

if not os.path.exists(os.path.join(data_dir, 'cec2013')):
    print('extracting cec2013 input data')
    with zipfile.ZipFile(input_data_13_dir) as zf:
        os.makedirs('cec2013')
        zf.extractall(os.path.join(data_dir, 'cec2013'))

if not os.path.exists(os.path.join(data_dir, 'cec2017')):
    print('extracting cec2013 input data')
    with zipfile.ZipFile(input_data_17_dir) as zf:
        os.makedirs('cec2017')
        zf.extractall(os.path.join(data_dir, 'cec2017'))
