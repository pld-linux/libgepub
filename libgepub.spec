#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library for epub documents
Summary(pl.UTF-8):	Biblioteka do obsługi dokumentów epub
Name:		libgepub
Version:	0.4
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgepub/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	431a1be6408825a6a7df5eb5f2362791
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-webkit4-devel
BuildRequires:	libarchive-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgepub is a GObject based library for handling and rendering epub
documents.

%description -l pl.UTF-8
libgepub to oparta na GObject biblioteka do obsługi i renderowania
dokumentów epub.

%package devel
Summary:	Header files for libgepub library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgepub
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	libarchive-devel
Requires:	libxml2-devel

%description devel
Header files for libgepub library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgepub.

%package static
Summary:	Static libgepub library
Summary(pl.UTF-8):	Statyczna biblioteka libgepub
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgepub library.

%description static -l pl.UTF-8
Statyczna biblioteka libgepub.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable static_libs static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libgepub.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgepub.so.0
%{_libdir}/girepository-1.0/Gepub-0.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgepub.so
%{_includedir}/libgepub
%{_pkgconfigdir}/libgepub.pc
%{_datadir}/gir-1.0/Gepub-0.4.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgepub.a
%endif
