%define upstream_name    Test-URI
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Check Uniform Resource Identifiers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(URI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description 
Check various parts of Uniform Resource Locators.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*
