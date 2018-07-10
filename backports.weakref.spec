#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : backports.weakref
Version  : 1.0rc1
Release  : 21
URL      : http://pypi.debian.net/backports.weakref/backports.weakref-1.0rc1.tar.gz
Source0  : http://pypi.debian.net/backports.weakref/backports.weakref-1.0rc1.tar.gz
Summary  : Backport of new features in Python's weakref module
Group    : Development/Tools
License  : Python-2.0
Requires: backports.weakref-python3
Requires: backports.weakref-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
=================
backports.weakref
=================
This package provides backports of new features in Python's weakref_ module
under the backports_ namespace.

%package python
Summary: python components for the backports.weakref package.
Group: Default
Requires: backports.weakref-python3

%description python
python components for the backports.weakref package.


%package python3
Summary: python3 components for the backports.weakref package.
Group: Default
Requires: python3-core

%description python3
python3 components for the backports.weakref package.


%prep
%setup -q -n backports.weakref-1.0rc1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530329790
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.7/site-packages/backports/__init__.py
%exclude /usr/lib/python3.7/site-packages/backports/__pycache__/__init__.cpython-37.pyc
/usr/lib/python3*/*
