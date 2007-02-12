Summary:	An X Window System based image viewer
Summary(cs.UTF-8):   Prohlížeč obrázků na pro X Window System
Summary(da.UTF-8):   Billledvisningsprogram for X vinduesystemet
Summary(de.UTF-8):   Ein Bild-Anzeiger für das X Window System
Summary(es.UTF-8):   Visor de imágenes para X Window
Summary(fr.UTF-8):   Programme d'affichage d'images basé sur le système X Window
Summary(id.UTF-8):   Utility X Window System untuk melihat gambar
Summary(is.UTF-8):   Myndbirtir fyrir X gluggakerfið
Summary(it.UTF-8):   Visualizzatore di immagini per X Window
Summary(ja.UTF-8):   X Window System ベースの画像ビューア
Summary(ko.UTF-8):   X 윈도우 시스템 기반 이미지 보기 프로그램
Summary(nb.UTF-8):   Bildevisningsprogram for X vindusystemet
Summary(pl.UTF-8):   Przeglądarka obrazków dla X Window
Summary(pt.UTF-8):   Um visualizador de imagens baseado em X Window System
Summary(ru.UTF-8):   Программа просмотра изображений в X Window System
Summary(sk.UTF-8):   Prehliadač obrázkov pre systém X Window
Summary(sl.UTF-8):   Pregledovalnik slik za Okna X
Summary(sv.UTF-8):   En bildvisare för X11
Summary(uk.UTF-8):   Програма перегляду зображень під X Window System
Summary(zh_CN.UTF-8):   一个基于 X 窗口系统的图像查看器。
Name:		xloadimage
Version:	4.1
Release:	28
License:	MIT
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
# Source0-md5:	7331850fc04056ab8ae6b5725d1fb3d2
Patch0:		%{name}-linux.patch
Patch1:		%{name}-nobr.patch
Patch2:		%{name}-unaligned.patch
Patch3:		%{name}-buffer.patch
Patch4:		%{name}-errno.patch
Patch5:		%{name}-varargs2stdarg.patch
BuildRequires:	libtiff-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir		%{_datadir}/X11/app-defaults
%define		_noautocompressdoc	*rc

%description
The xloadimage utility displays images in an X Window System window,
loads images into the root window, or writes images into a file.
Xloadimage supports many images types (GIF, TIFF, JPEG, XPM, XBM,
etc.).

%description -l cs.UTF-8
Xloadimage zobrazuje obrázky v X Window Systemu, umisťuje obrázky do
kořenového okna nebo ukládá obrázky do souboru. Podporuje množství
formátů (GIF, TIFF, JPEG, XPM, XBM, atd.).

%description -l da.UTF-8
Xloadimage er et værktøj som viser billeder i et X-vindue, indlæser
billeder i rodvinduet, eller skriver billeder på en fil.  Xloadimage
behandler mange billedtyper (GIF, TIFF, JPEG, XPM, XBM, etc.).

%description -l de.UTF-8
Das Dienstprogramm xloadimage zeigt Bilder in einem X Window
System-Fenster an, lädt Bilder in das Root-Fenster oder schreibt
Bilder in eine Datei. Xloadimage unterstützt viele Bildformate (GIF,
TIFF, JPEG, XPM, XBM usw.).

%description -l es.UTF-8
La utilidad xloadimage muestra imágenes en una ventana de X Window,
carga imágenes en la ventana de fondo o las escribe en un fichero.
Xloadimage soporta múltiples formatos de imagen(GIF, TIFF, JPEG. XPM,
XBM, etc.).

%description -l fr.UTF-8
L'utilitaire xloadimage affiche des images dans une fenêtre du système X
Window, charge des images dans la fenêtre root ou écrit des images dans
un fichier. Xloadimage prend en charge de nombreux types d'image (GIF,
TIFF, JPEG, XPM et XBM).

%description -l id.UTF-8
Utility xloadimage menampilkan gambar di sebuah window pada X Window
System, di root window, atau menyimpan gambar ke dalam file. Xloadimage
menukung banyak type gambar (GIF, TIFF, JPEG, XPM, XBM, dll.).

%description -l is.UTF-8
Xloadimage forritið birtir myndir í glugga X gluggakerfis, hleður
myndir í rótargluggann, eða skrifar myndir í skrá. Xloadimage styður
margar tegundir mynda (GIF, TIFF, JPEG, XPM, XBM, o.fl.).

%description -l it.UTF-8
Il programma xloadimage visualizza un'immagine in una finestra del
sistema X Window, carica le immagini nella finestra di root o salva
le immagini in un file. Xloadimage supporta molti formati di immagini
(tra cui GIF, TIFF, JPEG. XPM, XBM, ecc.).

%description -l ja.UTF-8
xloadimage ユーティリティは X Window System ウィンドウに画像を表示し、
ルートウィンドウへの画像のロード、またはファイルへの画像書き込みを行い
ます。xloadimage では多くの画像タイプ (GIF、TIFF、JPEG、XPM、XBM) を
サポートしています。

%description -l pl.UTF-8
Xloadimage wyświetla obrazki w zwykłym i głównym oknie X Window lub
zapisuje je do pliku. Rozpoznaje wiele formatów plików graficznych,
m.in. GIF, TIFF, XPM, XBM, etc.

%description -l pt.UTF-8
O utilitário xloadimage mostra imagens numa janela do X Window System,
lê imagens para a janela de raiz, ou escreve imagens para um ficheiro.
O xloadimage suporta muitos tipos de imagem (GIF, TIFF, JPEG, XPM e
XBM).

%description -l ru.UTF-8
Утилита xloadimage демонстрирует изображения в окне X Window System,
выводит изображения на фон экрана или записывает изображения в файл.
Xloadimage поддерживает многие графические форматы (GIF, TIFF, JPEG,
XPM, XBM и т.д.).

%description -l sk.UTF-8
Nástroj xloadimage zobrazuje obrázky v systéme X Window, nahráva
obrázky do hlavného okna, alebo ich zapisuje do súboru. Xloadimage
podporuje mnoho typov obrázkov (GIF, TIFF, JPEG, XPM, XBM, atď.).

%description -l sv.UTF-8
Xloadimage är ett verktyg som visar bilder i ett X-fönster, laddar
bilder i rotfönstret, eller skriver bilder på en fil.  Xloadimage
hantera många bildtyper (GIF, TIFF, JPEG, XPM, XBM, etc.).

%description -l uk.UTF-8
Утиліта xloadimage показує зображення у вікні X Window System, завантажує
їх в кореневе вікно, або записує в файл. Xloadimage підтримує багато
форматів графічних файлів (GIF, TIFF, JPEG, XPM, XBM та інші).


%description -l zh_CN.UTF-8
xloadimage 实用程序用于在 X Window 系统窗口中显示图象、
在根窗口中装载图象或在文件中写入图象。Xloadimage 支持多种图象
类型（GIF、TIFF、JPEG、XPM 和 XBM 等等）。

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
	CDEBUGFLAGS="%{rpmcflags}" \
	SYSPATHFILE="%{_appdefsdir}/Xloadimage"

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
%attr(755,root,root) %{_bindir}/uufilter
%attr(755,root,root) %{_bindir}/xloadimage
%attr(755,root,root) %{_bindir}/xview
%attr(755,root,root) %{_bindir}/xsetbg
%{_appdefsdir}/Xloadimage
%{_mandir}/man1/uufilter.1x*
%{_mandir}/man1/xloadimage.1x*
