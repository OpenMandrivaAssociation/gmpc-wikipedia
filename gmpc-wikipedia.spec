Summary:	A wikipedia plugin for gmpc
Name:		gmpc-wikipedia
Version:	0.19.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://sourceforge.net/projects/musicpd/files/gmpc-plugins/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	webkitgtk-devel
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A wikipedia plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/wikiplugin.la
%{_libdir}/gmpc/plugins/wikiplugin.so
%{_datadir}/gmpc/plugins/wikipedia/wikipedia.png
