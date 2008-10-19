%define		tarversion	021212

Summary: 	A clone of the game Rick Dangerous
Name: 		xrick
Version: 	0.0.%{tarversion}
Release: 	3%{?dist}
License: 	Distributable
Group: 		Amusements/Games
URL:		http://www.bigorno.net/xrick/
Source0: 	http://www.bigorno.net/xrick/%{name}-%{tarversion}.tgz
Patch1:		xrick-rpmoptflags-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	SDL-devel zlib-devel desktop-file-utils ImageMagick
Requires:	hicolor-icon-theme

#---------------------------------------------------------------------

%description
xrick is a clone of Rick Dangerous. Written entirely in C, it relies
on the Simple DirectMedia Layer library and has been ported to Linux
(its primary target). Way before Lara Croft, back in the 1980's and
early 1990's, Rick Dangerous was the Indiana Jones of computer games,
running away from rolling rocks and avoiding traps in places from
South America to a futuristic missile base via Egypt and the
Schwarzendumpf castle.

#---------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{tarversion}
%patch1 -p1
sed -i 's:data.zip:%{_datadir}/%{name}/data.zip:g' src/xrick.c
# make xrick manpage UTF8
gunzip xrick.6.gz
iconv -f ISO-8859-1 -t UTF8 xrick.6 > xrick.6.tmp
mv xrick.6.tmp xrick.6

#---------------------------------------------------------------------

%build
make %{?_smp_mflags}
convert src/xrickST.ico xrickST.png

#---------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
install -m 0755 xrick $RPM_BUILD_ROOT/%{_bindir}
install -m 0644 data.zip $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m 0644 xrick.6 $RPM_BUILD_ROOT/%{_mandir}/man6

cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=X Rick
Comment=A "Rick Dangerous" Clone.
Exec=%{name} -fullscreen
Icon=xrickST.png
Terminal=false
Type=Application
Categories=Game;ActionGame;
EOF

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
desktop-file-install --vendor rpmfusion \
  --dir $RPM_BUILD_ROOT/%{_datadir}/applications    \
  %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 xrickST.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

#---------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

#---------------------------------------------------------------------

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

#---------------------------------------------------------------------

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/32x32/apps/xrickST.png

#---------------------------------------------------------------------

%changelog
* Sun Oct 19 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0.021212-3
- Change EVR to 0:0.0.021212-3 for freshrpms upgrade path

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.0-0.7.021212
- rebuild

* Fri Sep 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0-0.6.021212
- install data files under /usr/share/xrick instead of /usr/share/games/xrick
- install icon into the fdo /usr/share/icons dir instead of /usr/share/pixmap
- make the manpage UTF-8
- start fullscreen

* Sat Mar 25 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.0-0.5.021212
- fix release
- remove epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Aug  5 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.4.021212
- using convert at build time to do ico->png conversion

* Thu Jul 17 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.3.021212
- Added icon for menu

* Wed Jun 18 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.2.0212120
- Desktop entry : oops !! Sorry.

* Tue Jun 17 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.1.0212120
- Modified Summary
- Package now own datadir/games/xrick directory

* Mon May 19 2003 Dams <anvil[AT]livna.org> 0:021212-0.fdr.4
- Added a desktop entry. BuildRequires desktop-file-utils.
- Modified the patch to keep ansi/pedantic and other gcc warning flags

* Tue May 13 2003 Dams <anvil[AT]livna.org> 0:021212-0.fdr.3
- Patch to accept RPM_OPT_FLAGS from Michael Schwendt

* Tue May 13 2003 Dams <anvil[AT]livna.org> 0:021212-0.fdr.2
- buildroot -> RPM_BUILD_ROOT
- Modified Source0

* Wed Apr 23 2003 Dams <anvil[AT]livna.org> 
- Initial build.
