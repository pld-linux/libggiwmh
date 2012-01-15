#
# Conditional build:
%bcond_with	static_modules	# build static library AND make all modules builtin (also in shared lib)
#
Summary:	LibGGIWMH - Window Manager Hint extension
Summary(pl.UTF-8):	LibGGIWMH - rozszerzenie podpowiedzi dla zarządców okien
Name:		libggiwmh
Version:	0.3.2
Release:	1
License:	Public Domain
Group:		Libraries
# HTTP 403
#Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
Source0:	http://downloads.sourceforge.net/ggi/%{name}-%{version}.src.tar.bz2
# Source0-md5:	5f47aad2a8e224a09e90f3f0073c3c11
URL:		http://www.ggi-project.org/packages/libggiwmh.html
BuildRequires:	libggi-devel >= 2.2.2
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Requires:	libggi >= 2.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGIWMH is an extension for GGI targets that are window system based
to allow access to things like setting the title bar, resizing, etc..

%description -l pl.UTF-8
LibGGIWMH to rozszerzenie dla modułów wyświetlających GGI opartych na
zarządcach okien, mające na celu dostęp do możliwości takich jak
ustawianie belki tytułowej okienka, zmianę rozmiaru itp.

%package devel
Summary:	Header files for libggiwmh library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libggiwmh
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libggi-devel >= 2.2.2
%if %{with static_modules}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
%endif

%description devel
Header files for libggiwmh library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libggiwmh.

%package static
Summary:	Static libggiwmh library
Summary(pl.UTF-8):	Statyczna biblioteka libggiwmh
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libggiwmh library.

%description static -l pl.UTF-8
Statyczna biblioteka libggiwmh.

%package X
Summary:	X target for libggiwmh library
Summary(pl.UTF-8):	Wtyczka X dla biblioteki libggiwmh
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description X
X target for libggiwmh library.

%description X -l pl.UTF-8
Wtyczka X dla biblioteki libggiwmh.

%prep
%setup -q

%build
%configure \
	%{!?with_static_modules:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ggi/wmh/display/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libggiwmh.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggiwmh.so.0
%dir %{_libdir}/ggi/wmh
%dir %{_libdir}/ggi/wmh/display
%attr(755,root,root) %{_libdir}/ggi/wmh/display/pseudo_stubs_wmh.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/libggiwmh.conf
%{_mandir}/man7/libggiwmh.7*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libggiwmh.so
%{_libdir}/libggiwmh.la
%{_includedir}/ggi/wmh*.h
%{_includedir}/ggi/internal/wmh.h
%{_mandir}/man3/ggiWmh*.3*

%if %{with static_modules}
%files static
%defattr(644,root,root,755)
%{_libdir}/libggiwmh.a
%endif

%files X
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/wmh/display/X_wmh.so
