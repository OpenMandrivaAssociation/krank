%define		oversion	07

Name:		krank
Version:	0.7
Release:	3
Summary:	Mouse magnet manipulation game with nifty graphics
Group:		Games/Puzzles
License:	Public Domain
URL:		http://krank.sourceforge.net/
Source:		%{name}-%{oversion}.tar.bz2
Source1:	%{name}.png
BuildRequires:	imagemagick
Requires:	pygame
Buildarch:	noarch

%description
A game of dexterity, being somewhere between Breakout and billiard, where
the aim of each level is to shove floating stones towards compatible static
stones. You control a short chain of stones with your mouse to achieve that.

%prep
%setup -q -n %{name}-%{oversion}
rm -r levels/images/.DS_Store

%build
rm src/*.pyc
sed -i '/KRANKPATH=/s@=.*@=%{_gamesdatadir}/%{name}@' %{name}
sed -i '/^python/i\
export APPDATA="$HOME/.krank"\
mkdir -p "$APPDATA"\
cd $KRANKPATH
' %{name}
for N in 16 32 64 128; do convert %{SOURCE1} -resize ${N}x${N} $N.png; done

%install
mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
for D in fonts html levels sounds src; do cp -a $D %{buildroot}%{_gamesdatadir}/%{name}/; done
install -D %{name} %{buildroot}%{_gamesbindir}/%{name}
install -D 16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D 32.png %{buildroot}%{_liconsdir}/%{name}.png
install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Krank
Comment=Mouse magnet manipulation game
Exec=krank
Icon=krank
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt Info.plist README
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
* Tue Mar 13 2012 Andrey Bondrov <abondrov@mandriva.org> 0.7-1
+ Revision: 784518
- imported package krank

