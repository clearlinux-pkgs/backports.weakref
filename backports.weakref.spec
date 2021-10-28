#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : backports.weakref
Version  : 1.0.post1
Release  : 45
URL      : https://files.pythonhosted.org/packages/12/ab/cf35cf43a4a6215e3255cf2e49c77d5ba1e9c733af2aa3ec1ca9c4d02592/backports.weakref-1.0.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/ab/cf35cf43a4a6215e3255cf2e49c77d5ba1e9c733af2aa3ec1ca9c4d02592/backports.weakref-1.0.post1.tar.gz
Summary  : Backport of new features in Python's weakref module
Group    : Development/Tools
License  : Python-2.0
Requires: backports.weakref-license = %{version}-%{release}
Requires: backports.weakref-python = %{version}-%{release}
Requires: backports.weakref-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
backports.weakref
        =================
        
        This package provides backports of new features in Python's weakref_ module
        under the backports_ namespace.

%package license
Summary: license components for the backports.weakref package.
Group: Default

%description license
license components for the backports.weakref package.


%package python
Summary: python components for the backports.weakref package.
Group: Default
Requires: backports.weakref-python3 = %{version}-%{release}

%description python
python components for the backports.weakref package.


%package python3
Summary: python3 components for the backports.weakref package.
Group: Default
Requires: python3-core
Provides: pypi(backports.weakref)

%description python3
python3 components for the backports.weakref package.


%prep
%setup -q -n backports.weakref-1.0.post1
cd %{_builddir}/backports.weakref-1.0.post1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607995883
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/backports.weakref
cp %{_builddir}/backports.weakref-1.0.post1/LICENSE %{buildroot}/usr/share/package-licenses/backports.weakref/4dfc4478b1d5f7388b298fdfc06802485bdeae0c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/backports/__pycache__/__init__.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/backports/__init__.py

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/backports.weakref/4dfc4478b1d5f7388b298fdfc06802485bdeae0c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
