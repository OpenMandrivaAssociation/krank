%define		oversion	07

Name:		krank
Version:	0.7
Release:	%mkrel 1
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
%__rm -r levels/images/.DS_Store

%build
%__rm src/*.pyc
%__sed -i '/KRANKPATH=/s@=.*@=%{_gamesdatadir}/%{name}@' %{name}
%__sed -i '/^python/i\
export APPDATA="$HOME/.krank"\
%__mkdir_p "$APPDATA"\
cd $KRANKPATH
' %{name}
for N in 16 32 64 128; do convert %{SOURCE1} -resize ${N}x${N} $N.png; done

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}
for D in fonts html levels sounds src; do %__cp -a $D %{buildroot}%{_gamesdatadir}/%{name}/; done
%__install -D %{name} %{buildroot}%{_gamesbindir}/%{name}
%__install -D 16.png %{buildroot}%{_miconsdir}/%{name}.png
%__install -D 32.png %{buildroot}%{_liconsdir}/%{name}.png
%__install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Krank
Comment=Mouse magnet manipulation game
Exec=krank
Icon=krank
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt Info.plist README
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

