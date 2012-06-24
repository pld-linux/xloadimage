Summary:	An X Window System based image viewer
Summary(cs):	Prohl�e� obr�zk� na pro X Window System
Summary(da):	Billledvisningsprogram for X vinduesystemet
Summary(de):	Ein Bild-Anzeiger f�r das X Window System
Summary(es):	Visor de im�genes para X Window
Summary(fr):	Programme d'affichage d'images bas� sur le syst�me X Window
Summary(id):	Utility X Window System untuk melihat gambar
Summary(is):	Myndbirtir fyrir X gluggakerfi�
Summary(it):	Visualizzatore di immagini per X Window
Summary(ja):	X Window System �١����β����ӥ塼��
Summary(ko):	X ������ �ý��� ��� �̹��� ���� ���α׷�
Summary(no):	Bildevisningsprogram for X vindusystemet
Summary(pl):	Przegl�darka obrazk�w dla X Window
Summary(pt):	Um visualizador de imagens baseado em X Window System
Summary(ru):	��������� ��������� ����������� � X Window System
Summary(sk):	Prehliada� obr�zkov pre syst�m X Window
Summary(sl):	Pregledovalnik slik za Okna X
Summary(sv):	En bildvisare f�r X11
Summary(uk):	�������� ��������� ��������� Ц� X Window System
Summary(zh_CN):	һ������ X ����ϵͳ��ͼ��鿴����
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
Xloadimage zobrazuje obr�zky v X Window Systemu, umis�uje obr�zky do
ko�enov�ho okna nebo ukl�d� obr�zky do souboru. Podporuje mno�stv�
form�t� (GIF, TIFF, JPEG, XPM, XBM, atd.).

%description -l da
Xloadimage er et v�rkt�j som viser billeder i et X-vindue, indl�ser
billeder i rodvinduet, eller skriver billeder p� en fil.  Xloadimage
behandler mange billedtyper (GIF, TIFF, JPEG, XPM, XBM, etc.).

%description -l de
Das Dienstprogramm xloadimage zeigt Bilder in einem X Window
System-Fenster an, l�dt Bilder in das Root-Fenster oder schreibt
Bilder in eine Datei. Xloadimage unterst�tzt viele Bildformate (GIF,
TIFF, JPEG, XPM, XBM usw.).

%description -l es
La utilidad xloadimage muestra im�genes en una ventana de X Window,
carga im�genes en la ventana de fondo o las escribe en un fichero.
Xloadimage soporta m�ltiples formatos de imagen(GIF, TIFF, JPEG. XPM,
XBM, etc.).

%description -l fr
L'utilitaire xloadimage affiche des images dans une fen�tre du syst�me X
Window, charge des images dans la fen�tre root ou �crit des images dans
un fichier. Xloadimage prend en charge de nombreux types d'image (GIF,
TIFF, JPEG, XPM et XBM).

%description -l id
Utility xloadimage menampilkan gambar di sebuah window pada X Window
System, di root window, atau menyimpan gambar ke dalam file. Xloadimage
menukung banyak type gambar (GIF, TIFF, JPEG, XPM, XBM, dll.).

%description -l is
Xloadimage forriti� birtir myndir � glugga X gluggakerfis, hle�ur
myndir � r�targluggann, e�a skrifar myndir � skr�. Xloadimage sty�ur
margar tegundir mynda (GIF, TIFF, JPEG, XPM, XBM, o.fl.).

%description -l it
Il programma xloadimage visualizza un'immagine in una finestra del
sistema X Window, carica le immagini nella finestra di root o salva
le immagini in un file. Xloadimage supporta molti formati di immagini
(tra cui GIF, TIFF, JPEG. XPM, XBM, ecc.).

%description -l ja
xloadimage �桼�ƥ���ƥ��� X Window System ������ɥ��˲�����ɽ������
�롼�ȥ�����ɥ��ؤβ����Υ��ɡ��ޤ��ϥե�����ؤβ����񤭹��ߤ�Ԥ�
�ޤ���xloadimage �Ǥ�¿���β��������� (GIF��TIFF��JPEG��XPM��XBM) ��
���ݡ��Ȥ��Ƥ��ޤ���

%description -l pl
Xloadimage wy�wietla obrazki w zwyk�ym i g��wnym oknie X Window lub
zapisuje je do pliku. Rozpoznaje wiele format�w plik�w graficznych,
m.in. GIF, TIFF, XPM, XBM, etc.

%description -l pt
O utilit�rio xloadimage mostra imagens numa janela do X Window System,
l� imagens para a janela de raiz, ou escreve imagens para um ficheiro.
O xloadimage suporta muitos tipos de imagem (GIF, TIFF, JPEG, XPM e
XBM).

%description -l ru
������� xloadimage ������������� ����������� � ���� X Window System,
������� ����������� �� ��� ������ ��� ���������� ����������� � ����.
Xloadimage ������������ ������ ����������� ������� (GIF, TIFF, JPEG,
XPM, XBM � �.�.).

%description -l sk
N�stroj xloadimage zobrazuje obr�zky v syst�me X Window, nahr�va
obr�zky do hlavn�ho okna, alebo ich zapisuje do s�boru. Xloadimage
podporuje mnoho typov obr�zkov (GIF, TIFF, JPEG, XPM, XBM, at�.).

%description -l sv
Xloadimage �r ett verktyg som visar bilder i ett X-f�nster, laddar
bilder i rotf�nstret, eller skriver bilder p� en fil.  Xloadimage
hantera m�nga bildtyper (GIF, TIFF, JPEG, XPM, XBM, etc.).

%description -l uk
���̦�� xloadimage �����դ ���������� � צ�Φ X Window System, ��������դ
�� � �������� צ���, ��� �����դ � ����. Xloadimage Ц�����դ ������
�����Ԧ� ���Ʀ���� ���̦� (GIF, TIFF, JPEG, XPM, XBM �� ��ۦ).


%description -l zh_CN
xloadimage ʵ�ó��������� X Window ϵͳ��������ʾͼ��
�ڸ�������װ��ͼ������ļ���д��ͼ��Xloadimage ֧�ֶ���ͼ��
���ͣ�GIF��TIFF��JPEG��XPM �� XBM �ȵȣ���

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
