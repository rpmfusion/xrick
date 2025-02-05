%define _legacy_common_support 1
%define        tarversion    021212

Summary:       A clone of the game Rick Dangerous
Name:          xrick
Version:       0.0.%{tarversion}
Release:       26%{?dist}
License:       Distributable
URL:           http://www.bigorno.net/xrick/
Source0:       http://www.bigorno.net/xrick/%{name}-%{tarversion}.tgz
Patch1:        xrick-rpmoptflags-makefile.patch
Patch2:        xrick-021212-fix_format_security_error.patch
BuildRequires: gcc
BuildRequires: SDL-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
Requires:      hicolor-icon-theme


%description
xrick is a clone of Rick Dangerous. Written entirely in C, it relies
on the Simple DirectMedia Layer library and has been ported to Linux
(its primary target). Way before Lara Croft, back in the 1980's and
early 1990's, Rick Dangerous was the Indiana Jones of computer games,
running away from rolling rocks and avoiding traps in places from
South America to a futuristic missile base via Egypt and the
Schwarzendumpf castle.


%prep
%setup -q -n %{name}-%{tarversion}
%patch -P1 -p1
%patch -P2 -p1
sed -i 's:data.zip:%{_datadir}/%{name}/data.zip:g' src/xrick.c
# make xrick manpage UTF8
gunzip xrick.6.gz
iconv -f ISO-8859-1 -t UTF8 xrick.6 > xrick.6.tmp
touch -r xrick.6 xrick.6.tmp
mv xrick.6.tmp xrick.6
# convert xrick icon to png format
convert src/xrickST.ico xrickST.png


%build
%make_build


%install
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
  --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
  %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 xrickST.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps


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


%files
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/32x32/apps/xrickST.png


%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.021212-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.021212-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.021212-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.021212-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.021212-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0.021212-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.021212-14
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Sat Jul 28 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.0.021212-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 20 2018 Xavier Bachelot <xavier@bachelot.org> - 0.0.021212-12
- Add BR: gcc.
- Remove Group:.

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.0.021212-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.021212-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 Xavier Bachelot <xavier@bachelot.org> - 0.0.021212-9
- Fix format-security error.
- Preserve man page timestamp.
- Cleanup spec file.

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.021212-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.0.021212-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.0.021212-6
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.021212-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.0.021212-4
- rebuild for new F11 features

* Sun Oct 19 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0.021212-3
- Change EVR to 0:0.0.021212-3 for freshrpms upgrade path

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.0-0.7.021212
- rebuild

* Fri Sep 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0-0.6.021212
- install data files under /usr/share/xrick instead of /usr/share/games/xrick
- install icon into the fdo /usr/share/icons dir instead of /usr/share/pixmap
- make the manpage UTF-8
- start fullscreen

* Sat Mar 25 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.0-0.5.021212
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
