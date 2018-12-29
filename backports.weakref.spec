#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : backports.weakref
Version  : 1.0.post1
Release  : 23
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

%description python3
python3 components for the backports.weakref package.


%prep
%setup -q -n backports.weakref-1.0.post1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542158931
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/backports.weakref
cp LICENSE %{buildroot}/usr/share/package-licenses/backports.weakref/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/backports.weakref/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.7/site-packages/backports/__init__.py
%exclude /usr/lib/python3.7/site-packages/backports/__pycache__/__init__.cpython-37.pyc
/usr/lib/python3*/*
