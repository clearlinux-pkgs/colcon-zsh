#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-zsh
Version  : 0.4.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/c9/57/5170e32f0caab9078d43011b057c1a2a5452e6ccb41920dbfaadaabc46f3/colcon-zsh-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/57/5170e32f0caab9078d43011b057c1a2a5452e6ccb41920dbfaadaabc46f3/colcon-zsh-0.4.0.tar.gz
Summary  : Extension for colcon to provide Z shell scripts.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-zsh-python = %{version}-%{release}
Requires: colcon-zsh-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
colcon-zsh
==========

An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to provide `Z shell <http://www.zsh.org>`_ scripts.

%package python
Summary: python components for the colcon-zsh package.
Group: Default
Requires: colcon-zsh-python3 = %{version}-%{release}

%description python
python components for the colcon-zsh package.


%package python3
Summary: python3 components for the colcon-zsh package.
Group: Default
Requires: python3-core
Provides: pypi(colcon-zsh)

%description python3
python3 components for the colcon-zsh package.


%prep
%setup -q -n colcon-zsh-0.4.0
cd %{_builddir}/colcon-zsh-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582911388
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
