%define	version	2.4.2
%define release	%mkrel 3
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

