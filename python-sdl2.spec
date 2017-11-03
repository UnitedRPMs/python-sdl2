%define module sdl2
%define oname PySDL2

Name:           python-%{module}
Version:        0.9.6
Release:        1%{dist}
Summary:        Python 2.x SDL2 bindings
License:        Public Domain or CC0
Group:          Development/Python
URL:            https://bitbucket.org/marcusva/py-sdl2
Source0:        https://github.com/marcusva/py-sdl2/archive/rel_0_9_6.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
Provides:	python-pysdl

%description
PySDL2 is a wrapper around the SDL2 library and as such similar to the
discontinued PySDL project. In contrast to PySDL, it has no licensing
restrictions, nor does it rely on C code, but uses ctypes instead.

%package -n python3-%{module}
Summary:        Python 3.x SDL2 bindings
Group:          Development/Python

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-devel
Provides:	python3-pysdl

%description -n python3-%{module}
PySDL2 is a wrapper around the SDL2 library and as such similar to the
discontinued PySDL project. In contrast to PySDL, it has no licensing
restrictions, nor does it rely on C code, but uses ctypes instead.

%prep
%autosetup -n py-sdl2-rel_0_9_6

cp -a . %{py3dir}

%build
%py2_build

pushd %{py3dir}
%py3_build
popd

%install
%py2_install

pushd %{py3dir}
%py3_install
popd

%files
%doc README.txt doc/html/*.html
%license doc/copying.rst
%{python2_sitelib}/%{oname}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{module}/

%files -n python3-%{module}
%doc README.txt doc/html/*.html
%license doc/copying.rst
%{python3_sitelib}/%{oname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{module}/


%changelog

* Thu Nov 02 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.9.6-1
- Updated to 0.9.6

* Sat Sep 02 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.9.5-3
- Upstream
- Changed source code url
- Added provides for compatibility

* Sat Aug 05 2017 pterjan <pterjan> 0.9.5-2.mga7
+ Revision: 1135623
- Rebuild for python 3.6

* Sat Jan 21 2017 akien <akien> 0.9.5-1.mga6
+ Revision: 1082553
- imported package python-sdl2

