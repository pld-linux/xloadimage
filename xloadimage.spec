Summary:	An X Window System based image viewer
Summary(cs):	Prohlí¾eè obrázkù na pro X Window System
Summary(da):	Billledvisningsprogram for X vinduesystemet
Summary(de):	Ein Bild-Anzeiger für das X Window System
Summary(es):	Visor de imágenes para X Window
Summary(fr):	Programme d'affichage d'images basé sur le système X Window
Summary(id):	Utility X Window System untuk melihat gambar
Summary(is):	Myndbirtir fyrir X gluggakerfiğ
Summary(it):	Visualizzatore di immagini per X Window
Summary(ja):	X Window System ¥Ù¡¼¥¹¤Î²èÁü¥Ó¥å¡¼¥¢
Summary(ko):	X À©µµ¿ì ½Ã½ºÅÛ ±â¹İ ÀÌ¹ÌÁö º¸±â ÇÁ·Î±×·¥
Summary(no):	Bildevisningsprogram for X vindusystemet
Summary(pl):	Przegl±darka obrazków dla X Window
Summary(pt):	Um visualizador de imagens baseado em X Window System
Summary(ru):	ğÒÏÇÒÁÍÍÁ ĞÒÏÓÍÏÔÒÁ ÉÚÏÂÒÁÖÅÎÉÊ × X Window System
Summary(sk):	Prehliadaè obrázkov pre systém X Window
Summary(sl):	Pregledovalnik slik za Okna X
Summary(sv):	En bildvisare för X11
Summary(uk):	ğÒÏÇÒÁÍÁ ĞÅÒÅÇÌÑÄÕ ÚÏÂÒÁÖÅÎØ Ğ¦Ä X Window System
Summary(zh_CN):	Ò»¸ö»ùÓÚ X ´°¿ÚÏµÍ³µÄÍ¼Ïñ²é¿´Æ÷¡£
Name:		xloadimage
Version:	4.1
Release:	27
License:	MIT
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
# Source0-md5: 7331850fc04056ab8ae6b5725d1fb3d2
Patch0:		%{name}-linux.patch
Patch1:		%{name}-nobr.patch
Patch2:		%{name}-unaligned.patch
Patch3:		%{name}-buffer.patch
Patch4:		%{name}-errno.patch
Patch5:		%{name}-varargs2stdarg.patch
BuildRequires:	XFree86-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix			/usr/X11R6
%define		_mandir			%{_prefix}/man
%define		_appdefsdir		/usr/X11R6/lib/X11/app-defaults
%define		_noautocompressdoc	*rc

%description
The xloadimage utility displays images in an X Window System window,
loads images into the root window, or writes images into a file.
Xloadimage supports many images types (GIF, TIFF, JPEG, XPM, XBM,
etc.).

%description -l cs
Xloadimage zobrazuje obrázky v X Window Systemu, umis»uje obrázky do
koøenového okna nebo ukládá obrázky do souboru. Podporuje mno¾ství
formátù (GIF, TIFF, JPEG, XPM, XBM, atd.).

%description -l da
Xloadimage er et værktøj som viser billeder i et X-vindue, indlæser
billeder i rodvinduet, eller skriver billeder på en fil.  Xloadimage
behandler mange billedtyper (GIF, TIFF, JPEG, XPM, XBM, etc.).

%description -l de
Das Dienstprogramm xloadimage zeigt Bilder in einem X Window
System-Fenster an, lädt Bilder in das Root-Fenster oder schreibt
Bilder in eine Datei. Xloadimage unterstützt viele Bildformate (GIF,
TIFF, JPEG, XPM, XBM usw.).

%description -l es
La utilidad xloadimage muestra imágenes en una ventana de X Window,
carga imágenes en la ventana de fondo o las escribe en un fichero.
Xloadimage soporta múltiples formatos de imagen(GIF, TIFF, JPEG. XPM,
XBM, etc.).

%description -l fr
L'utilitaire xloadimage affiche des images dans une fenêtre du système X
Window, charge des images dans la fenêtre root ou écrit des images dans
un fichier. Xloadimage prend en charge de nombreux types d'image (GIF,
TIFF, JPEG, XPM et XBM).

%description -l id
Utility xloadimage menampilkan gambar di sebuah window pada X Window
System, di root window, atau menyimpan gambar ke dalam file. Xloadimage
menukung banyak type gambar (GIF, TIFF, JPEG, XPM, XBM, dll.).

%description -l is
Xloadimage forritiğ birtir myndir í glugga X gluggakerfis, hleğur
myndir í rótargluggann, eğa skrifar myndir í skrá. Xloadimage styğur
margar tegundir mynda (GIF, TIFF, JPEG, XPM, XBM, o.fl.).

%description -l it
Il programma xloadimage visualizza un'immagine in una finestra del
sistema X Window, carica le immagini nella finestra di root o salva
le immagini in un file. Xloadimage supporta molti formati di immagini
(tra cui GIF, TIFF, JPEG. XPM, XBM, ecc.).

