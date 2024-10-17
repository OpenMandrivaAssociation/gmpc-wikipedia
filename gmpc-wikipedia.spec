Summary:	A wikipedia plugin for gmpc
Name:		gmpc-wikipedia
Version:	0.20.0
Release:	5
License:	GPLv2+
Group:		Sound
Url:		https://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	webkitgtk-devel
BuildRequires:	intltool
Requires:	gmpc

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
%{_libdir}/gmpc/plugins/wikiplugin.so
%{_datadir}/gmpc/plugins/wikipedia/wikipedia.png


%changelog
* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 686167
- rebuild for new webkit

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2mdv2011.0
+ Revision: 610910
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531614
- new version 0.20.0

* Sat Dec 26 2009 Funda Wang <fwang@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 482399
- BR intltool
- New version 0.19.0

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 379432
- New version 0.18.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246329
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160454
- add spec file
- add source
- Created package structure for gmpc-wikipedia.

