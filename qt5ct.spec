%define		qtver	5.15.0
Summary:	Qt5 Configuration Tool
Name:		qt5ct
Version:	1.7
Release:	1
License:	BSD
Group:		Applications
Source0:	https://downloads.sourceforge.net/qt5ct/%{name}-%{version}.tar.bz2
# Source0-md5:	cd06d8583e5ab9538fe32f62fb979a1f
URL:		https://sourceforge.net/projects/qt5ct/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5ThemeSupport-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.11.0
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	qt5-qttools >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 2.016
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qt5ct allows users to configure Qt5 settings (theme, font, icons,
etc.) under DE/WM without Qt integration.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
cp -p src/qt5ct/translations/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/qt5ct
%attr(755,root,root) %{_libdir}/libqt5ct-common.so.%{version}
%attr(755,root,root) %{_libdir}/qt5/plugins/platformthemes/libqt5ct.so
%attr(755,root,root) %{_libdir}/qt5/plugins/styles/libqt5ct-style.so
%dir %{_datadir}/qt5ct
%{_datadir}/qt5ct/colors
%{_datadir}/qt5ct/qss
%{_desktopdir}/qt5ct.desktop
%dir %{_datadir}/qt5ct/translations
