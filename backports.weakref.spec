#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : backports.weakref
Version  : 1.01
Release  : 2
URL      : https://pypi.python.org/packages/bc/cc/3cdb0a02e7e96f6c70bd971bc8a90b8463fda83e264fa9c5c1c98ceabd81/backports.weakref-1.0rc1.tar.gz
Source0  : https://pypi.python.org/packages/bc/cc/3cdb0a02e7e96f6c70bd971bc8a90b8463fda83e264fa9c5c1c98ceabd81/backports.weakref-1.0rc1.tar.gz
Summary  : Backport of new features in Python's weakref module
Group    : Development/Tools
License  : Python-2.0
Requires: backports.weakref-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
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

%description python
python components for the backports.weakref package.


%prep
%setup -q -n backports.weakref-1.0rc1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1497646657
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1497646657
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/backports/__init__.py
%exclude /usr/lib/python2.7/site-packages/backports/__init__.pyc
%exclude /usr/lib/python3.6/site-packages/backports/__init__.py
%exclude /usr/lib/python3.6/site-packages/backports/__pycache__/__init__.cpython-36.pyc
/usr/lib/python2*/*
/usr/lib/python3*/*
