#
# Conditional build:
%bcond_with	apidocs	# API documentation

Summary:	Library for serializing LV2 atoms to/from RDF
Summary(pl.UTF-8):	Biblioteka do serializacji obiektów LV2 do/z RDF
Name:		sratom
Version:	0.6.14
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	e229f08f841e5d8b5d967e63e0626fc4
URL:		http://drobilla.net/software/sratom/
# urid+atom extensions
BuildRequires:	lv2-devel >= 1.18.3
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	serd-devel >= 0.30.9
BuildRequires:	sord-devel >= 0.16.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	sphinx-pdg >= 2
%endif
Requires:	lv2 >= 1.18.3
Requires:	serd >= 0.30.9
Requires:	sord >= 0.16.9
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
Requires:	lv2-devel >= 1.18.3
Requires:	serd-devel >= 0.30.9
Requires:	sord-devel >= 0.16.9

%description devel
Header files for sratom library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sratom.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	%{!?with_apidocs:-Ddocs=disabled}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
