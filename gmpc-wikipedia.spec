Summary:	A wikipedia plugin for gmpc
Name:		gmpc-wikipedia
Version:	0.18.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.gz
Patch0:		gmpc-wikipedia-0.18.0-fix-str-fmt.patch
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
%patch0 -p0

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
