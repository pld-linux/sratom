Summary:	Library for serializing LV2 atoms to/from RDF
Summary(pl.UTF-8):	Biblioteka do serializacji obiektów LV2 do/z RDF
Name:		sratom
Version:	0.4.2
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	5bb7e4bc4198e19f388ac51239007f25
URL:		http://drobilla.net/software/sratom/
# urid+atom extensions
BuildRequires:	lv2-devel >= 1.0.0
BuildRequires:	python
BuildRequires:	serd-devel >= 0.14.0
BuildRequires:	sord-devel >= 0.12.0
Requires:	lv2 >= 1.0.0
Requires:	serd >= 0.14.0
Requires:	sord >= 0.12.0
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
Requires:	lv2-devel >= 1.0.0
Requires:	serd-devel >= 0.14.0
Requires:	sord-devel >= 0.12.0

%description devel
Header files for sratom library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sratom.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

# let rpm autogenerate dependencies
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libsratom-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsratom-0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsratom-0.so
%{_includedir}/sratom-0
%{_pkgconfigdir}/sratom-0.pc
