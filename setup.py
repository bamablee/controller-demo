#!/bin/env python
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
# 

import setuptools
import os

# Boost::Python infrastructure
bpy_incdir=['./env/include',]
bpy_libdir=['./env/lib',]
bpy_libs=['boost_python36',]

# assume we're running in a venv and need to set rpath
# for compiled extensions
rtl_dirs=[os.path.join( os.path.dirname( os.path.realpath(__file__) ), 'env', 'lib' ), ]

# compiled extension for fan interfaces
ext_files = [
    'src/extensions/tempcontrol_ext.cc',
    'src/extensions/fan.cc',
    'src/extensions/registers.cc',
]

ext = setuptools.extension.Extension(
    "_tempcontrol_ext",
    ext_files,
    library_dirs = bpy_libdir,
    include_dirs = bpy_incdir,
    libraries = bpy_libs,
    runtime_library_dirs = rtl_dirs,
    extra_compile_args = ['-std=c++11',],
    depends = []
)

# the main package
with open('README.md', 'r') as fh:
    longdesc = fh.read()
    
setuptools.setup( name="tempcontrol",
                  version='0.0.1',
                  author='Bryson Lee',
                  author_email='r.bryson.lee@gmail.com',
                  description='A conceptual temperature-control system',
                  long_description=longdesc,
                  long_description_content_type='text/markdown',
                  packages=setuptools.find_packages('src'),
                  package_dir={'': 'src'},
                  ext_modules=[ ext, ],
                  classifiers=[
                      'Programming Language :: Python :: 3',
                      'License :: OSI Approved :: MIT License',
                      'Operating System :: Linux',
                  ],
                  )


