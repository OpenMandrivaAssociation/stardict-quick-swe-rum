%define	version	2.4.2
%define release	%mkrel 6
%define dict_format_version	2.4.2

Summary:	Swedish -> Romanian *Quick dictionary for StarDict 2
Name:		stardict-quick-swe-rum
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-quick_swe-rum-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
Swedish -> Romanian *Quick dictionary in StarDict 2 format.
*Quick is an open source translation application. For more info, visit

http://www.futureware.at/.

%prep
%setup -q -n stardict-quick_swe-rum-%{version}
# tarball contains broken filename
for i in *; do mv -f $i ${i/\?\?/an}; done

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*



%changelog
* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-6mdv2009.0
+ Revision: 261122
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-5mdv2009.0
+ Revision: 253484
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.4.2-3mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-3mdv2008.0
+ Revision: 67745
- use %%mkrel


* Wed Oct 05 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- Rebuild

* Tue Jun 01 2004 Abel Cheung <deaddog@deaddog.org> 2.4.2-2mdk
- Dictionaries require main program as well

* Fri Nov 28 2003 Abel Cheung <deaddog@deaddog.org> 2.4.2-1mdk
- New version
- Conflict with old version of stardict

* Mon Jul 28 2003 Abel Cheung <maddog@linux.org.hk> 2.1.0-1mdk
- First Mandrake style spec