%description -l ja
xloadimage ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ï X Window System ¥¦¥£¥ó¥É¥¦¤Ë²èÁü¤òÉ½¼¨¤·¡¢
¥ë¡¼¥È¥¦¥£¥ó¥É¥¦¤Ø¤Î²èÁü¤Î¥í¡¼¥É¡¢¤Ş¤¿¤Ï¥Õ¥¡¥¤¥ë¤Ø¤Î²èÁü½ñ¤­¹ş¤ß¤ò¹Ô¤¤
¤Ş¤¹¡£xloadimage ¤Ç¤ÏÂ¿¤¯¤Î²èÁü¥¿¥¤¥× (GIF¡¢TIFF¡¢JPEG¡¢XPM¡¢XBM) ¤ò
¥µ¥İ¡¼¥È¤·¤Æ¤¤¤Ş¤¹¡£

%description -l pl
Xloadimage wy¶wietla obrazki w zwyk³ym i g³ównym oknie X Window lub
zapisuje je do pliku. Rozpoznaje wiele formatów plików graficznych,
m.in. GIF, TIFF, XPM, XBM, etc.

%description -l pt
O utilitário xloadimage mostra imagens numa janela do X Window System,
lê imagens para a janela de raiz, ou escreve imagens para um ficheiro.
O xloadimage suporta muitos tipos de imagem (GIF, TIFF, JPEG, XPM e
XBM).

%description -l ru
õÔÉÌÉÔÁ xloadimage ÄÅÍÏÎÓÔÒÉÒÕÅÔ ÉÚÏÂÒÁÖÅÎÉÑ × ÏËÎÅ X Window System,
×Ù×ÏÄÉÔ ÉÚÏÂÒÁÖÅÎÉÑ ÎÁ ÆÏÎ ÜËÒÁÎÁ ÉÌÉ ÚÁĞÉÓÙ×ÁÅÔ ÉÚÏÂÒÁÖÅÎÉÑ × ÆÁÊÌ.
Xloadimage ĞÏÄÄÅÒÖÉ×ÁÅÔ ÍÎÏÇÉÅ ÇÒÁÆÉŞÅÓËÉÅ ÆÏÒÍÁÔÙ (GIF, TIFF, JPEG,
XPM, XBM É Ô.Ä.).

%description -l sk
Nástroj xloadimage zobrazuje obrázky v systéme X Window, nahráva
obrázky do hlavného okna, alebo ich zapisuje do súboru. Xloadimage
podporuje mnoho typov obrázkov (GIF, TIFF, JPEG, XPM, XBM, atï.).

%description -l sv
Xloadimage är ett verktyg som visar bilder i ett X-fönster, laddar
bilder i rotfönstret, eller skriver bilder på en fil.  Xloadimage
hantera många bildtyper (GIF, TIFF, JPEG, XPM, XBM, etc.).

%description -l uk
õÔÉÌ¦ÔÁ xloadimage ĞÏËÁÚÕ¤ ÚÏÂÒÁÖÅÎÎÑ Õ ×¦ËÎ¦ X Window System, ÚÁ×ÁÎÔÁÖÕ¤
§È × ËÏÒÅÎÅ×Å ×¦ËÎÏ, ÁÂÏ ÚÁĞÉÓÕ¤ × ÆÁÊÌ. Xloadimage Ğ¦ÄÔÒÉÍÕ¤ ÂÁÇÁÔÏ
ÆÏÒÍÁÔ¦× ÇÒÁÆ¦ŞÎÉÈ ÆÁÊÌ¦× (GIF, TIFF, JPEG, XPM, XBM ÔÁ ¦ÎÛ¦).


%description -l zh_CN
xloadimage ÊµÓÃ³ÌĞòÓÃÓÚÔÚ X Window ÏµÍ³´°¿ÚÖĞÏÔÊ¾Í¼Ïó¡¢
ÔÚ¸ù´°¿ÚÖĞ×°ÔØÍ¼Ïó»òÔÚÎÄ¼şÖĞĞ´ÈëÍ¼Ïó¡£Xloadimage Ö§³Ö¶àÖÖÍ¼Ïó
ÀàĞÍ£¨GIF¡¢TIFF¡¢JPEG¡¢XPM ºÍ XBM µÈµÈ£©¡£

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1

cd jpeg
mv -f Makefile Makefile.orig
ln -sf makefile.ansi Makefile

%build
xmkmf

# it uses outdated, incompatible libjpeg 4a
%{__make} -C jpeg libjpeg.a \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdefsdir}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	SYSPATHFILE=$RPM_BUILD_ROOT%{_appdefsdir}/Xloadimage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xloadimagerc
%attr(755,root,root) %{_bindir}/xloadimage
%attr(755,root,root) %{_bindir}/xview
%attr(755,root,root) %{_bindir}/xsetbg

%{_appdefsdir}/Xloadimage
%{_mandir}/man1/xloadimage.1x*
