Summary:	An X Window System based image viewer
Summary(pl):	Przegl±darka obrazków dla X Window
Name:		xloadimage
Version:	4.1
Release:	13
License:	MIT
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
Patch0:		%{name}-linux.patch
Patch1:		%{name}-nobr.patch
BuildRequires:	XFree86-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The xloadimage utility displays images in an X Window System window,
loads images into the root window, or writes images into a file.
Xloadimage supports many images types (GIF, TIFF, JPEG, XPM, XBM,
etc.).

%description -l pl
Xloadimage wy¶wietla obrazki w zwyk³ym i g³ównym oknie X Window lub
zapisuje je do pliku. Rozpoznaje wiele formatów plików graficznych,
m.in. GIF, TIFF, XPM, XBM, etc.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1

cd jpeg
mv -f Makefile Makefile.orig
ln -sf makefile.ansi Makefile

%build
xmkmf

(cd jpeg; %{__make} libjpeg.a CFLAGS="%{rpmcflags}")

%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	SYSPATHFILE=$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Xloadimage \
	install install.man

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz xloadimagerc
%attr(755,root,root) %{_bindir}/xloadimage
%attr(755,root,root) %{_bindir}/xview
%attr(755,root,root) %{_bindir}/xsetbg

%{_libdir}/X11/app-defaults/Xloadimage
%{_mandir}/man1/xloadimage.1x*
