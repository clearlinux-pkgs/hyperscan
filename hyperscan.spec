#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : hyperscan
Version  : 5.4.2
Release  : 31
URL      : https://github.com/intel/hyperscan/archive/v5.4.2/hyperscan-5.4.2.tar.gz
Source0  : https://github.com/intel/hyperscan/archive/v5.4.2/hyperscan-5.4.2.tar.gz
Summary  : Intel(R) Hyperscan Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: hyperscan-lib = %{version}-%{release}
Requires: hyperscan-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pypi(sphinx)
BuildRequires : pypi-sphinx
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
%setup -q -n hyperscan-5.4.2
cd %{_builddir}/hyperscan-5.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702320594
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DBUILD_AVX512=ON \
-DBUILD_SHARED_LIBS=ON \
-DBUILD_AVX512VBMI=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DBUILD_AVX512=ON \
-DBUILD_SHARED_LIBS=ON \
-DBUILD_AVX512VBMI=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -m64 "
%cmake .. -DBUILD_AVX512=ON \
-DBUILD_SHARED_LIBS=ON \
-DBUILD_AVX512VBMI=ON
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702320594
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hyperscan
cp %{_builddir}/hyperscan-%{version}/COPYING %{buildroot}/usr/share/package-licenses/hyperscan/460136879250bc39dbc8be7799af9c079527808f || :
cp %{_builddir}/hyperscan-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/hyperscan/e9e53a0b2358d3fd707a717d971d01ef87bffd0e || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/hs/hs.h
/usr/include/hs/hs_common.h
/usr/include/hs/hs_compile.h
/usr/include/hs/hs_runtime.h
/usr/lib64/libhs.so
/usr/lib64/libhs_runtime.so
/usr/lib64/pkgconfig/libhs.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/hyperscan/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libhs.so.5.4.2
/V3/usr/lib64/libhs_runtime.so.5.4.2
/V4/usr/lib64/libhs.so.5.4.2
/V4/usr/lib64/libhs_runtime.so.5.4.2
/usr/lib64/libhs.so.5
/usr/lib64/libhs.so.5.4.2
/usr/lib64/libhs_runtime.so.5
/usr/lib64/libhs_runtime.so.5.4.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hyperscan/460136879250bc39dbc8be7799af9c079527808f
/usr/share/package-licenses/hyperscan/e9e53a0b2358d3fd707a717d971d01ef87bffd0e
