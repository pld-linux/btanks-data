# TODO:
# - pl description and summary
%define _name	btanks
Summary:	Fast 2d tank arcade game with multiplayer and split-screen modes
Name:		%{_name}-data
Version:	0.7.5800
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/btanks/%{_name}-%{version}.tar.bz2
# Source0-md5:	538eadf2b78897620f3ef683a4ea423a
URL:		http://btanks.sourceforge.net/blog/langswitch_lang/en
Requires:	%{_name} = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battle Tanks is a funny battle on your desk, where you can choose one
of three vehicles and eliminate your enemy using the whole arsenal of
weapons. It has original cartoon-like graphics and cool music, it is
fun and dynamic, it has several network modes for deathmatch and
cooperative - what else is needed to have fun with your friends?

And all is packed and ready for you in Battle Tanks.

This package contains Battle Tanks data files.

%prep
%setup -q -n %{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}
cp -r data $RPM_BUILD_ROOT%{_datadir}/%{_name}

# Game is looking for those libs in the datadir folder
ln -s %{_libdir}/libbt_objects.so $RPM_BUILD_ROOT%{_datadir}/%{_name}/libbt_objects.so
ln -s %{_libdir}/libbt.so $RPM_BUILD_ROOT%{_datadir}/%{_name}/libbt.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/*
