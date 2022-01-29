#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hyperscan
Version  : 5.3.0
Release  : 18
URL      : https://github.com/intel/hyperscan/archive/v5.3.0/hyperscan-5.3.0.tar.gz
Source0  : https://github.com/intel/hyperscan/archive/v5.3.0/hyperscan-5.3.0.tar.gz
Summary  : Intel(R) Hyperscan Library
Group    : Development/Tools
License  : BSD-3-Clause Intel
Requires: hyperscan-lib = %{version}-%{release}
Requires: hyperscan-license = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : ragel
BuildRequires : util-linux

%description
# Hyperscan
Hyperscan is a high-performance multiple regex matching library. It follows the
regular expression syntax of the commonly-used libpcre library, but is a
standalone library with its own C API.

%package dev
Summary: dev components for the hyperscan package.
Group: Development
Requires: hyperscan-lib = %{version}-%{release}
Provides: hyperscan-devel = %{version}-%{release}
Requires: hyperscan = %{version}-%{release}

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
Requires: hyperscan-license = %{version}-%{release}

%description lib
lib components for the hyperscan package.


%package license
Summary: license components for the hyperscan package.
Group: Default

%description license
license components for the hyperscan package.


%prep
%setup -q -n hyperscan-5.3.0
cd %{_builddir}/hyperscan-5.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590516447
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fno-lto -march=haswell "
export FCFLAGS="$FFLAGS -O3 -fno-lto -march=haswell "
export FFLAGS="$FFLAGS -O3 -fno-lto -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fno-lto -march=skylake-avx512 "
export FCFLAGS="$FFLAGS -O3 -fno-lto -march=skylake-avx512 "
export FFLAGS="$FFLAGS -O3 -fno-lto -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
export FFLAGS="$FFLAGS -march=skylake-avx512 -m64 "
export FCFLAGS="$FCFLAGS -march=skylake-avx512 -m64 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1590516447
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hyperscan
cp %{_builddir}/hyperscan-5.3.0/COPYING %{buildroot}/usr/share/package-licenses/hyperscan/460136879250bc39dbc8be7799af9c079527808f
cp %{_builddir}/hyperscan-5.3.0/LICENSE %{buildroot}/usr/share/package-licenses/hyperscan/e9e53a0b2358d3fd707a717d971d01ef87bffd0e
pushd clr-build-avx512
%make_install_avx512  || :
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
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
/usr/lib64/haswell/avx512_1/libhs.so
/usr/lib64/haswell/libhs.so
/usr/lib64/haswell/libhs_runtime.so
/usr/lib64/libhs.so
/usr/lib64/libhs_runtime.so
/usr/lib64/pkgconfig/libhs.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/hyperscan/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libhs.so.5
/usr/lib64/haswell/avx512_1/libhs.so.5.3.0
/usr/lib64/haswell/libhs.so.5
/usr/lib64/haswell/libhs.so.5.3.0
/usr/lib64/haswell/libhs_runtime.so.5
/usr/lib64/haswell/libhs_runtime.so.5.3.0
/usr/lib64/libhs.so.5
/usr/lib64/libhs.so.5.3.0
/usr/lib64/libhs_runtime.so.5
/usr/lib64/libhs_runtime.so.5.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hyperscan/460136879250bc39dbc8be7799af9c079527808f
/usr/share/package-licenses/hyperscan/e9e53a0b2358d3fd707a717d971d01ef87bffd0e
