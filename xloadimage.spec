Summary:	An X Window System based image viewer
Summary(pl):	Przegl±darka obrazków dla X Window
Name:		xloadimage
Version:	4.1
Release:	13
Copyright:	MIT
Group:		X11/Applications/Graphics
Group(pl):	X11/Grafika
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
Patch0:		xloadimage-linux.patch
Patch1:		xloadimage-nobr.patch
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
mv Makefile Makefile.orig
ln -s makefile.ansi Makefile

%build
xmkmf

(cd jpeg; make libjpeg.a CFLAGS="$RPM_OPT_FLAGS")

%{__make} CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults 

make	DESTDIR=$RPM_BUILD_ROOT \
	SYSPATHFILE=$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Xloadimage \
	install install.man

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/xloadimage.1x \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz xloadimagerc
%attr(755,root,root) %{_bindir}/xloadimage
%attr(755,root,root) %{_bindir}/xview
%attr(755,root,root) %{_bindir}/xsetbg

%{_libdir}/X11/app-defaults/Xloadimage
%{_mandir}/man1/xloadimage.1x.gz
