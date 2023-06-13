#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library for epub documents
Summary(pl.UTF-8):	Biblioteka do obsługi dokumentów epub
Name:		libgepub
Version:	0.7.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libgepub/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	24fdda446dc6991e969c5bc46f965dcc
Patch0:		%{name}-gir.patch
URL:		https://gitlab.gnome.org/GNOME/libgepub
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-webkit4.1-devel
BuildRequires:	libarchive-devel
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
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
Requires:	libxml2-devel >= 2.0

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
%patch0 -p1

%build
%meson build

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
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_libdir}/libgepub-0.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgepub-0.7.so.0
%{_libdir}/girepository-1.0/Gepub-0.7.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgepub-0.7.so
%{_includedir}/libgepub-0.7
%{_pkgconfigdir}/libgepub-0.7.pc
%{_datadir}/gir-1.0/Gepub-0.7.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgepub-0.7.a
