Summary: An X Window System based image viewer.
Name: xloadimage
Version: 4.1
Release: 12
Copyright: MIT
Group: Amusements/Graphics
Source: ftp.x.org:/R5contrib/xloadimage.4.1.tar.gz
Patch0: xloadimage.4.1-linux.patch
Patch1: xloadimage.4.1-nobr.patch
BuildRoot: /var/tmp/xloadimage-root

%description
The xloadimage utility displays images in an X Window System window,
loads images into the root window, or writes images into a file.
Xloadimage supports many images types (GIF, TIFF, JPEG, XPM, XBM, etc.).

Install the xloadimage package if you need a utility for displaying
images or loading images into the root window.

%prep
%setup -q -n xloadimage.4.1
%patch0 -p1
%patch1 -p1 -b .nobr

cd jpeg
mv Makefile Makefile.orig
ln -s makefile.ansi Makefile

%build
xmkmf
cd jpeg
make libjpeg.a
cd ..
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

make	DESTDIR=$RPM_BUILD_ROOT \
	SYSPATHFILE=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Xloadimage \
	install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/lib/X11/app-defaults/Xloadimage
/usr/X11R6/bin/xloadimage
/usr/X11R6/bin/xview
/usr/X11R6/bin/xsetbg
/usr/X11R6/man/man1/xloadimage.1x
