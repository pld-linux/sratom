#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	Library for serializing LV2 atoms to/from RDF
Summary(pl.UTF-8):	Biblioteka do serializacji obiektów LV2 do/z RDF
Name:		sratom
Version:	0.6.18
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	7f0411550c69ab009365517186f4b103
URL:		http://drobilla.net/software/sratom/
# urid+atom extensions
BuildRequires:	lv2-devel >= 1.18.4
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	serd-devel >= 0.30.10
BuildRequires:	sord-devel >= 0.16.16
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-sphinx_lv2_theme
BuildRequires:	sphinx-pdg >= 2
BuildRequires:	sphinxygen
%endif
Requires:	lv2 >= 1.18.4
Requires:	serd >= 0.30.10
Requires:	sord >= 0.16.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sratom is a library for serialising LV2 atoms to/from RDF,
particularly the Turtle syntax.

%description -l pl.UTF-8
Sratom to biblioteka do serializacji obiektów LV2 do/z RDF, w
szczególności składni Turtle.

%package devel
Summary:	Header files for sratom library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sratom
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2-devel >= 1.18.4
Requires:	serd-devel >= 0.30.10
Requires:	sord-devel >= 0.16.16

%description devel
Header files for sratom library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sratom.

%package apidocs
Summary:	API documentation for sratom library
Summary(pl.UTF-8):	Dokumentacja API biblioteki sratom
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for sratom library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki sratom.

%prep
%setup -q

%build
%meson \
	--default-library=shared \
	%{!?with_apidocs:-Ddocs=disabled} \
	-Dsinglehtml=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%attr(755,root,root) %{_libdir}/libsratom-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsratom-0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsratom-0.so
%{_includedir}/sratom-0
%{_pkgconfigdir}/sratom-0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/sratom-0
%{_docdir}/sratom-0/html
%endif
