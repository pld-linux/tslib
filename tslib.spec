Summary:	Abstraction layer for touchscreen panel event
Summary(pl.UTF-8):	Warstwa abstrakcji dla zdarzeń pochodzących z paneli dotykowych
Name:		tslib
Version:	1.14
Release:	1
License:	LGPL v2
Group:		Libraries
#Source0Download: https://github.com/kergoth/tslib/releases
Source0:	https://github.com/kergoth/tslib/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	8f1417989a1d9b97c687bddc35a33e73
URL:		http://www.tslib.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%description -l pl.UTF-8
tslib to warstwa abstrakcji dla zdarzeń pochodzących z paneli
dotykowych, a także stos filtrów do przetwarzania tych zdarzeń.
Została stworzona przez Russela Kinga z projektu arm.linux.org.uk.
Przykładowe zaimplementowane filtry obejmują wygładzanie drgań i
kalibrację.

tslib jest często używana w urządzeniach wbudowanych w celu
zapewnienia wspólnego interfejsu przestrzeni użytkownika dla
ekranów dotykowych. Jest obsługiwana przez Kdrive (TinyX) i OPIE, a
także przez wiele komercyjnych urządzeń linuksowych, w tym Nokię 770.

%package devel
Summary:	Header files for tslib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tslib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tslib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tslib.

%package static
Summary:	Static tslib library
Summary(pl.UTF-8):	Statyczna biblioteka tslib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tslib library.

%description static -l pl.UTF-8
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
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ts/*.{la,a}
# obsoleted by pkg-config, but keep for now for other existing *.la
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/libts.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ts_calibrate
%attr(755,root,root) %{_bindir}/ts_finddev
%attr(755,root,root) %{_bindir}/ts_harvest
%attr(755,root,root) %{_bindir}/ts_print
%attr(755,root,root) %{_bindir}/ts_print_mt
%attr(755,root,root) %{_bindir}/ts_print_raw
%attr(755,root,root) %{_bindir}/ts_test
%attr(755,root,root) %{_bindir}/ts_test_mt
%attr(755,root,root) %{_bindir}/ts_uinput
%attr(755,root,root) %{_bindir}/ts_verify
%attr(755,root,root) %{_libdir}/libts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libts.so.0
%dir %{_libdir}/ts
%attr(755,root,root) %{_libdir}/ts/*.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ts.conf
%{_mandir}/man1/ts_calibrate.1*
%{_mandir}/man1/ts_finddev.1*
%{_mandir}/man1/ts_harvest.1*
%{_mandir}/man1/ts_print.1*
%{_mandir}/man1/ts_print_mt.1*
%{_mandir}/man1/ts_print_raw.1*
%{_mandir}/man1/ts_test.1*
%{_mandir}/man1/ts_test_mt.1*
%{_mandir}/man1/ts_uinput.1*
%{_mandir}/man1/ts_verify.1*
%{_mandir}/man5/ts.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libts.so
%{_libdir}/libts.la
%{_includedir}/tslib.h
%{_pkgconfigdir}/tslib.pc
%{_mandir}/man3/ts_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libts.a
