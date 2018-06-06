Name: intel-opencl-clang
Version: 1.0
Release:	1%{?dist}
Summary:	Intel(R) OpenCL(TM) Clang

Group: System Environment/Libraries
License: MIT
URL: https://github.com/ArturHarasimiuk/opencl-clang
Source0: https://github.com/intel/opencl-clang/archive/master/opencl-clang-master.tar.gz
Source1: https://github.com/llvm-mirror/llvm/archive/release_40/llvm-40.tar.gz
Source2: https://github.com/llvm-mirror/clang/archive/release_40/clang-40.tar.gz

BuildRequires: cmake clang gcc-c++ ninja-build
# Requires:

%description


%prep
echo $RPM_BUILD_DIR
echo $RPM_SOURCE_DIR

# %setup -q


%build
echo "==== BUILD ===="
rm -rf *
tar xzf $RPM_SOURCE_DIR/opencl-clang-master.tar.gz
tar xzf $RPM_SOURCE_DIR/llvm-40.tar.gz
tar xzf $RPM_SOURCE_DIR/clang-40.tar.gz
mv llvm-release_40 llvm_source
mv clang-release_40 clang_source
mkdir build
cd build
cmake -G Ninja ../intel-opencl-clang-1.0 -DCMAKE_BUILD_TYPE=Release
cmake --build . --target cclang
find -name libopencl_clang.so
find -name libcommon_clang.so
nproc
free

%install
# %make_install
echo "==== INSTALL ===="
pwd


# %files
# %doc



# %changelog
echo "==== DONE ===="

