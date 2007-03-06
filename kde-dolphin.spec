%define 	_name dolphin

Summary:	File manager for KDE
Summary(pl.UTF-8):	Manager plików dla KDE
Name:		kde-%{_name}
Version:	0.8.2
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://enzosworld.gmxhome.de/download/%{_name}-%{version}.tar.gz
# Source0-md5:	376f7a1deca0f4d69fa96a393cea464b
URL:		http://enzosworld.gmxhome.de/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dolphin is a file manager for KDE focusing on usability. The main
features of Dolphin are:
     - Navigation bar for URLs, which allows to navigate quickly through 
        the file hierarchy.
     - View properties are remembered for each folder.
     - Split of views is supported.
     - Network transparency.
     - Undo/redo functionality.
     - Renaming of a variable number of selected items in one step.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dolphin
%{_datadir}/apps/dolphin
%{_desktopdir}/kde/dolphin.desktop
%{_iconsdir}/hicolor/*/apps/*.png
