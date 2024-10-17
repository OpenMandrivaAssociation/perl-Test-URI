%define upstream_name    Test-URI
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Check Uniform Resource Identifiers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description 
Check various parts of Uniform Resource Locators.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 405600
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-4mdv2009.0
+ Revision: 258582
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-3mdv2009.0
+ Revision: 246572
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.1
+ Revision: 152904
- update to new version 1.08
- update to new version 1.08

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2008.0
+ Revision: 63965
- update to new version 1.07


* Mon Jan 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2007.0
+ Revision: 111627
- new version
- Import perl-Test-URI

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-2mdv2007.0
- Rebuild

* Sat May 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdk
- New release 1.05
- test in %%check

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-3mdk
- Fix SPEC according to Perl Policy
    - BuildRequires
    - Source URL

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-2mdk
- Fix BuildRequires

* Tue Apr 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdk 
- new release
- spec cleanup
- better url
- rpmbuildupdate aware

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5-0.04.3mdk
- fix buildrequires in a backward compatible way

* Sun Aug 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5-0.04.2mdk 
- fix directory ownership (distlint)
- buildrequires

* Wed Mar 31 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5-0.04.1mdk
- first mdk release

