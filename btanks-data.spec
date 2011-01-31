%define _name	btanks
Summary:	Data for Battle Tanks arcade game with multiplayer and split-screen modes
Summary(pl.UTF-8):	Dane do gry zręcznościowej Battle Tanks z trybem dla wielu graczy
Name:		%{_name}-data
Version:	0.9.8083
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/btanks/%{_name}-%{version}.tar.bz2
# Source0-md5:	49cb95c0eec47d3436c4fdf65e7c9d12
URL:		http://btanks.sourceforge.net/blog/
BuildRequires:	zip
Requires:	%{_name} = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battle Tanks is a funny battle on your desk, where you can choose one
of three vehicles and eliminate your enemy using the whole arsenal of
weapons. It has original cartoon-like graphics and cool music, it is
fun and dynamic, it has several network modes for deathmatch and
cooperative - what else is needed to have fun with your friends?

This package contains Battle Tanks data files.

%description -l pl.UTF-8
Battle Tanks to zabawna gra, w której można wybrać jeden z trzech
pojazdów i eliminować wrogów przy użyciu całego arsenału broni. Ma
oryginalną grafikę w stylu kreskówek i świetną muzykę; jest zabawna i
dynamiczna, ma kilka trybów sieciowych, pozwalających na grę przeciwko
wszystkim oraz współpracę - cóż więcej potrzeba do zabawy z kolegami?

Ten pakiet zawiera pliki z danymi dla Battle Tanks.

%prep
%setup -q -n %{_name}-%{version}/data
zip -q -0 -r resources.dat .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}
cp -a resources.dat $RPM_BUILD_ROOT%{_datadir}/%{_name}/resources.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/resources.dat
