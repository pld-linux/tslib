Summary:	Abstraction layer for touchscreen panel event
Summary(pl):	Warstwa abstrakcji dla zdarzeñ pochodz±cych z paneli dotykowych
Name:		tslib
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.berlios.de/tslib/%{name}-%{version}.tar.bz2
# Source0-md5:	92b2eb55b1e4ef7e2c0347069389390e
URL:		http://tslib.berlios.de/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tslib is an abstraction layer for touchscreen panel events, as well as
a filter stack for the manipulation of those events. It was created by
Russell King, of arm.linux.org.uk. Examples of implemented filters
include jitter smoothing and the calibration transform.

tslib is generally used on embedded devices to provide a common user
space interface to touchscreen functionality. It is supported by
Kdrive (aka TinyX) and OPIE as well as being used on a number of
commercial Linux devices including the Nokia 770.

%description -l pl
tslib to warstwa abstrakcji dla zdarzeñ pochodz±cych z paneli
dotykowych, a tak¿e stos filtrów do przetwarzania tych zdarzeñ.
Zosta³a stworzona przez Russela Kinga z projektu arm.linux.org.uk.
Przyk³adowe zaimplementowane filtry obejmuj± wyg³adzanie drgañ i
kalibracjê.

tslib jest czêsto u¿ywana w urz±dzeniach wbudowanych w celu
zapewnienia wspólnego interfejsu przestrzeni u¿ytkownika dla
ekranów dotykowych. Jest obs³ugiwana przez Kdrive (TinyX) i OPIE, a
tak¿e przez wiele komercyjnych urz±dzeñ linuksowych, w tym Nokiê 770.

%package devel
Summary:	Header files for tslib library
Summary(pl):	Pliki nag³ówkowe biblioteki tslib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tslib library.

%description devel -l pl
Pliki nag³ówkowe biblioteki tslib.

%package static
Summary:	Static tslib library
Summary(pl):	Statyczna biblioteka tslib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tslib library.

%description static -l pl
Statyczna biblioteka tslib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4/internal
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ts/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ts_*
%attr(755,root,root) %{_libdir}/libts-*.so.*.*.*
%dir %{_libdir}/ts
%attr(755,root,root) %{_libdir}/ts/*.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ts.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libts.so
%{_libdir}/libts.la
%{_includedir}/tslib.h
%{_pkgconfigdir}/tslib-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libts.a
