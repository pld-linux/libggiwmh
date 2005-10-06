Summary:	LibGGIWMH - Window Manager Hint extension
Summary(pl):	LibGGIWMH - rozszerzenie podpowiedzi dla zarz±dców okien
Name:		libggiwmh
Version:	0.2.2
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
# Source0-md5:	42f51c7496508f17d524ea1f9b10a0e0
URL:		http://www.ggi-project.org/packages/libggiwmh.html
BuildRequires:	XFree86-devel
BuildRequires:	libggi-devel >= 2.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGIWMH is an extension for GGI targets that are window system based
to allow access to things like setting the title bar, resizing, etc..

%description -l pl
LibGGIWMH to rozszerzenie dla modu³ów wy¶wietlaj±cych GGI opartych na
zarz±dcach okien, maj±ce na celu dostêp do mo¿liwo¶ci takich jak
ustawianie belki tytu³owej okienka, zmianê rozmiaru itp.

%package devel
Summary:	Header files for libggiwmh library
Summary(pl):	Pliki nag³ówkowe biblioteki libggiwmh
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libggi-devel >= 2.1.2

%description devel
Header files for libggiwmh library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libggiwmh.

%package X
Summary:	X target for libggiwmh library
Summary(pl):	Wtyczka X dla biblioteki libggiwmh
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description X
X target for libggiwmh library.

%description X -l pl
Wtyczka X dla biblioteki libggiwmh.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ggi/wmh/display/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libggiwmh.so.*.*.*
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

%files X
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggi/wmh/display/X_wmh.so
