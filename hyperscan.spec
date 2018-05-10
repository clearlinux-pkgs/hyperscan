#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hyperscan
Version  : 4.7.0
Release  : 3
URL      : https://github.com/intel/hyperscan/archive/v4.7.0.tar.gz
Source0  : https://github.com/intel/hyperscan/archive/v4.7.0.tar.gz
Summary  : Intel(R) Hyperscan Library
Group    : Development/Tools
License  : BSD-3-Clause Intel
Requires: hyperscan-lib
Requires: hyperscan-doc
BuildRequires : Sphinx
BuildRequires : boost-dev
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : python3-dev
BuildRequires : ragel
BuildRequires : sqlite-autoconf-dev

%description
# Hyperscan
Hyperscan is a high-performance multiple regex matching library. It follows the
regular expression syntax of the commonly-used libpcre library, but is a
standalone library with its own C API.

%package dev
Summary: dev components for the hyperscan package.
Group: Development
Requires: hyperscan-lib
Provides: hyperscan-devel

%description dev
dev components for the hyperscan package.


%package doc
Summary: doc components for the hyperscan package.
Group: Documentation

%description doc
doc components for the hyperscan package.


%package lib
Summary: lib components for the hyperscan package.
Group: Libraries

%description lib
lib components for the hyperscan package.


%prep
%setup -q -n hyperscan-4.7.0
pushd ..
cp -a hyperscan-4.7.0 buildavx2
popd
pushd ..
cp -a hyperscan-4.7.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522180736
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}
popd
mkdir clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -march=haswell "
export FCFLAGS="$CFLAGS -O3 -march=haswell "
export FFLAGS="$CFLAGS -O3 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell"
export CXXFLAGS="$CXXFLAGS -march=haswell"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib/haswell -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}  || :
popd
mkdir clr-build-avx512
pushd clr-build-avx512
export CFLAGS="$CFLAGS -O3 -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512"
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib/haswell/avx512_1 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}  || :
popd

%install
export SOURCE_DATE_EPOCH=1522180736
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/haswell/avx512_1
pushd clr-build-avx2
%make_install  || :
mv %{buildroot}/usr/lib64/*so* %{buildroot}/usr/lib64/haswell/ || :
popd
rm -f %{buildroot}/usr/bin/*
mkdir -p %{buildroot}/usr/lib64/haswell/avx512_1
pushd clr-build-avx512
%make_install  || :
mv %{buildroot}/usr/lib64/*so* %{buildroot}/usr/lib64/haswell/avx512_1 || :
popd
rm -f %{buildroot}/usr/bin/*
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/hs/hs.h
/usr/include/hs/hs_common.h
/usr/include/hs/hs_compile.h
/usr/include/hs/hs_runtime.h
/usr/lib64/haswell/libhs.so
/usr/lib64/haswell/libhs_runtime.so
/usr/lib64/libhs.so
/usr/lib64/libhs_runtime.so
/usr/lib64/pkgconfig/libhs.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/hyperscan/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libhs.so
/usr/lib64/haswell/avx512_1/libhs.so.4
/usr/lib64/haswell/avx512_1/libhs.so.4.7.0
/usr/lib64/haswell/avx512_1/libhs_runtime.so
/usr/lib64/haswell/avx512_1/libhs_runtime.so.4
/usr/lib64/haswell/avx512_1/libhs_runtime.so.4.7.0
/usr/lib64/haswell/libhs.so.4
/usr/lib64/haswell/libhs.so.4.7.0
/usr/lib64/haswell/libhs_runtime.so.4
/usr/lib64/haswell/libhs_runtime.so.4.7.0
/usr/lib64/libhs.so.4
/usr/lib64/libhs.so.4.7.0
/usr/lib64/libhs_runtime.so.4
/usr/lib64/libhs_runtime.so.4.7.0
