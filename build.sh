mkdir dependencies

git clone https://github.com/awslabs/handwritten-text-recognition-for-apache-mxnet
cd ..
git clone https://github.com/usnistgov/SCTK
cd SCTK
export CXXFLAGS="-std=c++11" && make config
make all
make check
make install
make doc
cd handwritten-text-recognition-for-apache-mxnet

pip3 install pybind11 numpy setuptools
cd ..
git clone https://github.com/nmslib/hnswlib
cd hnswlib/python_bindings
python3 setup.py install
cd ../..
