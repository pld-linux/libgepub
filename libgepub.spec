#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library for epub documents
Summary(pl.UTF-8):	Biblioteka do obsługi dokumentów epub
Name:		libgepub
Version:	0.6.0
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgepub/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	77e3f2e3f57436d426eaf996675e44aa
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-webkit4-devel
BuildRequires:	libarchive-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.41.0
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
Obsoletes:	libgepub-static < 0.6.0

%description devel
Header files for libgepub library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgepub.

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libgepub-0.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgepub-0.6.so.0
%{_libdir}/girepository-1.0/Gepub-0.6.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgepub-0.6.so
%{_includedir}/libgepub-0.6
%{_pkgconfigdir}/libgepub-0.6.pc
%{_datadir}/gir-1.0/Gepub-0.6.gir
