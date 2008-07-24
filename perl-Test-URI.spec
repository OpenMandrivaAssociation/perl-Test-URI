%define module  Test-URI
%define name    perl-%{module}
%define version 1.08
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Check Uniform Resource Identifiers
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(URI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
Check various parts of Uniform Resource Locators.

%prep
%setup -q -n %{module}-%{version}

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


